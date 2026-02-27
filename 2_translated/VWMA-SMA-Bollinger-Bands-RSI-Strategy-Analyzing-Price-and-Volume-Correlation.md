```pinescript
/*backtest
start: 2022-08-31 00:00:00
end: 2023-09-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
//@version=2
// strategy("VWMA + SMA Bollinger Bands + RSI, Analyzing Price and Volume Correlation", shorttitle="VWMA_SMA_BB_RSI_Strat", overlay=true)

// This strategy combines the Volume Weighted Moving Average (VWMA), Simple Moving Average (SMA) Bollinger Bands, and Relative Strength Index (RSI) indicators to identify potential buying and selling opportunities by examining the correlation between price changes and volume changes.

// Version 1.0
// Developed by BiO618 based on ChartArt's original "CA_RSI_Bolling_Strat".

// This strategy uses a modified RSI to sell when the RSI increases over the value of 55 (or to buy when the value falls below 45), with the classic Bollinger Bands strategy to sell when the price is above the upper Bollinger Band (and to buy when this value is below the lower band).
// The VWMA provides a faster correlation between price and volume changes. As the volume increases, the VWMA decreases, indicating potential changes in market sentiment.

// It's important to note that no indicator can guarantee accurate predictions in the market. Therefore, it is recommended to support your interpretation of this strategy with other indicators such as the Moving Average Convergence Divergence (MACD) and additional analysis tools.
// No strategy is foolproof, and traders should exercise caution and conduct thorough analysis before executing trades.

///////////// RSI
RSIlength = input(16, title="RSI Period Length")
RSIvalue = input(45, title="RSI Value Range")
RSIoverSold = 0 + RSIvalue
RSIoverBought = 100 - RSIvalue
price = close
vrsi = rsi(price, RSIlength)


///////////// Bollinger Bands
BBlength = input(20, minval=1, title="SMA Bollinger Bands Period Length")
BBmult = input(2.0, minval=0.001, maxval=50, title="Bollinger Bands Standard Deviation")
BBbasis = sma(price, BBlength)
BBdev = BBmult * stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev
source = close
buyEntry = crossover(source, BBlower)
sellEntry = crossunder(source, BBupper)
plot(BBbasis, color=aqua, title="Bollinger Bands SMA Basis Line")
p1 = plot(BBupper, color=silver, title="Bollinger Bands Upper Line")
p2 = plot(BBlower, color=silver, title="Bollinger Bands Lower Line")
fill(p1, p2)

basis2 = vwma(price, BBlength)                                           // Notice that the basis is based on a VWMA and not an SMA.

vwma = plot(basis2, color=orange, linewidth=2, title="VWMA")              // Plotting VWMA with a line width of 2 for better visibility
```