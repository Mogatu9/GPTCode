"""
Stock list compiled from multiple prestigious investment and technology research sources.
Updated: 2026
"""

# ── Analyst Conviction & Focus Lists ─────────────────────────────────────────

# IBD Tech Leaders / IBD 50 (Investor's Business Daily)
# Source: SwingTradeBot IBD tags, IBD Leaderboard — updated 2025/2026
ibd_tech_leaders = [
    "PLTR",   # Palantir Technologies
    "NVDA",   # NVIDIA
    "CRDO",   # Credo Technology
    "SOUN",   # SoundHound AI
    "RKLB",   # Rocket Lab USA
    "MU",     # Micron Technology
    "HOOD",   # Robinhood Markets
    "INOD",   # Innodata
    "CLS",    # Celestica
    "RMBS",   # Rambus
    "FIX",    # Comfort Systems USA
    "AMSC",   # American Superconductor
    "APP",    # AppLovin
    "ANET",   # Arista Networks
    "AVGO",   # Broadcom
    "ARM",    # ARM Holdings
    "SMCI",   # Super Micro Computer
    "CRWD",   # CrowdStrike
    "FTNT",   # Fortinet
    "PANW",   # Palo Alto Networks
]

# Bank of America US 1 List — Q1 2026
# Source: CNBC / BofA Global Research (Dec 2025 – Q1 2026)
bofa_us1 = [
    "AMZN",   # Amazon
    "BA",     # Boeing
    "CI",     # Cigna
    "CEG",    # Constellation Energy
    "DG",     # Dollar General
    "EQIX",   # Equinix
    "MRK",    # Merck
    "SPOT",   # Spotify
    "VRTX",   # Vertex Pharmaceuticals
    "MSFT",   # Microsoft
    "LLY",    # Eli Lilly
    "NVDA",   # NVIDIA
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "AAPL",   # Apple
    "JPM",    # JPMorgan Chase
    "V",      # Visa
    "MA",     # Mastercard
    "UNH",    # UnitedHealth
    "CAT",    # Caterpillar
    "GS",     # Goldman Sachs
    "HD",     # Home Depot
]

# JP Morgan Analyst Focus List — 2026
# Source: CNBC / JPMorgan Research (Dec 2025)
jpmorgan_focus = [
    "GOOGL",  # Alphabet
    "AMZN",   # Amazon
    "DASH",   # DoorDash
    "AVGO",   # Broadcom
    "MU",     # Micron Technology
    "MRVL",   # Marvell Technology
    "ADI",    # Analog Devices
    "GEV",    # GE Vernova
    "BFAM",   # Bright Horizons Family Solutions
    "CELH",   # Celsius Holdings
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "META",   # Meta Platforms
    "AAPL",   # Apple
    "NOW",    # ServiceNow
    "CRM",    # Salesforce
    "UBER",   # Uber
    "ABNB",   # Airbnb
    "LLY",    # Eli Lilly
    "TSM",    # TSMC
    "ANET",   # Arista Networks
]

# Morgan Stanley Top Picks — 2026
# Source: CNBC / Morgan Stanley Research (Dec 2025 – Apr 2026)
morgan_stanley_top_picks = [
    "NVDA",   # NVIDIA
    "SPOT",   # Spotify
    "PANW",   # Palo Alto Networks
    "WDC",    # Western Digital
    "INTU",   # Intuit
    "EQIX",   # Equinix
    "DKS",    # Dick's Sporting Goods
    "AZO",    # AutoZone
    "W",      # Wayfair
    "MSFT",   # Microsoft
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "GOOGL",  # Alphabet
    "AAPL",   # Apple
    "LLY",    # Eli Lilly
    "UNH",    # UnitedHealth
    "V",      # Visa
    "NOW",    # ServiceNow
]

# Needham Conviction List — 2025/2026
# Source: Yahoo Finance / Investing.com analyst coverage
needham_conviction = [
    "RDDT",   # Reddit
    "SIBN",   # SI-Bone
    "ALC",    # Alcon
    "ROKU",   # Roku
    "CRM",    # Salesforce
    "MNMD",   # MindMed
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AAPL",   # Apple
    "DDOG",   # Datadog
    "SNOW",   # Snowflake
    "TTD",    # The Trade Desk
    "NOW",    # ServiceNow
]

