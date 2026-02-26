---

## Overview

The Improved RSI Breakout Strategy is a trend-following strategy that uses the Relative Strength Index (RSI) indicator to determine entry and exit points. It builds upon a basic RSI strategy by adding stop loss and take profit orders to manage risk.

When RSI crosses above 70 (overbought level), the strategy goes long. When RSI crosses below 30 (oversold level), the strategy goes short. This allows it to ride strong trends up and down. Stop loss and take profit orders are then used to lock in profits and limit losses on existing positions.

## How it Works

The core mechanism relies on the RSI indicator crossing its overbought level (default 70) or oversold level (default 30) to trigger entries.

- When RSI crosses above 70, it indicates the asset is overbought and may reverse, so the strategy opens a long position.
  
- When RSI crosses below 30, it indicates the asset is oversold and may bounce, so the strategy opens a short position.

This allows the strategy to capitalize on mean reversion tendencies coming off extreme RSI levels.

The key enhancement is the added risk management through stop loss and take profit orders.

After entering a position, stop loss and take profit orders are placed at fixed percentages away from the entry price (default 2% stop loss, 10% take profit). This locks in a fixed reward to risk ratio on every trade.

If a position moves favorably, the take profit limit order will close it for a gain. If it moves adversely, the stop loss order will close it for a small loss. This maximizes profits in winning trades and minimizes losses from losing trades.

## Advantages

- Rides strong trends by buying dips and selling rallies.
- Take profit targets larger than stop loss targets allow asymmetric risk-reward.
- Stop losses minimize losses on trades going the wrong direction.
- Simple concept easy to understand and implement.
- Added risk management gives it an edge over basic RSI strategies.

## Risks

- Whipsaws possible if RSI crosses levels multiple times.
- Stop loss placement can be optimized.
- Take profit levels need fine tuning for better performance.
- Works best in trending markets, range-bound performance weaker.

## Enhancements

Some ways the strategy can be improved further:

- Add additional filters before entry trigger, such as a price breakout.
- Trail stop loss levels to lock in more profits in winning trades.
- Expand take profit targets for bigger reward potential.
- Optimize RSI levels, stop loss %, and take profit % for each market.
- Adapt to volatility conditions by using ATR for stop loss size.

## Conclusion

The Improved RSI Breakout Strategy brings together several positive elements—using RSI to identify potential turning points, trend following entries in the direction of momentum, asymmetric risk-reward from take profits > stop loss, and risk mitigation from exit orders.

By combining these aspects, it aims to maximize reward while minimizing risk on each trade. Proper optimization and robust position sizing can turn this into a stable system across various market environments. The built-in risk controls give it an edge over basic RSI strategies.

---

## Summary

The Improved RSI Breakout Strategy combines several positive elements: using the RSI indicator to identify potential turning points, trend-following entries in the direction of momentum, asymmetric risk-reward from take profits greater than stop losses, and risk mitigation through exit orders.

By integrating these features, it aims to optimize reward while minimizing risk per trade. Appropriate optimization and robust position sizing can make this strategy stable across different market conditions. The built-in risk controls provide an advantage over basic RSI strategies.

---

## Strategy Arguments

|Argument|Default|Description|
|--------|-------|-----------|
|v_input_1|70|overbought value|
|v_input_2|30|oversold value|

## Source (PineScript)

```pinescript
/*backtest
start: 2024-01-04 00:00:00
end: 2024-02-03 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=4
// Improved RSI Simple Strategy
// Added Risk Management System: SL & TP
// © Bitduke
// All scripts: https://www.tradingview.com/u/Bitduke/#published-scripts

strategy("Simple RSI Buy/Sell at a level", shorttitle="Simple RSI Strategy (SL/TP)", overlay=false )
overbought = input(70, title="overbought value")
oversold = input(30, title="oversold value")

lenght = 14
rsi = rsi(close, length)
myrsi = rsi > overbought
myrsi2 = rsi < oversold

barcolor(myrsi ? color.black : na)
barcolor(myrsi2 ? color.blue : na)

// Risk Management System
convert_percent_to_points(percent) =>
    strategy.position_size != 0 ? round(percent / 100 * strategy.position_avg_price / syminfo.mintick) : float(na)
    
setup_percent(percent) =>
    convert_percent_to_points(percent)

STOP_LOSS = 2
TAKE_PROFIT = 10

plot(rsi)
plot(overbought, color=color.red)
plot(oversold, color=color.green)

//STRATEGY
if (myrsi)
    strategy.entry("Long", strategy.long)
    
if (myrsi2)
    strategy.entry("Short", strategy.short)

strategy.exit("Exit", qty_percent=100, profit=setup_percent(STOP_LOSS), loss=setup_percent(TAKE_PROFIT))
```

## Detail

https://www.fmz.com/strategy/440990

## Last Modified

2024-02-04 15:27:50