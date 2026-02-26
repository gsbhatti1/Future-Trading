<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RSI Multi-directional Momentum Strategy RSI-Momentum-Long-Short-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/170f858ca2195a0c150.png)

[trans]

## Overview

The RSI Multi-directional Momentum Strategy is a typical momentum strategy based on the Larry Connors RSI indicator, using overbought and oversold signals from the RSI to determine buy and sell decisions. The key is to identify whether the price is in an overbought or oversold state and use that as trading signals.

## Strategy Logic

The strategy constructs the RSI indicator by calculating the upward momentum and downward momentum of prices over a lookback period. When RSI falls below 10, it is considered oversold; when it exceeds 90, it is considered overbought. The strategy generates long signals when RSI crosses above the oversold level from below, and short signals when RSI crosses below the overbought level from above.

Additional moving average rules are added - only allowing long signals when the 5-day MA is above the 200-day MA, and short signals when the 5-day MA is below the 200-day MA. This helps filter out false signals caused by short-term rebounds.

Moreover, a profit-taking mechanism is also introduced. Long positions are forcibly closed when RSI rises above 90. Short positions are forcibly closed when RSI falls below 10. This locks in profits and prevents losses from expanding.

## Advantages of the Strategy

1. Using the RSI indicator to identify overbought/oversold conditions can catch price reversal moments.
2. Adding moving average filters can reduce false signals caused by short-term noise.
3. Profit-taking mechanisms help control risks and limit losses.
4. The strategy rules are simple and clear, making them easy to understand and implement.
5. RSI is a widely used and practical technical indicator, suitable for many instruments.

## Risks of the Strategy

1. An overbought/oversold condition in RSI does not always result in a price reversal.
2. Moving average filters may also filter out good trading opportunities.
3. Improper profit-taking settings can result in early lockouts and missed trends.
4. Parameters such as RSI lookback, overbought/oversold thresholds, and moving average settings need to be tuned.

These risks can be mitigated by optimizing parameters, combining other indicators, adjusting profit-taking mechanisms flexibly, etc.

## Enhancement Opportunities

1. Test the strategy with different RSI lookback periods.
2. Add other indicators like KDJ, MACD to complement the RSI.
3. Adjust overbought/oversold thresholds based on market conditions.
4. Fine-tune the profit-taking RSI levels based on holding period.
5. Incorporate stop loss strategies based on a percentage of maximum loss.
6. Optimize the moving average system, using dynamic trailing stop losses.

## Conclusion

The RSI Multi-directional Momentum Strategy catches short-term reversal opportunities by utilizing RSI to identify overbought/oversold conditions, filtered by moving averages and profit-taking rules. The strategy is simple and practical, worth further testing and enhancement to adapt to diverse market situations. Overall, it provides a good framework that can serve as a reference for developing quantitative trading strategies.

||


## Overview

The RSI Momentum Long Short Strategy is a typical momentum strategy based on the Larry Connors RSI indicator, using overbought and oversold signals from the RSI to determine entries and exits. The key is to identify whether the price is in an overbought or oversold state and use that as trading signals.

## Strategy Logic

The strategy constructs the RSI indicator by calculating the upward momentum and downward momentum of prices over a lookback period. When RSI falls below 10, it is considered oversold; when it exceeds 90, it is considered overbought. The strategy generates long signals when RSI crosses above the oversold level from below, and short signals when RSI crosses below the overbought level from above.

Additional moving average rules are added - only allowing long signals when the 5-day MA is above the 200-day MA, and short signals when the 5-day MA is below the 200-day MA. This helps filter out false signals caused by short-term rebounds.

Moreover, a profit-taking mechanism is also introduced. Long positions are forcibly closed when RSI rises above 90. Short positions are forcibly closed when RSI falls below 10. This locks in profits and prevents losses from expanding.

## Advantages of the Strategy

1. Using the RSI indicator to identify overbought/oversold conditions can catch price reversal moments.
2. Adding moving average filters can reduce false signals caused by short-term noise.
3. Profit-taking mechanisms help control risks and limit losses.
4. The strategy rules are simple and clear, making them easy to understand and implement.
5. RSI is a widely used and practical technical indicator, suitable for many instruments.

## Risks of the Strategy

1. An overbought/oversold condition in RSI does not always result in a price reversal.
2. Moving average filters may also filter out good trading opportunities.
3. Improper profit-taking settings can result in early lockouts and missed trends.
4. Parameters such as RSI lookback, overbought/oversold thresholds, and moving average settings need to be tuned.

These risks can be mitigated by optimizing parameters, combining other indicators, adjusting profit-taking mechanisms flexibly, etc.

## Enhancement Opportunities

1. Test the strategy with different RSI lookback periods.
2. Add other indicators like KDJ, MACD to complement the RSI.
3. Adjust overbought/oversold thresholds based on market conditions.
4. Fine-tune the profit-taking RSI levels based on holding period.
5. Incorporate stop loss strategies based on a percentage of maximum loss.
6. Optimize the moving average system, using dynamic trailing stop losses.

## Conclusion

The RSI Momentum Long Short Strategy catches short-term reversal opportunities by utilizing RSI to identify overbought/oversold conditions, filtered by moving averages and profit-taking rules. The strategy is simple and practical, worth further testing and enhancement to adapt to diverse market situations. Overall, it provides a good framework that can serve as a reference for developing quantitative trading strategies.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Entry area|
|v_input_2|90|overBought|
|v_input_3|10|overSold|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-25 00:00:00
end: 2023-10-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// author: SudeepBisht
//@version=3
// Based on Larry Connors RSI-2 Strategy - Lower RSI
strategy("SB_CM_RSI_2_Strategy_Version 2.0", overlay=true)

src = close
entry = input(defval=0, title="Entry area")
entry := nz(entry[1])
overBought = input(90)
overSold = input(10)

// RSI CODE
up = rma(max(change(src), 0), 2)
down = rma(-min(change(src), 0), 2)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))

// Criteria for Moving Avg rules
ma5 = sma(close, 5)
ma200 = sma(close, 200)

// Rule for RSI Color
col = close > ma200 and close < ma5 and rsi < 10 ? lime : close < ma200 and close > ma5 and rsi > 90 ? red : silver
chk = col == red ? -1 : col == lime ? 1 : 0

if (not na(rsi))
    if (crossover(rsi, overSold))
        if(chk[1] == 1)
            strategy.entry("RsiLE", strategy.long, comment="RsiLE")
            entry := 1
    if (crossunder(rsi, overBought))
        if(chk[1] == -1)
            strategy.entry("RsiSE", strategy.short, comment="RsiSE")
            entry := -1
        
if (not na(rsi))
    if (crossover(rsi, overSold) and entry == -1)
        strategy.close_all()
        //strategy.entry("RsiLE", strategy.long, comment="RsiLE")
        entry := 0
    if (crossunder(rsi, overBought) and entry == 1)
        strategy.close_all()
        //strategy.entry("RsiSE", strategy.short, comment="RsiSE")
        entry := 0
```

> Detail

https://www.fmz.com/strategy/430271

> Last Modified

2023-10-26 17:05:40