# Citigroup Catalyst Watch — 2025/2026
# Source: Yahoo Finance / Citi Research analyst notes
citi_catalyst_watch = [
    "AMD",    # Advanced Micro Devices
    "ADI",    # Analog Devices
    "MRVL",   # Marvell Technology
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "GOOGL",  # Alphabet
    "AAPL",   # Apple
    "JPM",    # JPMorgan Chase
    "GS",     # Goldman Sachs
    "LLY",    # Eli Lilly
    "TSM",    # TSMC
    "PANW",   # Palo Alto Networks
]

# Goldman Sachs Conviction / Favorite Retail — 2026
# Source: CNBC / Goldman Sachs Global Investment Research (Dec 2025 – Q1 2026)
goldman_sachs_conviction = [
    "DKS",    # Dick's Sporting Goods
    "BBY",    # Best Buy
    "DRI",    # Darden Restaurants
    "EAT",    # Brinker International
    "GAP",    # Gap Inc.
    "SBUX",   # Starbucks
    "ROST",   # Ross Stores
    "TJX",    # TJX Companies
    "ULTA",   # Ulta Beauty
    "BURL",   # Burlington Coat Factory
    "AMZN",   # Amazon
    "COST",   # Costco
    "WMT",    # Walmart
    "HD",     # Home Depot
    "LOW",    # Lowe's
    "TGT",    # Target
    "LULU",   # Lululemon Athletica
    "NKE",    # Nike
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "LLY",    # Eli Lilly
    "V",      # Visa
    "MA",     # Mastercard
]

# ── Technology Research & Analyst Reports ────────────────────────────────────

# Gartner Magic Quadrant Leaders — 2025/2026 (multiple categories)
# Source: IBM, Microsoft, AWS, Salesforce/Informatica press releases
gartner_magic_quadrant = [
    "AMZN",   # Amazon (AWS) — Cloud Platform leader 15 consecutive years
    "MSFT",   # Microsoft — Cloud, Integration Platform, Data Fabric
    "IBM",    # IBM — 7 AI-related MQ leader positions
    "GOOGL",  # Alphabet (Google Cloud) — Cloud, AI
    "CRM",    # Salesforce/Informatica — Data Quality, MDM
    "ACN",    # Accenture — Digital Technology & Business Consulting
    "NOW",    # ServiceNow — Workflow Automation
    "WDAY",   # Workday — HCM, Finance
    "PANW",   # Palo Alto Networks — Cybersecurity
    "CRWD",   # CrowdStrike — Endpoint Security
    "ZS",     # Zscaler — Zero Trust Networking
    "OKTA",   # Okta — Identity & Access Management
    "VEEV",   # Veeva Systems — Life Sciences CRM
    "DDOG",   # Datadog — Observability
    "SNOW",   # Snowflake — Data Cloud
    "ORCL",   # Oracle — Cloud ERP, Database
    "SAP",    # SAP SE — ERP
    "MDB",    # MongoDB — Database Platforms
    "NET",    # Cloudflare — SASE, Network Security
    "HUBS",   # HubSpot — CRM, Marketing
]

# Forrester Wave Leaders — 2025/2026 (multiple categories)
# Source: Google Cloud, Microsoft, Atlassian, Wiz press releases
forrester_wave = [
    "GOOGL",  # Alphabet — AI Infrastructure Solutions (Q4 2025)
    "MSFT",   # Microsoft — Data Fabric Platforms (Q4 2025), Digital Experience
    "TEAM",   # Atlassian — DevOps Platforms (Q2 2025)
    "IBM",    # IBM — Data, AI Platforms
    "ADBE",   # Adobe — Digital Experience Platforms
    "CRM",    # Salesforce — CRM, Marketing Cloud
    "ORCL",   # Oracle — Database, Cloud
    "SAP",    # SAP — ERP
    "ZS",     # Zscaler — Zero Trust
    "PANW",   # Palo Alto Networks — Cybersecurity
    "AMZN",   # Amazon — Cloud Infrastructure
    "SNOW",   # Snowflake — Data Platforms
]

# IDC MarketScape Leaders — 2025/2026
idc_marketscape = [
    "MSFT",   # Microsoft
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "IBM",    # IBM
    "ORCL",   # Oracle
    "HPE",    # Hewlett Packard Enterprise
    "DELL",   # Dell Technologies
    "CRM",    # Salesforce
    "NOW",    # ServiceNow
    "CSCO",   # Cisco Systems
    "SAP",    # SAP SE
    "WDAY",   # Workday
]

