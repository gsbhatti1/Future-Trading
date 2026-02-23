import os
import re
import subprocess
import ollama

FMZQUANT_REPO = "https://github.com/fmzquant/strategies.git"
SOURCE_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Trading-Strategies", "fmz-source")
OUT_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Future-Trading", "2_translated")
REPO_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Future-Trading")

AUTO_PUSH_EVERY = 10

os.makedirs(OUT_DIR, exist_ok=True)

# Step 1: Clone fmzquant/strategies if not already cloned
if not os.path.exists(SOURCE_DIR):
    print("[CLONE] Cloning fmzquant/strategies...")
    os.makedirs(SOURCE_DIR, exist_ok=True)
    subprocess.run(["git", "clone", FMZQUANT_REPO, SOURCE_DIR], check=True)
else:
    print("[CLONE] Already cloned, skipping.")

# Step 2: Find all .md files to translate
all_files = []
for root, dirs, files in os.walk(SOURCE_DIR):
    for f in files:
        if f.endswith(".md"):
            all_files.append(os.path.join(root, f))

total = len(all_files)
print(f"[INFO] Found {total} .md files to translate.")

# Helper: strip Chinese characters from a string
def strip_chinese(text):
    parts = re.split(r'[\u4e00-\u9fff]+', text)
    english_parts = [p.strip('-').strip() for p in parts if p.strip('-').strip()]
    if english_parts:
        result = '-'.join(english_parts)
        result = re.sub(r'-+', '-', result).strip('-')
        return result
    return text

# Build a set of all existing filenames in OUT_DIR (both original and renamed)
# This catches files whether they were renamed to English or kept original
already_done = set()
for root, dirs, files in os.walk(OUT_DIR):
    for f in files:
        if f.endswith(".md"):
            already_done.add(f.lower())
            # Also add the English-stripped version so we match source filenames
            stripped = strip_chinese(f[:-3]).lower() + ".md"
            already_done.add(stripped)

print(f"[INFO] Already translated: {len(already_done)//2} files (will skip these)")

# Auto-push helper
def git_push(label="auto"):
    try:
        subprocess.run(["git", "-C", REPO_DIR, "pull", "--rebase"], check=True)
        subprocess.run(["git", "-C", REPO_DIR, "add", "2_translated/"], check=True)
        result = subprocess.run(
            ["git", "-C", REPO_DIR, "diff", "--cached", "--quiet"]
        )
        if result.returncode != 0:
            subprocess.run(
                ["git", "-C", REPO_DIR, "commit", "-m", f"Auto-save translation progress ({label})"],
                check=True
            )
            subprocess.run(["git", "-C", REPO_DIR, "push"], check=True)
            print(f"[PUSH] Pushed to GitHub ({label})")
        else:
            print(f"[PUSH] Nothing new to push ({label})")
    except Exception as e:
        print(f"[PUSH ERROR] {e}")

# Step 3: Translate each file
translated_count = 0

for i, filepath in enumerate(all_files):
    rel_path = os.path.relpath(filepath, SOURCE_DIR)
    fname = os.path.basename(filepath)
    out_path = os.path.join(OUT_DIR, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Check by exact filename AND english-stripped version
    fname_lower = fname.lower()
    fname_stripped = strip_chinese(fname[:-3]).lower() + ".md"

    if fname_lower in already_done or fname_stripped in already_done or os.path.exists(out_path):
        print(f"[SKIP] [{i+1}/{total}] {fname}")
        continue

    print(f"[TRANSLATING] [{i+1}/{total}] {fname}")
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if len(content.strip()) == 0:
            print(f"[EMPTY] Skipping empty file.")
            already_done.add(fname_lower)
            continue

        response = ollama.chat(
            model="qwen2.5:7b",
            messages=[{
                "role": "user",
                "content": f"Translate the following trading strategy document from Chinese to English. Keep all code blocks, numbers, and formatting exactly as-is. Only translate the human-readable text.\n\n{content[:6000]}"
            }]
        )
        translated = response["message"]["content"]
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(translated)

        already_done.add(fname_lower)
        already_done.add(fname_stripped)
        translated_count += 1

        if translated_count % AUTO_PUSH_EVERY == 0:
            git_push(f"{i+1}/{total}")

    except Exception as e:
        print(f"[ERROR] {e}")
        continue

git_push("final")
print(f"[DONE] All files processed. Newly translated: {translated_count}")
