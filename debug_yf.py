"""Run this and paste the full output so we can diagnose the N/A issue."""
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

print("=== STEP 1: Visit finance.yahoo.com ===")
r1 = session.get("https://finance.yahoo.com", timeout=15)
print(f"Status : {r1.status_code}")
print(f"Cookies: {list(session.cookies.keys())}")

print("\n=== STEP 2: Get crumb ===")
r2 = session.get("https://query2.finance.yahoo.com/v1/test/getcrumb", timeout=15)
print(f"Status : {r2.status_code}")
print(f"Body   : {r2.text[:300]}")

crumb = r2.text.strip()

print("\n=== STEP 3: Fetch AAPL defaultKeyStatistics ===")
url = (
    "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
    f"AAPL?modules=defaultKeyStatistics&crumb={crumb}"
)
r3 = session.get(url, timeout=15)
print(f"Status : {r3.status_code}")
print(f"Body   : {r3.text[:800]}")

print("\n=== STEP 4: Try v7 quote endpoint (no crumb needed) ===")
r4 = session.get(
    "https://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL",
    timeout=15,
)
print(f"Status : {r4.status_code}")
print(f"Body   : {r4.text[:800]}")