# Deloitte Annual Tech Trends Report — 2025/2026
deloitte_tech_trends = [
    "MSFT",   # Microsoft
    "GOOGL",  # Alphabet
    "AMZN",   # Amazon
    "IBM",    # IBM
    "ORCL",   # Oracle
    "SAP",    # SAP SE
    "CRM",    # Salesforce
    "NOW",    # ServiceNow
    "SNOW",   # Snowflake
    "DDOG",   # Datadog
    "NVDA",   # NVIDIA
    "PLTR",   # Palantir
    "INTC",   # Intel
    "AMD",    # AMD
    "QCOM",   # Qualcomm
]

# ── Innovation & Industry Awards ─────────────────────────────────────────────

# CES Innovation Awards — 2025/2026
# Source: CES.tech / CTA, Morningstar/BusinessWire (Dec 2025)
ces_innovation_awards = [
    "OSK",    # Oshkosh Corporation — Best of Innovation, Robotics (JLG Boom Lift)
    "SSNLF",  # Samsung Electronics (OTC) — Multiple awards incl. Galaxy XR, Z Fold 7
    "NVDA",   # NVIDIA — AI/GPU platforms
    "QCOM",   # Qualcomm — AI on-device chips
    "AMD",    # AMD — AI processor innovations
    "MSFT",   # Microsoft — AI PCs
    "AAPL",   # Apple — Wearables, Vision Pro ecosystem
    "SONY",   # Sony Group (ADR) — XR, Gaming innovations
    "SNE",    # Sony (NYSE ADR)
    "INTC",   # Intel — AI PC platforms
    "LG",     # LG Electronics (OTC: LGELY)
]

# CRN Top 100 Coolest Cloud Computing Companies — 2022/2025
# Source: CRN.com
crn_top_100 = [
    "MSFT",   # Microsoft (Azure)
    "AMZN",   # Amazon (AWS)
    "GOOGL",  # Alphabet (Google Cloud)
    "IBM",    # IBM Cloud
    "ORCL",   # Oracle Cloud
    "CRM",    # Salesforce
    "NOW",    # ServiceNow
    "WDAY",   # Workday
    "SNOW",   # Snowflake
    "DDOG",   # Datadog
    "NET",    # Cloudflare
    "ZS",     # Zscaler
    "PANW",   # Palo Alto Networks
    "CRWD",   # CrowdStrike
    "OKTA",   # Okta
    "MDB",    # MongoDB
    "HUBS",   # HubSpot
    "TWLO",   # Twilio
    "DOCN",   # DigitalOcean
    "ESTC",   # Elastic
    "HPE",    # Hewlett Packard Enterprise
    "DELL",   # Dell Technologies
    "CSCO",   # Cisco
    "TEAM",   # Atlassian
    "VEEV",   # Veeva Systems
    "ANET",   # Arista Networks
    "PSTG",   # Pure Storage
    "VRNT",   # Verint Systems
    "FIVN",   # Five9
    "RNG",    # RingCentral
]

# MMI / Barron's Industry Awards — 2025/2026
mmi_barrons_awards = [
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AAPL",   # Apple
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "TSLA",   # Tesla
    "V",      # Visa
    "MA",     # Mastercard
    "BRK.B",  # Berkshire Hathaway
    "JPM",    # JPMorgan Chase
    "UNH",    # UnitedHealth
    "LLY",    # Eli Lilly
    "COST",   # Costco
    "HD",     # Home Depot
]

# ── Business Publication Lists ────────────────────────────────────────────────

# Barron's Conviction List — 2025/2026
barrons_conviction = [
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AAPL",   # Apple
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "BRK.B",  # Berkshire Hathaway
    "JPM",    # JPMorgan Chase
    "V",      # Visa
    "MA",     # Mastercard
    "UNH",    # UnitedHealth
    "LLY",    # Eli Lilly
    "COST",   # Costco
    "AVGO",   # Broadcom
    "NOW",    # ServiceNow
    "CEG",    # Constellation Energy
    "EQIX",   # Equinix
    "VRTX",   # Vertex Pharmaceuticals
    "GEV",    # GE Vernova
]

