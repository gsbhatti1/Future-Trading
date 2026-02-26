<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

DEMA Volatility Index Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1ebd0d025cccd3156f3.png)

[trans]

## Overview

This strategy uses the Double Exponential Moving Average (DEMA) to calculate price volatility and applies additional smoothing to the volatility to identify trends in price fluctuations. It goes long when volatility is rising and short when volatility is falling.

## Strategy Logic

1. Calculate the Double Exponential Moving Average (DEMA) of prices using the formula: DEMA = 2*EMA(price, N) - EMA(EMA(price, N), N)

2. Calculate price volatility relative to DEMA: Volatility = (price - DEMA) / price * 100%

3. Apply another DEMA smoothing to the volatility to obtain trend signals

4. Go long when the smoothed volatility crosses above a certain level; go short when it crosses below a certain level

5. Trading can be limited to specific time periods

## Advantages

1. Using DEMA allows faster capture of price trend changes

2. Volatility reflects market sentiment - rising volatility indicates bullish dominance, while falling volatility indicates bearish dominance

3. Additional smoothing of volatility filters out short-term noise and captures major trends

4. Limiting trading to specific time periods avoids unnecessary slippage losses

5. Stop-loss and exit strategies help control risk

## Risks

1. During volatile markets, DEMA may lag, causing missed optimal entry points

2. The volatility indicator may produce false breakouts and should be verified with other indicators

3. Stop-loss levels should be set to prevent loss expansion

4. Outside trading hours, trading opportunities may be missed

5. Selection of trading hours requires historical data testing; inappropriate timing may reduce profitability

### Risk Mitigation Solutions

1. Optimize DEMA parameters by using smaller N values

2. Combine with other indicators such as RSI, MACD for comprehensive judgment

3. Determine stop-loss points based on historical data and maximum acceptable loss

4. Optimize selection of trading time periods

5. Test optimal trading periods separately for different instruments

## Optimization Directions

1. Test different DEMA parameter combinations to find optimal smoothing effects

2. Try other types of moving averages such as EMA, SMA, etc.

3. Apply multiple smoothing to the volatility indicator to find optimal smoothing parameters

4. Add other auxiliary indicators for multi-factor verification

5. Use machine learning methods to automatically optimize entry and exit parameters

6. Test optimal parameter combinations separately for different instruments

7. Enhance stop-loss and exit strategies for strict risk control

## Summary

This strategy quickly identifies changes in market sentiment trends by calculating DEMA-based price volatility and applying additional smoothing. It goes long when volatility rises and short when it falls, enabling trend-following trades. However, the strategy may suffer from DEMA lag and false breakouts. Parameters should be optimized, strict stop-losses applied, and other indicators used for comprehensive analysis. When used appropriately, this strategy can capture market trend reversal opportunities and achieve favorable investment returns.


||

## Overview

This strategy uses Double Exponential Moving Average (DEMA) to calculate price volatility, and further smoothes the volatility to detect trends in price fluctuations, going long when volatility rises and short when volatility falls.

## Strategy Logic

1. Calculate Double Exponential Moving Average (DEMA) of price, formula: DEMA = 2*EMA(price, N) - EMA(EMA(price, N), N)  

2. Calculate price volatility relative to DEMA: Volatility = (price - DEMA) / price * 100%

3. Apply DEMA smoothing on volatility again to get trend signal of volatility

4. When smoothed volatility crosses above a level, go long. When it crosses below, go short.

5. Can set to trade only during specific time period.

## Advantages

1. DEMA catches trend changes faster than simple moving averages.

2. Volatility reflects market sentiment, rise in volatility represents dominance of bulls, fall represents bears.

3. Smoothing volatility filters out short-term noise and captures major trend.  

4. Trading in specific time periods avoids unnecessary slippage costs.

5. Stop loss and exit strategies control risk.

## Risks

1. DEMA may lag during strong trends, missing best entry points.

2. Volatility index may give false signals, should combine with other indicators.

3. Should set stop loss to prevent magnified losses.

4. Missing opportunities outside trading time period. 

5. Trading time period needs testing on historical data, improper time may reduce profits.

### Risk Management

1. Optimize DEMA parameters, use smaller N values.

2. Combine other indicators like RSI, MACD for confirmation. 

3. Set stop loss based on historical data and maximum tolerable loss.

4. Optimize trading time period selection.

5. Test optimal trading times separately for different products.

## Enhancement Opportunities

1. Test different DEMA parameter combinations for best smoothing.

2. Try other moving averages like EMA, SMA. 

3. Additional smoothing of volatility with different parameters.

4. Add other indicators for multi-factor verification.

5. Use machine learning to auto-optimize entry and exit parameters.

6. Test optimal parameters separately for different products. 

7. Add stop loss and exit strategies to control risk.

## Summary 

This strategy captures trend changes in market sentiment by calculating smoothed DEMA volatility, going long when volatility rises and short when it falls. But DEMA lag and false signals are risks. Parameters should be optimized, strict stop loss implemented, and other indicators combined for confirmation. If used properly, this strategy can catch trend reversals and provide good investment returns.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|-2|buyper|
|v_input_2|2|sellper|
|v_input_3|50|Dema Length|
|v_input_4|true|Band for OverBought|
|v_input_5|-1|Band for OverSold|
|v_input_6|21|DEMA to Calculate dema of DPD|
|v_input_7|2018|yearfrom|
|v_input_8|2019|yearuntil|
|v_input_9|6|monthfrom|
|v_input_10|12|monthuntil|
|v_input_11|true|dayfrom|
|v_input_12|31|dayuntil|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-17 00:00:00
end: 2023-10-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version= 2
strategy("DEMA of DPD Strategy ",shorttitle="DPD% DEMA " ,overlay=false)

buyper =input(-2)
sellper=input(2)

demalen = input(50,title="Dema Length")

e1= ema(close,demalen)
e2=ema(e1,demalen)
demaprice  =   2 * e1 - e2

price=close
demadifper =  ((price-demaprice)/price)*100


OverDemaPer = input(1, title="Band for OverBought")
UnderDemaPer= input(-1,title="Band for OverSold")

band1 = hline(OverDemaPer)
band0 = hline(UnderDemaPer)
zeroline=0
fill(band1, band0, color=green, transp=90)


demalen2 = input(21,title="DEMA to Calculate dema of DPD")
demaofdpd =ema(demadifper,demalen2)
demaofdpd2 =ema(demaofdpd,demalen2)
resultstrategy = 2*demaofdpd - demaofdpd2

plot(resultstrategy,color=blue)


yearfrom = input(2018)
yearuntil =input(2019)
monthfrom =input(6)
monthuntil =input(12)
dayfrom=input(1)
dayuntil=input(31)



if (  crossover(resultstrategy,buyper)  ) 
    strategy.entry("BUY", strategy.long, stop=close, oca_name="TREND",  comment="BUY")
    
else
    strategy.cancel(id="BUY")


if ( crossunder(resultstrategy,sellper) ) 

    strategy.entry("SELL", strategy.short,stop=close, oca_name="TREND",  comment="SELL")
else
    strategy.cancel(id="SELL")
    
    
    
```

> Detail

https://www.fmz.com/strategy/430050

> Last Modified

2023-10-24 16:04:37