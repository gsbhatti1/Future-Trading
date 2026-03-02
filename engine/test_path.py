from pathlib import Path

def main() -> None:
    here = Path(__file__).resolve().parent
    print("HERE:", here)
    folders = [
        "strategies/staging",
        "strategies/best",
        "strategies/archive/trash",
        "reports",
        "db",
    ]
    for rel in folders:
        p = here / rel
        p.mkdir(parents=True, exist_ok=True)
        print("OK", p)

if __name__ == "__main__":
    main()
