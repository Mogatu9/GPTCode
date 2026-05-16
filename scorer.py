"""
Scorer v1  --  Composite scoring & ranking of screener output.
Reads the latest screener_pass_*.csv, scores each stock across
5 weighted metrics, and outputs a ranked leaderboard + CSV.

Weights:
  PEG ratio       30%  (lower = better)
  Forward P/E     20%  (lower = better)
  Revenue Growth  20%  (higher = better)
  ROE             15%  (higher = better)
  Debt/Equity     15%  (lower = better)
"""

import csv
import os
import glob
from datetime import datetime

# ── Weights (must sum to 1.0) ─────────────────────────────────────────────────
WEIGHTS = {
    "peg":        0.30,
    "fwd_pe":     0.20,
    "rev_growth": 0.20,
    "roe":        0.15,
    "debt_eq":    0.15,
}

# Metrics where lower value = better score
LOWER_IS_BETTER = {"peg", "fwd_pe", "debt_eq"}

# Clip outliers at these percentiles before normalising
CLIP_PCT = 0.05   # bottom 5% and top 5% clipped


def find_latest_csv(pattern):
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def load_csv(path):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def parse_float(val):
    try:
        return float(str(val).replace("%", "").strip())
    except (ValueError, TypeError):
        return None


def extract(row):
    return {
        "ticker":     row.get("ticker", "").strip(),
        "name":       row.get("name", "").strip(),
        "peg":        parse_float(row.get("peg")),
        "fwd_pe":     parse_float(row.get("fwd_pe")),
        "rev_growth": parse_float(row.get("rev_growth_pct")),
        "roe":        parse_float(row.get("roe_pct")),
        "debt_eq":    parse_float(row.get("debt_to_equity")),
        "mkt_cap":    row.get("mkt_cap", ""),
        "price":      row.get("price", ""),
    }


def clip_values(values, pct=CLIP_PCT):
    valid = sorted(v for v in values if v is not None)
    if len(valid) < 4:
        return None, None
    lo_idx = max(0, int(len(valid) * pct))
    hi_idx = min(len(valid) - 1, int(len(valid) * (1 - pct)))
    return valid[lo_idx], valid[hi_idx]


def normalise(value, lo, hi, lower_is_better):
    if value is None or lo is None or hi is None or hi == lo:
        return None
    value = max(lo, min(hi, value))   # clip to [lo, hi]
    ratio = (value - lo) / (hi - lo)
    score = (1 - ratio) if lower_is_better else ratio
    return round(score * 100, 2)


def score_stocks(stocks):
    metrics = list(WEIGHTS.keys())

    # Build per-metric clip bounds from all stocks
    bounds = {}
    for m in metrics:
        vals = [s[m] for s in stocks]
        lo, hi = clip_values(vals)
        bounds[m] = (lo, hi)

    scored = []
    for s in stocks:
        component_scores = {}
        for m in metrics:
            lo, hi = bounds[m]
            ns = normalise(s[m], lo, hi, m in LOWER_IS_BETTER)
            component_scores[m] = ns

        # Weighted composite — skip metrics with no score
        total_weight = 0.0
        composite = 0.0
        for m, w in WEIGHTS.items():
            ns = component_scores[m]
            if ns is not None:
                composite += ns * w
                total_weight += w

        composite = round(composite / total_weight * 100, 1) if total_weight > 0 else 0.0

        scored.append({**s, **{f"score_{m}": component_scores[m] for m in metrics},
                       "composite": composite})

    scored.sort(key=lambda x: x["composite"], reverse=True)
    return scored


def save_csv(scored, path):
    fieldnames = [
        "rank", "ticker", "name", "composite",
        "peg", "score_peg",
        "fwd_pe", "score_fwd_pe",
        "rev_growth", "score_rev_growth",
        "roe", "score_roe",
        "debt_eq", "score_debt_eq",
        "mkt_cap", "price",
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for rank, s in enumerate(scored, 1):
            w.writerow({**s, "rank": rank})


def fmt(val, decimals=2, suffix=""):
    if val is None:
        return "N/A"
    return f"{round(val, decimals)}{suffix}"


def print_leaderboard(scored, top_n=30):
    print()
    print("=" * 82)
    print(f"  COMPOSITE LEADERBOARD  --  top {min(top_n, len(scored))} of {len(scored)}")
    print(f"  {'Rank':<5} {'Ticker':<8} {'Score':>6}  "
          f"{'PEG':>5}  {'FwdPE':>6}  {'RevGrw':>7}  {'ROE':>6}  {'D/E':>6}  MktCap")
    print("-" * 82)
    for rank, s in enumerate(scored[:top_n], 1):
        rg = fmt(s["rev_growth"], 1, "%") if s["rev_growth"] is not None else "N/A"
        roe = fmt(s["roe"], 1, "%") if s["roe"] is not None else "N/A"
        print(
            f"  {rank:<5} {s['ticker']:<8} {s['composite']:>6.1f}  "
            f"{fmt(s['peg']):>5}  {fmt(s['fwd_pe'], 1):>6}  "
            f"{rg:>7}  {roe:>6}  {fmt(s['debt_eq'], 1):>6}  {s['mkt_cap']}"
        )
    print("=" * 82)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Find latest screener_pass CSV
    pattern = os.path.join(script_dir, "screener_pass_*.csv")
    csv_path = find_latest_csv(pattern)
    if not csv_path:
        raise SystemExit(
            "No screener_pass_*.csv found. Run peg_screener.py first."
        )

    print(f"  Reading: {os.path.basename(csv_path)}")
    raw_rows = load_csv(csv_path)
    stocks   = [extract(r) for r in raw_rows]
    stocks   = [s for s in stocks if s["ticker"]]   # drop blanks

    print(f"  {len(stocks)} stocks loaded  |  scoring on 5 metrics")

    scored = score_stocks(stocks)
    print_leaderboard(scored, top_n=30)

    # Save
    ts       = datetime.now().strftime("%Y%m%d_%H%M")
    out_path = os.path.join(script_dir, f"scored_ranked_{ts}.csv")
    save_csv(scored, out_path)
    print(f"\n  Saved: {out_path}")
    print(f"\n  Feed top 20-30 tickers into WBA for deep fundamental analysis.")


if __name__ == "__main__":
    main()
