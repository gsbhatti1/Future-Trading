``` pinescript
/*backtest
start: 2024-04-07 00:00:00
end: 2025-04-06 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
*/

//@version=5
strategy("EMA3 & RMA3 ATR Strategy", overlay=true, initial_capital=10000, currency=currency.USD)

// —— Input Parameters ——
ema_len = input.int(3, "EMA Length")
ema_mult = input.float(1.5, "EMA Channel ATR Multiplier", step=0.1)
rma_len = input.int(3, "RMA Length")
rma_mult = input.float(1.0, "RMA Channel ATR Multiplier", step=0.1)
atr_len = input.int(3, "ATR Length")

// —— Core Calculations ——
ema_val = ta.ema(close, ema_len)
atr_val = ta.atr(atr_len)
ema_upper = ema_val + atr_val * ema_mult
ema_lower = ema_val - atr_val * ema_mult

rma_val = ta.rma(close, rma_len)
rma_upper = rma_val + atr_val * rma_mult
rma_lower = rma_val - atr_val * rma_mult

// —— Signal Conditions ——
ema_buy = barstate.isconfirmed and close > ema_upper
ema_sell = barstate.isconfirmed and close < ema_lower
rma_buy = barstate.isconfirmed and close > rma_upper
rma_sell = barstate.isconfirmed and close < rma_lower

// —— Position Sizing ——
risk_percent = 0.5 // 0.5% risk per trade
position_size(price, stop_price) => 
    risk_amount = strategy.equity * risk_percent / 100
    math.abs(price - stop_price) > 0 ? (risk_amount / math.abs(price - stop_price)) : na

// —— Trading Logic ——
var float prev_open = na
if barstate.isconfirmed
    prev_open := open[1]

// Long Entry Logic
if (ema_buy or rma_buy) and strategy.position_size == 0
    stop_price = open
    qty = position_size(close, stop_price)
    if not na(qty)
        strategy.entry("Long", strategy.long, qty=qty)
        strategy.exit("Long Stop", "Long", stop=stop_price)

// Short Entry Logic
if (ema_sell or rma_sell) and strategy.position_size == 0
    stop_price = open
    qty = position_size(close, stop_price)
    if not na(qty)
        strategy.entry("Short", strategy.short, qty=qty)
        strategy.exit("Short Stop", "Short", stop=stop_price)

// Exit Logic
if strategy.position_size > 0
    if ta.crossover(low, prev_open)
        strategy.close("Long")

if strategy.position_size < 0
    if ta.crossunder(high, prev_open)
        strategy.close("Short")

// —— Visualization ——
plot(ema_val, "EMA3", color.new(#00BFFF, 0), 2)
plot(ema_upper, "EMA Upper", color.red, 1)
plot(ema_lower, "EMA Lower", color.green, 1)
plot(rma_val, "RMA3", color.new(#FFA500, 0), 2)
plot(rma_upper, "RMA Upper", #FF1493, 1)
plot(rma_lower, "RMA Lower", #32CD32, 1)

```