"""
PEG Screener v4  --  Multi-filter stock screener
Filters: PEG < 2.0 | Forward P/E < 30 | Revenue Growth > 5% | Market Cap > $1B
Saves passing stocks to CSV.
Uses requests only (no yfinance / pandas / numpy) -- works on Android.
"""

import time
import random
import csv
import os
from datetime import datetime

try:
    import requests
except ImportError:
    raise SystemExit("Run:  pip install requests")

VERSION = "v4-multifilter"

# ── Thresholds ────────────────────────────────────────────────────────────────
PEG_MAX        = 2.0      # PEG ratio upper limit
FWD_PE_MAX     = 30.0     # Forward P/E upper limit
REV_GROWTH_MIN = 0.05     # Revenue growth minimum (5%)
MKTCAP_MIN     = 1e9      # Market cap minimum ($1B)

MAX_RETRIES = 4

ALL_STOCKS = sorted([
    "AAPL", "ABNB", "ACN", "ADBE", "ADI", "ALC", "AMD", "AMSC", "AMZN",
    "ANET", "APP", "ARM", "AVGO", "AZO", "BA", "BAC", "BBY", "BFAM",
    "BIIB", "BMY", "BRK-B", "BURL", "CAT", "CEG", "CELH", "CI", "CLS",
    "COST", "CRDO", "CRM", "CRWD", "CSCO", "CVX", "DASH", "DDOG", "DELL",
    "DG", "DIS", "DKS", "DOCN", "DRI", "EAT", "EGHT", "EQIX", "ESTC",
    "FIVN", "FIX", "FTNT", "GAP", "GEV", "GILD", "GLD", "GOOGL", "GS",
    "HD", "HOOD", "HPE", "HUBS", "IAU", "IBM", "INOD", "INTC", "INTU",
    "IONQ", "ISRG", "JNJ", "JPM", "KO", "LLY", "LOW", "LULU", "MA",
    "MDB", "MELI", "META", "MNMD", "MRK", "MRVL", "MSFT", "MU", "NEE",
    "NET", "NICE", "NKE", "NOW", "NVDA", "OKTA", "ORCL", "OSK", "PANW",
    "PG", "PLTR", "PSTG", "QCOM", "RDDT", "RKLB", "RMBS", "RNG", "ROKU",
    "ROST", "SAP", "SBUX", "SIBN", "SMCI", "SNOW", "SOUN", "SPOT", "STZ",
    "TEAM", "TGT", "TJX", "TRU", "TSLA", "TSM", "TTD", "TWLO", "TXN",
    "UBER", "ULTA", "UNH", "V", "VEEV", "VRNT", "VRTX", "W", "WDAY",
    "WDC", "WMT", "XOM", "ZM", "ZS",
])

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

MODULES = "defaultKeyStatistics,financialData,summaryDetail,price"


def get_session_and_crumb():
    session = requests.Session()
    session.headers.update(HEADERS)
    try:
        session.get("https://finance.yahoo.com", timeout=12)
    except Exception as e:
        raise SystemExit(f"Cannot reach Yahoo Finance: {e}")
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(
                "https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=12
            )
            crumb = r.text.strip()
            if crumb and "<" not in crumb:
                print(f"  [OK] Session established (crumb: {crumb[:6]}...)")
                return session, crumb
        except Exception:
            pass
        time.sleep(2 ** attempt)
    raise SystemExit("Failed to obtain Yahoo Finance crumb.")


def fetch_data(session, crumb, ticker: str):
    url = (
        "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
        f"{ticker}?modules={MODULES}&crumb={crumb}"
    )
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, timeout=12)
            data = r.json()
            result = data.get("quoteSummary", {}).get("result")
            if not result:
                return None
            res = result[0]

            ks  = res.get("defaultKeyStatistics", {})
            fd  = res.get("financialData", {})
            sd  = res.get("summaryDetail", {})
            pr  = res.get("price", {})

            def raw(d, key):
                val = d.get(key, {})
                if isinstance(val, dict):
                    return val.get("raw")
                return val

            return {
                "ticker":      ticker,
                "name":        pr.get("shortName", ""),
                "peg":         raw(ks, "pegRatio"),
                "fwd_pe":      raw(ks, "forwardPE"),
                "trailing_pe": raw(sd, "trailingPE"),
                "rev_growth":  raw(fd, "revenueGrowth"),
                "mkt_cap":     raw(pr, "marketCap"),
                "price":       raw(pr, "regularMarketPrice"),
                "roe":         raw(fd, "returnOnEquity"),
                "debt_eq":     raw(fd, "debtToEquity"),
            }
        except Exception:
            if attempt == MAX_RETRIES:
                return None
            time.sleep(2 ** (attempt - 1) + random.uniform(0, 1))
    return None