# Bloomberg BI 50 — Most Innovative Companies 2025/2026
bloomberg_bi50 = [
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "GOOGL",  # Alphabet
    "AAPL",   # Apple
    "TSLA",   # Tesla
    "LLY",    # Eli Lilly
    "JPM",    # JPMorgan Chase
    "V",      # Visa
    "MA",     # Mastercard
    "UNH",    # UnitedHealth
    "NOW",    # ServiceNow
    "CRM",    # Salesforce
    "AVGO",   # Broadcom
    "SPOT",   # Spotify
    "PLTR",   # Palantir
    "ARM",    # ARM Holdings
    "TSM",    # TSMC
    "PANW",   # Palo Alto Networks
]

# Fast Company — Brands That Matter 2025
fast_company_brands = [
    "AAPL",   # Apple
    "NVDA",   # NVIDIA
    "TSLA",   # Tesla
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "MSFT",   # Microsoft
    "SBUX",   # Starbucks
    "NKE",    # Nike
    "DIS",    # Disney
    "SPOT",   # Spotify
    "UBER",   # Uber
    "ABNB",   # Airbnb
    "HOOD",   # Robinhood
    "PLTR",   # Palantir
]

# Fast Money Most Innovative Companies — 2025/2026
fast_money_innovative = [
    "NVDA",   # NVIDIA
    "TSLA",   # Tesla
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "MSFT",   # Microsoft
    "AAPL",   # Apple
    "PLTR",   # Palantir
    "SOUN",   # SoundHound AI
    "APP",    # AppLovin
    "RDDT",   # Reddit
    "ARM",    # ARM Holdings
    "AVGO",   # Broadcom
    "AMD",    # AMD
    "IONQ",   # IonQ
]

# Harvard Business Review — Best Performing CEOs 2025
# Source: HBR CEO rankings (biennial/annual list)
hbr_best_ceos = [
    "AAPL",   # Apple (Tim Cook)
    "MSFT",   # Microsoft (Satya Nadella)
    "NVDA",   # NVIDIA (Jensen Huang)
    "AMZN",   # Amazon (Andy Jassy)
    "META",   # Meta (Mark Zuckerberg)
    "GOOGL",  # Alphabet (Sundar Pichai)
    "TSLA",   # Tesla (Elon Musk)
    "JPM",    # JPMorgan (Jamie Dimon)
    "BRK.B",  # Berkshire Hathaway (Warren Buffett)
    "LLY",    # Eli Lilly (David Ricks)
    "COST",   # Costco (Ron Vachris)
    "V",      # Visa (Ryan McInerney)
    "MA",     # Mastercard (Michael Miebach)
    "NOW",    # ServiceNow (Bill McDermott)
    "CRM",    # Salesforce (Marc Benioff)
]

# Times Best Companies for Future Leaders — 2025
# Source: TIME / Statista Best Companies for Future Leaders
time_future_leaders = [
    "MSFT",   # Microsoft
    "GOOGL",  # Alphabet
    "AMZN",   # Amazon
    "AAPL",   # Apple
    "META",   # Meta Platforms
    "NVDA",   # NVIDIA
    "IBM",    # IBM
    "INTC",   # Intel
    "CRM",    # Salesforce
    "ADBE",   # Adobe
    "JPM",    # JPMorgan Chase
    "GS",     # Goldman Sachs
    "BAC",    # Bank of America
    "ACN",    # Accenture
    "CSCO",   # Cisco
    "ORCL",   # Oracle
    "QCOM",   # Qualcomm
    "TXN",    # Texas Instruments
]

# EY Top Entrepreneurs — 2025 (Entrepreneur of the Year)
# Source: EY Entrepreneur of the Year program
ey_top_entrepreneurs = [
    "NVDA",   # NVIDIA (Jensen Huang)
    "TSLA",   # Tesla (Elon Musk)
    "CRM",    # Salesforce (Marc Benioff)
    "PLTR",   # Palantir (Alex Karp)
    "AMZN",   # Amazon (Andy Jassy)
    "META",   # Meta (Mark Zuckerberg)
    "GOOGL",  # Alphabet (Sundar Pichai)
    "SPOT",   # Spotify (Daniel Ek)
    "ABNB",   # Airbnb (Brian Chesky)
    "UBER",   # Uber (Dara Khosrowshahi)
    "RDDT",   # Reddit (Steve Huffman)
    "HOOD",   # Robinhood (Vlad Tenev)
]

# ── Portfolio & Research Services ─────────────────────────────────────────────

