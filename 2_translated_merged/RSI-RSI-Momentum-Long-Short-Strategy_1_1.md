<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RSI Momentum Long Short Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/170f858ca2195a0c150.png)

[trans]

## Overview

The RSI Momentum Long Short Strategy is a typical momentum strategy based on the Larry Connors RSI indicator. It uses overbought and oversold signals from the RSI indicator to determine buy and sell decisions. The strategy primarily judges whether the price is in an overbought or oversold state and uses this as a signal for buying or selling.

## Strategy Principle

This strategy calculates the upward and downward momentum of prices over a certain period to construct the RSI indicator. When the RSI indicator is below the oversold line at 10, it is considered oversold. When the indicator is above the overbought line at 90, it is considered overbought. The strategy generates a buy signal when the RSI indicator crosses above the oversold line from below, and generates a sell signal when the RSI indicator crosses below the overbought line from above.

An additional moving average judgment rule has been incorporated into the strategy, requiring the 5-day moving average to be above the 200-day moving average to generate a buy signal, and the 5-day moving average to be below the 200-day moving average to generate a sell signal. This filters out false signals caused by short-term rebounds.

Additionally, the strategy includes a take-profit mechanism. When holding a long position, if the RSI indicator crosses above the overbought line at 90, all long positions will be forcibly closed. When holding a short position, if the RSI indicator crosses below the oversold line at 10, all short positions will be forcibly closed. This locks in profits and prevents losses from expanding.

## Strategy Advantages

1. Using the RSI indicator to judge overbought and oversold states can capture timing for price reversals.
2. Adding moving average filtering can reduce incorrect trades caused by short-term noise.
3. Setting a take-profit mechanism effectively controls risk and prevents loss expansion.
4. The strategy rules are simple and clear, making them easy to understand and implement.
5. RSI is a commonly used and practical technical indicator suitable for many stocks and cryptocurrencies.

## Strategy Risks

1. The RSI indicator may fail to reverse. Price being overbought or oversold does not necessarily lead to a reversal.
2. Moving average filtering may also filter out good trading opportunities.
3. Improper take-profit settings may result in premature profit-taking, preventing holding longer-term trends.
4. Parameters such as the calculation period for RSI, overbought and oversold thresholds, and moving average parameters need appropriate adjustment.

These risks can be mitigated through parameter optimization, combining other indicators, and appropriately loosening take-profit conditions.

## Strategy Optimization Directions

1. Different cycle RSI indicators can be tested for effectiveness.
2. Other indicators such as KDJ and MACD can be added to form a combination with RSI.
3. Overbought and oversold thresholds can be adjusted according to market conditions.
4. The RSI value for activating take-profit can be adjusted according to specific holding times.
5. Stop-loss strategies can be added to cut losses when they reach a certain percentage.
6. The moving average system can be optimized to use dynamic trailing stops.

## Summary

The RSI Momentum Long Short Strategy uses the RSI indicator to judge overbought and oversold states as signals, incorporating moving average and take-profit rules for screening and filtering. This effectively captures short-term reversal opportunities. The strategy is simple and practical and warrants further testing and optimization to adapt to broader market conditions. Overall, this strategy provides a good approach that can serve as a reference for developing quantitative trading strategies.

|| 

[/trans]

> Strategy Arguments



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

//authour: SudeepBisht
//@version=3
//Based on Larry Connors RSI-2 Strategy - Lower RSI
strategy("SB_CM_RSI_2_Strategy_Version 2.0", overlay=true)

src = close
entry= input(defval=0,title="Entry area")
entry:=nz(entry[1])
overBought=input(90)
overSold=input(10)
//RSI CODE
up = rma(max(change(src), 0), 2)
down = rma(-min(change(src), 0), 2)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
//Criteria for Moving Avg rules
ma5 = sma(close,5)
ma200= sma(close, 200)

//Rule for RSI Color
col = close > ma200 and close < ma5 and rsi < 10 ? lime : close < ma200 and close > ma5 and rsi > 90 ? red : silver
chk= col==red?-1:col==lime?1:0

if (not na(rsi))
    if (crossover(rsi, overSold))
        if(chk[1]==1)
            strategy.entry("RsiLE", strategy.long, comment="RsiLE")
            entry:=1
    if (crossunder(rsi, overBought))
        if(chk[1]==-1)
            strategy.entry("RsiSE", strategy.short, comment="RsiSE")
            entry:=-1
        
if (not na(rsi))
    if (crossover(rsi, overSold) and entry==-1)
        strategy.close_all()
        //strategy.entry("RsiLE", strategy.long, comment="RsiLE")
        entry:=0
    if (crossunder(rsi, overBought) and entry==1)
        strategy.close_all()
        //strategy.entry("RsiSE", strategy.short, comment="RsiSE")
        entry:=0
        

```

> Detail

https://www.fmz.com/strategy/430271

> Last Modified

2023-10-26 17:05:40