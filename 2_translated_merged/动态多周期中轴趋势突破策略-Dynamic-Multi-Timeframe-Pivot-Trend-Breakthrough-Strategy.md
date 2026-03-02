``` pinescript
/*backtest
start: 2024-03-31 00:00:00
end: 2025-03-29 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © yuxishejiang

//@version=6
//@version=5
strategy(title="BTC中轴策略优化-V2", overlay=true, pyramiding=1, initial_capital=5000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent, commission_value=0.075)

// 核心参数
strat_dir_input = input.string(title="Strategy Direction", defval="long", options=["long", "short"])
strat_dir_value = strat_dir_input == "long" ? strategy.direction.long : strat_dir_input == "short" ? strategy.direction.short : strategy.direction.all
strategy.risk.allow_entry_in(strat_dir_value)

// 指标计算
higherTF = input.timeframe("W", "Higher Timeframe")
pc = request.security(syminfo.tickerid, higherTF, close[1], barmerge.gaps_off, barmerge.lookahead_on)
ph = request.security(syminfo.tickerid, higherTF, high[1], barmerge.gaps_off, barmerge.lookahead_on)
pl = request.security(syminfo.tickerid, higherTF, low[1], barmerge.gaps_off, barmerge.lookahead_on)

PP = (ph + pl + pc) / 3
R1 = PP + (PP - pl)
S1 = PP - (ph - PP)
R2 = PP + (ph - pl)
S2 = PP - (ph - pl)
factor = input.int(2, "Factor")
R3 = ph + factor * (PP - pl)
S3 = pl - 2 * (ph - PP)

length = input.int(21, "RSI Length")
p = close
vrsi = ta.rsi(p, length)
pp_ema = ta.ema(vrsi, length)
d = (vrsi - pp_ema) * 5
cc = (vrsi + d + pp_ema) / 2

// 仓位管理变量
var float entry_qty = na

// 交易执行逻辑
longEntry = ta.crossover(cc, 0)
longExit = ta.crossover(high, R3)  // 使用实时最高价判断

shortEntry = ta.crossunder(low, S3)  // 改为使用S3支撑位
shortExit = ta.crossunder(cc, 0)     // 同步修改为下穿

if (longEntry)
    strategy.entry("Long", strategy.long)
    entry_qty := strategy.position_size

if (strategy.position_s
```