import os, subprocess, ollama
from dotenv import dotenv_values

BASE     = os.path.join(os.path.expanduser("~"), "qwen-dev")
ENV      = dotenv_values(os.path.join(BASE, ".env"))
TOKEN    = ENV["GITHUB_TOKEN"]
USERNAME = ENV["GITHUB_USERNAME"]
SOURCE   = ENV["SOURCE_REPO"]
MODEL    = ENV["MODEL"]

RAW_DIR  = os.path.join(BASE, "Future-Trading", "1_raw")
OUT_DIR  = os.path.join(BASE, "Future-Trading", "2_translated")
CLONE_DIR= os.path.join(BASE, "Trading-Strategies")

def clone_source():
    url = f"https://{TOKEN}@github.com/{USERNAME}/Trading-Strategies.git"
    if os.path.exists(CLONE_DIR):
        print("Pulling latest source...")
        subprocess.run(["git","-C",CLONE_DIR,"pull"], check=True)
    else:
        print("Cloning source repo...")
        subprocess.run(["git","clone",url,CLONE_DIR], check=True)

def translate_all():
    src = os.path.join(CLONE_DIR,"fmz-source")
    os.makedirs(OUT_DIR, exist_ok=True)
    files = [f for f in os.listdir(src) if f.endswith(".md")]
    total = len(files)
    print(f"Found {total} files to translate.")
    for i,fn in enumerate(files,1):
        out = os.path.join(OUT_DIR,fn)
        if os.path.exists(out):
            print(f"[{i}/{total}] Skip: {fn[:50]}")
            continue
        try:
            with open(os.path.join(src,fn),"r",encoding="utf-8") as fp:
                content = fp.read()
            r = ollama.chat(model=MODEL, messages=[
                {"role":"system","content":"Translate Chinese trading strategy to English. Keep Pine Script code blocks EXACTLY unchanged. Only translate Chinese text."},
                {"role":"user","content":content}
            ])
            with open(out,"w",encoding="utf-8") as fp:
                fp.write(r["message"]["content"])
            print(f"[{i}/{total}] Done: {fn[:50]}")
        except Exception as e:
            print(f"[{i}/{total}] ERROR {fn[:50]}: {e}")
    print("Translation complete.")

if __name__=="__main__":
    clone_source()
    translate_all()
