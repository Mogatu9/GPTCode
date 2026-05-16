"""
PEG Screener  --  threshold < 2.0
Fetches PEG ratio from Yahoo Finance with retry + exponential backoff.
"""

import time
import random
import yfinance as yf
from stocks import all_stocks

PEG_THRESHOLD = 2.0
MAX_RETRIES = 4
BASE_DELAY = 2.0   # seconds


def fetch_peg(ticker: str) -> float | None:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            info = yf.Ticker(ticker).info
            peg = info.get("pegRatio") or info.get("trailingPegRatio")
            if peg is not None:
                return float(peg)
            # Got a response but PEG genuinely not available
            return None
        except Exception:
            if attempt == MAX_RETRIES:
                return None
            delay = BASE_DELAY * (2 ** (attempt - 1)) + random.uniform(0, 1)
            time.sleep(delay)
    return None


def main():
    tickers = all_stocks
    total = len(tickers)
    results = []

    print("=" * 66)
    print(f"  PEG SCREENER  --  threshold < {PEG_THRESHOLD}")
    print(f"  {total} tickers  |  source: Yahoo Finance")
    print("=" * 66)

    for i, ticker in enumerate(tickers, 1):
        print(f"  [{i:3}/{total}] {ticker:<8} ...", end=" ", flush=True)
        peg = fetch_peg(ticker)

        if peg is None:
            print("PEG=N/A")
        else:
            print(f"PEG={peg:.2f}", end="")
            if peg < PEG_THRESHOLD:
                print("  ✓ PASS")
                results.append((ticker, peg))
            else:
                print()

        # Polite delay between every request to avoid rate limiting
        time.sleep(0.5 + random.uniform(0, 0.3))

    print()
    print("=" * 66)
    print(f"  RESULTS  --  PEG < {PEG_THRESHOLD}  ({len(results)} stocks)")
    print("=" * 66)
    for ticker, peg in sorted(results, key=lambda x: x[1]):
        print(f"  {ticker:<8}  PEG = {peg:.2f}")


if __name__ == "__main__":
    main()
