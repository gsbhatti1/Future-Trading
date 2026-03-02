import os, time, base64, json, importlib.util, requests

#  Load config 
def load_config():
    spec = importlib.util.spec_from_file_location("config",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "0_config.py"))
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)
    return cfg

def load_secrets():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "0_secrets.py")
    spec = importlib.util.spec_from_file_location("secrets", p)
    sec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sec)
    return sec

cfg     = load_config()
secrets = load_secrets()

GITHUB_TOKEN = secrets.GITHUB_TOKEN
HEADERS      = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
OUT_DIR      = cfg.TRANSLATED_DIR
os.makedirs(OUT_DIR, exist_ok=True)

#  Search queries - Chinese, Korean, Indian, global quant repos 
QUERIES = [
    "trading strategy pine script stars:>50",
    "quantitative trading strategy python stars:>50",
    "backtest trading strategy win rate python stars:>30",
    "BTC ETH trading bot strategy python stars:>30",
    "crypto trading strategy EMA RSI MACD python stars:>20",
    # Chinese
    " python stars:>20",
    " pine script stars:>10",
    " backtest BTC ETH stars:>10",
    # Korean
    "  python stars:>10",
    "  stars:>10",
    # Indian
    "algorithmic trading strategy python india stars:>20",
    "algo trading crypto python stars:>30",
]

CRYPTO_KEYWORDS = ["btc","eth","sol","crypto","usdt","binance","bybit","blofin",
                   "bitcoin","ethereum","solana","futures","perpetual"]
STRATEGY_KEYWORDS = ["strategy","signal","entry","exit","backtest","win_rate",
                     "winrate","long","short","ema","rsi","macd","bollinger"]

downloaded = set()
stats = {"repos_found": 0, "files_downloaded": 0, "skipped": 0}

def search_repos(query, page=1):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": 30, "page": page}
    r = requests.get(url, headers=HEADERS, params=params, timeout=15)
    if r.status_code == 200:
        return r.json().get("items", [])
    if r.status_code == 403:
        print("  Rate limited - sleeping 60s...")
        time.sleep(60)
    return []

def get_repo_files(owner, repo, path="", depth=0):
    if depth > 3:
        return []
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return []
    files = []
    for item in r.json():
        if item["type"] == "file":
            name = item["name"].lower()
            if name.endswith(".pine") or (name.endswith(".py") and
               any(k in name for k in ["strat","signal","backtest","trade","bot","algo"])):
                files.append(item)
        elif item["type"] == "dir" and depth < 2:
            subdir = item["name"].lower()
            if any(k in subdir for k in ["strat","signal","trade","bot","algo","backtest","script"]):
                files.extend(get_repo_files(owner, repo, item["path"], depth+1))
    return files

def is_relevant(content_str):
    low = content_str.lower()
    has_crypto   = any(k in low for k in CRYPTO_KEYWORDS)
    has_strategy = sum(1 for k in STRATEGY_KEYWORDS if k in low)
    return has_strategy >= 3

def download_file(item, repo_name, owner):
    fname_key = f"{owner}_{repo_name}_{item['name']}"
    if fname_key in downloaded:
        stats["skipped"] += 1
        return
    r = requests.get(item["download_url"], headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return
    content = r.text
    if not is_relevant(content):
        stats["skipped"] += 1
        return
    safe_name = fname_key.replace("/","_").replace(" ","_")[:120]
    ext = ".pine" if item["name"].endswith(".pine") else ".py"
    out_path = os.path.join(OUT_DIR, safe_name if safe_name.endswith(ext) else safe_name + ext)
    with open(out_path, "w", encoding="utf-8", errors="replace") as f:
        f.write(f"# SOURCE: https://github.com/{owner}/{repo_name}\n")
        f.write(f"# FILE  : {item['name']}\n\n")
        f.write(content)
    downloaded.add(fname_key)
    stats["files_downloaded"] += 1
    print(f"  SAVED: {safe_name[:80]}")

print("=" * 60)
print("PHANTOMFLIP STRATEGY HARVESTER")
print(f"Output: {OUT_DIR}")
print("=" * 60)

seen_repos = set()
for query in QUERIES:
    print(f"\nSearching: {query[:60]}")
    for page in [1, 2]:
        repos = search_repos(query, page)
        for repo in repos:
            key = repo["full_name"]
            if key in seen_repos:
                continue
            seen_repos.add(key)
            stats["repos_found"] += 1
            owner, rname = repo["owner"]["login"], repo["name"]
            stars = repo["stargazers_count"]
            print(f"  [{stars}*] {key}")
            files = get_repo_files(owner, rname)
            for f in files:
                download_file(f, rname, owner)
                time.sleep(0.3)
        time.sleep(2)
    time.sleep(3)

print("\n" + "=" * 60)
print(f"DONE!")
print(f"  Repos scanned   : {stats['repos_found']}")
print(f"  Files downloaded: {stats['files_downloaded']}")
print(f"  Skipped (low relevance): {stats['skipped']}")
print(f"\nNext step: run python 1_translate.py")
print("=" * 60)