# ================================================================
# GB AUTO-FINAL: MASTER OPTIMIZER & PINE GENERATOR
# Does EVERYTHING automatically:
# 1. Downloads NAS100 5m data
# 2. Runs 1,296 ORB loops + 900 Pullback loops (2,196 total)
# 3. Finds the Rank #1 winner for each
# 4. Generates two final .pine files with optimized variables
# ================================================================

import subprocess
import os
import json
import time

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
PINE_DIR   = os.path.join(os.path.dirname(ENGINE_DIR), "6_pine_scripts")
RESULTS_DIR = os.path.join(os.path.dirname(ENGINE_DIR), "4_backtest_results")

def run_optimizer(script_name):
    print(f"
[STEP] Running {script_name}...")
    start = time.time()
    subprocess.run(["python", os.path.join(ENGINE_DIR, script_name)], check=True)
    end = time.time()
    print(f"[DONE] {script_name} finished in {round((end-start)/60, 1)} minutes.")

def update_pine_script(template_name, results_file, output_name):
    print(f"[STEP] Generating optimized {output_name}...")
    
    with open(os.path.join(RESULTS_DIR, results_file), "r") as f:
        top5 = json.load(f)["top5"]
        best = top5[0] # The Rank #1 winner

    # Load original template (we'll just use the ones already on GitHub)
    pine_path = os.path.join(PINE_DIR, template_name)
    with open(pine_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # ORB replacements
        if "orb_end_min =" in line and "orb_optimizer" in results_file:
            new_lines.append(f'orb_end_min    = input.int({best["orb_end_min"]}, "ORB End Min", group="ORB Window")
')
        elif "atr_min_mult =" in line and "orb_optimizer" in results_file:
            new_lines.append(f'atr_min_mult   = input.float({best["atr_mult"]}, "Min ATR Mult", group="Filters")
')
        elif "vol_mult =" in line and "orb_optimizer" in results_file:
            new_lines.append(f'vol_mult       = input.float({best["vol_mult"]}, "Vol Multiplier", group="Filters")
')
        elif "rr_ratio =" in line and "orb_optimizer" in results_file:
            new_lines.append(f'rr_ratio       = input.float({best["rr_ratio"]}, "Reward:Risk", group="Risk")
')
        
        # Pullback replacements
        elif "ema_fast_len =" in line and "pullback_optimizer" in results_file:
            new_lines.append(f'ema_fast_len = input.int({best["ema_fast"]}, "Fast EMA", group="Trend")
')
        elif "rsi_low =" in line and "pullback_optimizer" in results_file:
            new_lines.append(f'rsi_low = input.int({best["rsi_zone"]}, "RSI Buy Pullback", group="Pullback")
')
        elif "rr_ratio =" in line and "pullback_optimizer" in results_file:
            new_lines.append(f'rr_ratio = input.float({best["rr_ratio"]}, "Reward:Risk", group="Risk")
')
        elif "atr_sl_mult =" in line and "pullback_optimizer" in results_file:
            new_lines.append(f'atr_sl_mult = input.float({best["atr_mult"]}, "ATR SL Mult", group="Risk")
')
        else:
            new_lines.append(line)

    with open(os.path.join(PINE_DIR, output_name), "w") as f:
        f.writelines(new_lines)
    print(f"[SUCCESS] {output_name} created with optimized variables!")

# ---- EXECUTION ----
print("="*60)
print("  GB MASTER AUTO-RUNNER STARTING")
print("="*60)

# 1. Run Optimizers
run_optimizer("3_orb_optimizer.py")
run_optimizer("4_pullback_optimizer.py")

# 2. Generate Optimized Pine Scripts
update_pine_script("GB-ORB-Strategy.pine", "orb_optimizer_top5.json", "GB-ORB-OPTIMIZED.pine")
update_pine_script("GB-Master-Ultimate-Strategy.pine", "pullback_optimizer_top5.json", "GB-PULLBACK-OPTIMIZED.pine")

print("
" + "="*60)
print("  ALL STEPS COMPLETE")
print("  Final optimized scripts are in 6_pine_scripts/")
print("  1. GB-ORB-OPTIMIZED.pine")
print("  2. GB-PULLBACK-OPTIMIZED.pine")
print("="*60)
