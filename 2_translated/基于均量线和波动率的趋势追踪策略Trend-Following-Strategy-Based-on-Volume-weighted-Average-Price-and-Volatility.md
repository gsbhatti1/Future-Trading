> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_15|false|Solid Color Slow Leadline|
|v_input_16|false|Solid Color Fast Leadline|
|v_input_1|9|(?Tenkansen / Kijunsen)Slow Tenkan Sen VWAP Line Length|
|v_input_2|26|Slow Kijun Sen VWAP Line Length|
|v_input_3|5|Fast Tenkan Sen VWAP Line Length|
|v_input_4|13|Fast Kijun Sen VWAP Line Length|
|v_input_5|20|(?Bollinger Bands)Bollinger Band Length|
|v_input_6|2|Bollinger Band StdDev|
|v_input_7|13|(?Time Segmented Volume)TSV Length|
|v_input_8|7|TSV Ema Length|
|v_input_9|true|(?Backtest Range)Start Date|
|v_input_10|true|Start Month|
|v_input_11|2000|Start Year|
|v_input_12|31|End Date|
|v_input_13|12|End Month|
|v_input_14|2021|End Year|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-09-14 00:00:00
end: 2023-09-20 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=4

// Credits

// "Vwap with period" code which used in this strategy to calculate the leadLine was written by "neolao" active on https://tr.tradingview.com/u/neolao/
// "TSV" code which used in this strategy was written by "liw0" active on https://www.tradingview.com/u/liw0. The code is corrected by "vitelot" December 2018.

strategy("HYE Trend Hunter [Strategy]", overlay = true, initial_capital = 1000, default_qty_value = 100, default_qty_type = strategy.percent_of_equity, commission_value = 0.025, pyramiding = 0)
  
// Strategy inputs 

slowtenkansenPeriod = input(9, minval=1, title="Slow Tenkan Sen VWAP Line Length", group = "Tenkansen / Kijunsen")
slowkijunsenPeriod = input(26, minval=1, title="Slow Kijun Sen VWAP Line Length", group = "Tenkansen / Kijunsen")
fasttenkansenPeriod = input(5, minval=1, title="Fast Tenkan Sen VWAP Line Length", group = "Tenkansen / Kijunsen")
fastkijunsenPeriod = input(13, minval=1, title="Fast Kijun Sen VWAP Line Length", group = "Tenkansen / Kijunsen")
BBlength = input(20, minval=1, title= "Bollinger Band Length", group = "Bollinger Bands")
BBmult = input(2.0, minval=0.001, maxval=50, title="Bollinger Band StdDev", group = "Bollinger Bands")
tsvlength  = input(13, minval=1, title="TSV Length", group = "Time Segmented Volume")
tsvemaperiod = input(7, minval=1, title="TSV Ema Length", group = "Time Segmented Volume")

// Make input options that configure backtest date range  

startDate = input(title="Start Date", type=input.time, defval=datetime(2000, 1, 1), minval=datetime(1970, 1, 1))
endDate = input(title="End Date", type=input.time, defval=datetime(2023, 12, 31), maxval=datetime(2025, 12, 31))

// Calculate VWAP lines
slowLeadline = vwap(slowkijunsenPeriod)
fastLeadline = vwap(fastkijunsenPeriod)

// Plot the VWAP lines and Bollinger Bands
plot(slowLeadline, color=color.new(color.blue, 0), linewidth=2, title="Slow Leadline")
plot(fastLeadline, color=color.new(color.red, 0), linewidth=2, title="Fast Leadline")

// Calculate Bollinger Bands
src = vwap(slowkijunsenPeriod)
basis = sma(src, BBlength)
dev = BBmult * stdev(src, BBlength)
upperBB = basis + dev
lowerBB = basis - dev

plot(basis, color=color.new(color.orange, 0), linewidth=2, title="Bollinger Middle Band")
plot(upperBB, color=color.new(color.green, 0), linewidth=1, title="Upper Bollinger Band")
plot(lowerBB, color=color.new(color.red, 0), linewidth=1, title="Lower Bollinger Band")

// Calculate TSV
tsv = tsvlength < 2 ? na : ema(volume[tsvlength], tsvemaperiod)

// Plot the TSV line
plot(tsv, title="Time Segmented Volume (TSV)", color=color.new(color.purple, 0), linewidth=1)

// Generate buy and sell signals
longCondition = crossover(fastLeadline, slowLeadline) and vwap(slowkijunsenPeriod) > upperBB and tsv > 0
shortCondition = crossunder(fastLeadline, slowLeadline) and vwap(slowkijunsenPeriod) < lowerBB and tsv < 0

strategy.entry("Long", strategy.long, when=longCondition)
strategy.close("Long", when=crossover(vwap(slowkijunsenPeriod), lowerBB))
strategy.close_on_signal = true

// Set stop loss and take profit levels
stopLossLevel = low[1] - (high[1] - low[1]) * 0.025
takeProfitLevel = high[1] + (high[1] - low[1]) * 0.025

strategy.exit("Exit Long", from_entry="Long", limit=takeProfitLevel, stop=stopLossLevel)

```

---

## Overview

This strategy integrates multiple indicators including volume-weighted average price, Bollinger Bands, and time segmented volume to identify the start and end of price trends and follow trends. The use of multiple confirmations effectively filters false breakouts.

## Strategy Logic

The strategy involves the following key steps:

1. Calculate fast and slow volume-weighted average price (VWAP) lines using VWAP instead of close price, which better reflects actual trading prices.
2. Compute the average of the VWAP lines to plot Bollinger Bands. Expanding volatility shown by bands suggests a trend start.
3. Introduce time segmented volume (TSV) to confirm increasing trading volume and validate the trend.
4. Generate buy signals when the fast VWAP crosses above the slow VWAP, price breaks above the upper Bollinger Band, and TSV is positive. Sell signals are generated in reverse.
5. Use VWAP pullback and lower Bollinger Band as stop loss signals.

## Advantages

- Multiple confirmations effectively filter false breakouts and identify trend start
- VWAP calculation reflects actual trading prices better 
- Volatility indicators judge if a trend is present
- Trading volume confirms trend continuation  
- Reasonable stop loss and take profit controls risk
- Configurable parameters allow flexible optimization

## Risks

- Difficulty in optimizing multiple indicators
- Lagging nature of VWAP and Bollinger Bands delays stop loss
- TSV sensitive to parameter tuning for different markets
- More false signals in range-bound markets
- Ignores trading costs, actual P&L weaker than backtest

## Enhancements

- Apply machine learning to auto optimize parameter combinations
- Set dynamic or trailing stop loss to better lock in profits
- Add volume momentum indicators to avoid divergence 
- Incorporate Elliott Waves to determine trend stages, adjust parameters accordingly
- Consider trading costs, set minimum profit target to control cost efficiency

## Conclusion

This strategy provides good trend identification by integrating multiple indicators. It can effectively determine the start and end of real trends. Further improvements in stability can be achieved through parameter optimization, stop loss optimization, and filter optimization. But overall, as a trend following strategy, it still carries certain levels of drawdown and risk-reward ratios. Traders need patience to wait for opportunities and strict risk management mindset.

---

This PineScript code defines the implementation details of the strategy described in the document, including the calculation methods for VWAP lines, Bollinger Bands, and TSV, as well as the generation of buy/sell signals based on these indicators.