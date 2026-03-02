import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "db" / "strategies.db"

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER PRIMARY KEY,
    strategy_name TEXT UNIQUE,
    source_file TEXT,
    logic_hash TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS backtest_results (
    id INTEGER PRIMARY KEY,
    strategy_id INTEGER,
    run_timestamp TEXT,
    timeframe TEXT,
    symbol TEXT,
    total_trades INTEGER,
    win_rate REAL,
    total_return REAL,
    max_dd REAL,
    profit_factor REAL,
    status TEXT,
    composite_score REAL,
    FOREIGN KEY(strategy_id) REFERENCES strategies(id)
);
"""

def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
        print("OK DB:", DB_PATH)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