# Morningstar Wide Moat Focus Index — 2025/2026 reconstitution
# Source: Morningstar Indexes, VanEck MOAT ETF
morningstar_wide_moat = [
    "AAPL",   # Apple
    "MSFT",   # Microsoft
    "GOOGL",  # Alphabet
    "AMZN",   # Amazon
    "V",      # Visa
    "MA",     # Mastercard
    "BRK.B",  # Berkshire Hathaway
    "JNJ",    # Johnson & Johnson
    "PG",     # Procter & Gamble
    "KO",     # Coca-Cola
    "UNH",    # UnitedHealth
    "ADBE",   # Adobe
    "INTU",   # Intuit
    "MELI",   # MercadoLibre
    "NKE",    # Nike
    "STZ",    # Constellation Brands
    "TRU",    # TransUnion
    "BIIB",   # Biogen
    "GILD",   # Gilead Sciences
    "BMY",    # Bristol-Myers Squibb
]

# Trefis High Quality (HQ) Portfolio — 2025/2026
# Source: Trefis.com portfolio holdings
trefis_hq = [
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AAPL",   # Apple
    "AMZN",   # Amazon
    "GOOGL",  # Alphabet
    "META",   # Meta Platforms
    "TSLA",   # Tesla
    "V",      # Visa
    "MA",     # Mastercard
    "UNH",    # UnitedHealth
    "LLY",    # Eli Lilly
    "AVGO",   # Broadcom
    "NOW",    # ServiceNow
    "ISRG",   # Intuitive Surgical
    "COST",   # Costco
]

# Benzinga Edge — Top Analyst Consensus Picks 2025/2026
benzinga_edge = [
    "NVDA",   # NVIDIA
    "MSFT",   # Microsoft
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "GOOGL",  # Alphabet
    "AAPL",   # Apple
    "AVGO",   # Broadcom
    "LLY",    # Eli Lilly
    "TSM",    # TSMC
    "PLTR",   # Palantir
    "ARM",    # ARM Holdings
    "NOW",    # ServiceNow
    "PANW",   # Palo Alto Networks
    "CRWD",   # CrowdStrike
    "APP",    # AppLovin
    "MRVL",   # Marvell Technology
    "SPOT",   # Spotify
    "RDDT",   # Reddit
]

# TalkingPointz — Unified Communications & Collaboration Leaders
# Source: TalkingPointz.com industry analyst research
talkingpointz = [
    "MSFT",   # Microsoft (Teams)
    "GOOGL",  # Alphabet (Google Meet/Workspace)
    "AMZN",   # Amazon (Chime, Connect)
    "CSCO",   # Cisco (Webex)
    "ZM",     # Zoom Video Communications
    "RNG",    # RingCentral
    "FIVN",   # Five9
    "NICE",   # NICE Systems (ADR)
    "EGHT",   # 8x8
]

# MarketWatch Best New Ideas in Money / Ray Dalio Outlook 2025/2026
# Source: MarketWatch Festival, Bridgewater macro themes
market_watch_dalio = [
    "GLD",    # SPDR Gold Shares (Gold ETF — Dalio macro hedge)
    "IAU",    # iShares Gold Trust
    "BRK.B",  # Berkshire Hathaway
    "JPM",    # JPMorgan Chase
    "BAC",    # Bank of America
    "WMT",    # Walmart
    "COST",   # Costco
    "XOM",    # ExxonMobil
    "CVX",    # Chevron
    "NEE",    # NextEra Energy
    "CEG",    # Constellation Energy
    "GEV",    # GE Vernova
]

# ── Master Combined List ──────────────────────────────────────────────────────

all_sources = (
    ibd_tech_leaders
    + bofa_us1
    + jpmorgan_focus
    + morgan_stanley_top_picks
    + needham_conviction
    + citi_catalyst_watch
    + goldman_sachs_conviction
    + gartner_magic_quadrant
    + forrester_wave
    + idc_marketscape
    + deloitte_tech_trends
    + ces_innovation_awards
    + crn_top_100
    + mmi_barrons_awards
    + barrons_conviction
    + bloomberg_bi50
    + fast_company_brands
    + fast_money_innovative
    + hbr_best_ceos
    + time_future_leaders
    + ey_top_entrepreneurs
    + morningstar_wide_moat
    + trefis_hq
    + benzinga_edge
    + talkingpointz
    + market_watch_dalio
)

# Deduplicated, sorted master list of US-listed stock tickers
all_stocks = sorted(set(all_sources))

if __name__ == "__main__":
    print(f"Total unique tickers: {len(all_stocks)}")
    print(all_stocks)
