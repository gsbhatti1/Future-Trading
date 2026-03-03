``` pinescript
/*backtest
start: 2025-01-01 00:00:00
end: 2025-01-31 23:59:59
period: 30m
basePeriod: 30m
exchanges: [{"eid":"Binance","currency":"TRB_USDT"}]
*/

//@version=5
strategy(title="EMA & MA Crossover Strategy", shorttitle="EMA & MA Crossover Strategy", overlay=true)

// Inputs
LengthMA = input.int(100, minval=1, title="MA Length")
LengthEMA = input.int(200, minval=1, title="EMA Length")
swingLookback = input.int(20, title="Swing Lookback")
Lengthhmaribbon = input.int(70, minval=1, title="HMA Ribbon")
// Input for ignoring the first `n` candles of the day
ignore_n_candles = input.int(1, "Ignore First N Candles", minval=0)
// Input for percentage threshold to ignore high run-up candles
run_up_threshold = input.float(0.5, "Run-up Threshold (%)", minval=0.0)

//====================================================================
hmacondition = ta.hma(close, Lengthhmaribbon) > ta.hma(close, Lengthhmaribbon)[1]

//====================================================================
// Function to drop the first `n` candles
dropn(src, n) =>
    na(src[n]) ? na : src

// Request data with the first `n` candles dropped
valid_candle = not na(dropn(close, ignore_n_candles))
// Check for run-up condition on the previous candle
prev_run_up = (high[1] - low[1]) / low[1] * 100

// Combine conditions: exclude invalid candles and ignore high run-up candles
valid_entry_condition = valid_candle and prev_run_up <= run_up_threshold

//======================================================
// Define the
```