def fmt_cap(v):
    if v is None:
        return "N/A"
    if v >= 1e12:
        return f"${v/1e12:.2f}T"
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    return f"${v/1e6:.0f}M"


def passes_all(d):
    if d is None:
        return False
    peg = d["peg"]
    fpe = d["fwd_pe"]
    rg  = d["rev_growth"]
    mc  = d["mkt_cap"]
    if peg  is None or peg  >= PEG_MAX:        return False
    if fpe  is None or fpe  >= FWD_PE_MAX:     return False
    if rg   is None or rg   <  REV_GROWTH_MIN: return False
    if mc   is None or mc   <  MKTCAP_MIN:     return False
    return True


def save_csv(rows, path):
    fieldnames = [
        "ticker", "name", "peg", "fwd_pe", "trailing_pe",
        "rev_growth_pct", "mkt_cap", "price", "roe_pct", "debt_to_equity"
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for d in rows:
            w.writerow({
                "ticker":         d["ticker"],
                "name":           d["name"],
                "peg":            round(d["peg"], 2)      if d["peg"]        is not None else "",
                "fwd_pe":         round(d["fwd_pe"], 2)   if d["fwd_pe"]     is not None else "",
                "trailing_pe":    round(d["trailing_pe"], 2) if d["trailing_pe"] is not None else "",
                "rev_growth_pct": f"{d['rev_growth']*100:.1f}" if d["rev_growth"] is not None else "",
                "mkt_cap":        fmt_cap(d["mkt_cap"]),
                "price":          round(d["price"], 2)    if d["price"]      is not None else "",
                "roe_pct":        f"{d['roe']*100:.1f}"   if d["roe"]        is not None else "",
                "debt_to_equity": round(d["debt_eq"], 2)  if d["debt_eq"]    is not None else "",
            })


def main():
    total = len(ALL_STOCKS)
    all_rows   = []
    pass_rows  = []

    print("=" * 70)
    print(f"  PEG SCREENER {VERSION}")
    print(f"  Filters: PEG<{PEG_MAX} | Fwd P/E<{FWD_PE_MAX} | "
          f"Rev Growth>{REV_GROWTH_MIN*100:.0f}% | MktCap>${MKTCAP_MIN/1e9:.0f}B")
    print(f"  {total} tickers  |  source: Yahoo Finance (cookie+crumb)")
    print("=" * 70)

    print("  Connecting to Yahoo Finance ...")
    session, crumb = get_session_and_crumb()
    print()

    for i, ticker in enumerate(ALL_STOCKS, 1):
        print(f"  [{i:3}/{total}] {ticker:<8} ...", end=" ", flush=True)
        d = fetch_data(session, crumb, ticker)

        if d is None:
            print("ERROR")
        else:
            peg = d["peg"]
            fpe = d["fwd_pe"]
            rg  = d["rev_growth"]
            mc  = d["mkt_cap"]

            peg_s = f"PEG={peg:.2f}"  if peg is not None else "PEG=N/A"
            fpe_s = f"PE={fpe:.1f}"   if fpe is not None else "PE=N/A"
            rg_s  = f"RG={rg*100:.0f}%" if rg is not None else "RG=N/A"
            mc_s  = fmt_cap(mc)

            status = "  ✓ PASS" if passes_all(d) else ""
            print(f"{peg_s}  {fpe_s}  {rg_s}  {mc_s}{status}")

            all_rows.append(d)
            if passes_all(d):
                pass_rows.append(d)

        time.sleep(0.5 + random.uniform(0, 0.3))

    # ── Save CSVs ─────────────────────────────────────────────────────────────
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    out_dir = os.path.dirname(os.path.abspath(__file__))

    all_path  = os.path.join(out_dir, f"screener_all_{ts}.csv")
    pass_path = os.path.join(out_dir, f"screener_pass_{ts}.csv")

    save_csv(all_rows,  all_path)
    save_csv(pass_rows, pass_path)

    # ── Print results ─────────────────────────────────────────────────────────
    pass_rows.sort(key=lambda x: x["peg"])

    print()
    print("=" * 70)
    print(f"  RESULTS  --  All filters passed  ({len(pass_rows)} stocks)")
    print(f"  {'Ticker':<8}  {'PEG':>5}  {'FwdPE':>7}  {'RevGrowth':>10}  {'MktCap':>10}")
    print("-" * 70)
    for d in pass_rows:
        rg_pct = f"{d['rev_growth']*100:.0f}%" if d["rev_growth"] is not None else "N/A"
        print(
            f"  {d['ticker']:<8}  "
            f"{d['peg']:>5.2f}  "
            f"{d['fwd_pe']:>7.1f}  "
            f"{rg_pct:>10}  "
            f"{fmt_cap(d['mkt_cap']):>10}"
        )
    print("=" * 70)
    print(f"\n  Saved: {pass_path}")
    print(f"  Saved: {all_path}")


if __name__ == "__main__":
    main()
