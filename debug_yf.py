"""Diagnose Yahoo Finance PEG data availability."""
import requests, json

session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
})

# Get cookies + crumb
session.get("https://finance.yahoo.com", timeout=15)
crumb = session.get(
    "https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=15
).text.strip()
print(f"Crumb: {crumb}\n")

# Test 3 stocks that usually have PEG ratios
for ticker in ["NVDA", "AAPL", "META"]:
    url = (
        "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
        f"{ticker}?modules=defaultKeyStatistics&crumb={crumb}"
    )
    r = session.get(url, timeout=15)
    data = r.json()
    try:
        stats = data["quoteSummary"]["result"][0]["defaultKeyStatistics"]
        peg   = stats.get("pegRatio", "NOT FOUND")
        fpe   = stats.get("forwardPE", "NOT FOUND")
        print(f"{ticker}  pegRatio={peg}  forwardPE={fpe}")
    except Exception as e:
        print(f"{ticker}  ERROR: {e}")
        print(f"  Raw: {r.text[:300]}")
    import time; time.sleep(0.5)
