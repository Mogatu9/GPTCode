"""
PEG Screener  --  threshold < 2.0
Uses requests only (no yfinance / pandas / numpy) -- works on Android.
"""

import time
import random
import json

try:
    import requests
except ImportError:
    raise SystemExit("Install requests:  pip install requests")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

PEG_THRESHOLD = 2.0
MAX_RETRIES = 4
BASE_DELAY = 2.0

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


def fetch_peg(ticker: str):
    url = (
        "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
        f"{ticker}?modules=defaultKeyStatistics"
    )
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=12)
            data = r.json()
            stats = (
                data.get("quoteSummary", {})
                    .get("result", [{}])[0]
                    .get("defaultKeyStatistics", {})
            )
            peg = stats.get("pegRatio", {}).get("raw")
            return float(peg) if peg is not None else None
        except Exception:
            if attempt == MAX_RETRIES:
                return None
            delay = BASE_DELAY * (2 ** (attempt - 1)) + random.uniform(0, 1)
            time.sleep(delay)
    return None


def main():
    total = len(ALL_STOCKS)
    results = []

    print("=" * 66)
    print(f"  PEG SCREENER  --  threshold < {PEG_THRESHOLD}")
    print(f"  {total} tickers  |  source: Yahoo Finance (requests only)")
    print("=" * 66)

    for i, ticker in enumerate(ALL_STOCKS, 1):
        print(f"  [{i:3}/{total}] {ticker:<8} ...", end=" ", flush=True)
        peg = fetch_peg(ticker)

        if peg is None:
            print("PEG=N/A")
        else:
            print(f"PEG={peg:.2f}", end="")
            if peg < PEG_THRESHOLD:
                print("  PASS")
                results.append((ticker, peg))
            else:
                print()

        time.sleep(0.6 + random.uniform(0, 0.4))

    print()
    print("=" * 66)
    print(f"  RESULTS  --  PEG < {PEG_THRESHOLD}  ({len(results)} stocks)")
    print("=" * 66)
    for ticker, peg in sorted(results, key=lambda x: x[1]):
        print(f"  {ticker:<8}  PEG = {peg:.2f}")


if __name__ == "__main__":
    main()
