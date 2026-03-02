import os, importlib.util
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font, Alignment

def load_config():
    spec = importlib.util.spec_from_file_location("config",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "0_config.py"))
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)
    return cfg

cfg = load_config()
COLORS = {5:"FF00AA00", 4:"FF88CC00", 3:"FFDDAA00", 2:"FFDD6600", 1:"FFCC0000"}
df = pd.read_csv(os.path.join(cfg.RESULTS_DIR, "raw_results.csv"))
pivot = df.pivot_table(index=["strategy","timeframe"], columns="ticker",
    values=["win_rate","stars"], aggfunc="mean").round(2)
pivot.columns = [f"{c[1]}_{c[0]}" for c in pivot.columns]
pivot = pivot.reset_index()
star_cols = [c for c in pivot.columns if c.endswith("_stars")]
pivot["avg_stars"] = pivot[star_cols].mean(axis=1).round(1)
pivot["bot_ready"] = pivot["avg_stars"].apply(lambda x: "YES" if x >= cfg.BOT_READY_STARS else "NO")
def tag(r):
    tf = str(r["timeframe"]).strip()

    # Classify purely by timeframe (style), not by performance
    if tf in ["1m", "3m", "5m"]:
        return "SCALP"
    elif tf in ["15m", "30m", "1h"]:
        return "INTRADAY"
    elif tf in ["4h", "1d", "1w"]:
        return "SWING"
    else:
        return "UNKNOWN"

pivot["trade_type"] = pivot.apply(tag, axis=1)
pivot = pivot.sort_values("avg_stars", ascending=False)
csv_out = os.path.join(cfg.RESULTS_DIR, "master_results.csv")
pivot.to_csv(csv_out, index=False); print(f"Saved: {csv_out}")
xlsx_out = os.path.join(cfg.RESULTS_DIR, "master_results.xlsx")
pivot.to_excel(xlsx_out, index=False)
wb = load_workbook(xlsx_out); ws = wb.active
ac = list(pivot.columns).index("avg_stars") + 1
for row in range(2, ws.max_row+1):
    v = ws.cell(row, ac).value
    if v:
        s = min(5, max(1, round(float(v))))
        ws.cell(row, ac).fill = PatternFill("solid", fgColor=COLORS[s])
for cell in ws[1]: cell.font = Font(bold=True); cell.alignment = Alignment(horizontal="center")
wb.save(xlsx_out); print(f"Saved: {xlsx_out}")
bot = pivot[pivot["bot_ready"]=="YES"]
print(f"\n=== RESULTS ===")
print(f"  Total    : {len(pivot):,}")
print(f"  Bot Ready: {len(bot):,}")
print(f"  SCALP    : {(pivot.trade_type=='SCALP').sum():,}")
print(f"  SWING    : {(pivot.trade_type=='SWING').sum():,}\n")
