import os
import subprocess
import ollama

FMZQUANT_REPO = "https://github.com/fmzquant/strategies.git"
SOURCE_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Trading-Strategies", "fmz-source")
OUT_DIR = os.path.join(os.path.expanduser("~"), "qwen-dev", "Future-Trading", "2_translated")

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

# Step 3: Translate each file using Ollama Qwen
for i, filepath in enumerate(all_files):
    rel_path = os.path.relpath(filepath, SOURCE_DIR)
    out_path = os.path.join(OUT_DIR, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Skip already translated
    if os.path.exists(out_path):
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

    except Exception as e:
        print(f"[ERROR] {e}")
        continue

print("[DONE] All files processed.")
