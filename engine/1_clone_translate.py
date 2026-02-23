import os
import subprocess
import ollama

FMZQUANT_REPO = "https://github.com/fmzquant/strategies.git"
SOURCE_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Trading-Strategies", "fmz-source")
OUT_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Future-Trading", "2_translated")
REPO_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Future-Trading")

AUTO_PUSH_EVERY = 10  # push to GitHub every N translated files

os.makedirs(OUT_DIR, exist_ok=True)

# Step 1: Clone fmzquant/strategies if not already cloned
if not os.path.exists(SOURCE_DIR):
    print("[CLONE] Cloning fmzquant/strategies...")
    os.makedirs(SOURCE_DIR, exist_ok=True)
    subprocess.run(["git", "clone", FMZQUANT_REPO, SOURCE_DIR], check=True)
else:
    print("[CLONE] Already cloned, skipping.")

# Step 2: Find all .md files
all_files = []
for root, dirs, files in os.walk(SOURCE_DIR):
    for f in files:
        if f.endswith(".md"):
            all_files.append(os.path.join(root, f))

total = len(all_files)
print(f"[INFO] Found {total} .md files to translate.")

# Build a set of already-translated filenames (just the filename, not full path)
# This way even if you run on a different PC, it won't re-translate files
# that were already done and pushed to GitHub
already_done = set()
for root, dirs, files in os.walk(OUT_DIR):
    for f in files:
        if f.endswith(".md"):
            already_done.add(f.lower())  # case-insensitive match

print(f"[INFO] Already translated: {len(already_done)} files (will skip these)")

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

# Step 3: Translate each file using Ollama Qwen
translated_count = 0

for i, filepath in enumerate(all_files):
    rel_path = os.path.relpath(filepath, SOURCE_DIR)
    fname = os.path.basename(filepath)
    out_path = os.path.join(OUT_DIR, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Skip if already translated - checks by filename so works across different PCs
    if fname.lower() in already_done or os.path.exists(out_path):
        print(f"[SKIP] [{i+1}/{total}] {rel_path}")
        continue

    print(f"[TRANSLATING] [{i+1}/{total}] {rel_path}")
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if len(content.strip()) == 0:
            print(f"[EMPTY] Skipping empty file.")
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

        # Add to already_done so we don't re-translate in same session
        already_done.add(fname.lower())
        translated_count += 1

        # Auto-push every N files
        if translated_count % AUTO_PUSH_EVERY == 0:
            git_push(f"{i+1}/{total}")

    except Exception as e:
        print(f"[ERROR] {e}")
        continue

# Final push at the end
git_push("final")
print("[DONE] All files processed.")
