``` pinescript
/*backtest
start: 2022-08-31 00:00:00
end: 2023-09-06 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
//@version=2
// strategy("VWMA + SMA Bollinger Bands + RSI, Modified Strategy (by BiO618)", shorttitle="VWMA_Bol_Strat", overlay=true)

// Modified VWMA + SMA Bollinger Bands + RSI strategy based on ChartArt's original "CA_RSI_Bolling_Strat"
//
// Version 1.0
// Developed by BiO618, inspired by ChartArt's idea.
//
// This strategy combines the Volume Weighted Moving Average (VWMA), Simple Moving Average Bollinger Bands, and Relative Strength Index (RSI) to identify potential buying and selling opportunities based on price-volume correlation. Traders can use these signals to make informed decisions.
//
// List of my work: 
// https://www.tradingview.com/u/BiO618/
// 
//  __             __  ___       __  ___ 
// /  ` |__|  /\  |__)  |   /\  |__)  |  
// \__, |  | /~~\ |  \  |  /~~\ |  \  |  
// 
// 


///////////// RSI
RSIlength = input(16, title="RSI Period Length") 
RSIvalue = input(45, title="RSI Value Range") 
RSIoverSold = 0 + RSIvalue
RSIoverBought = 100 - RSIvalue
price = close
vrsi = rsi(price, RSIlength)


///////////// Bollinger Bands
BBlength = input(20, minval=1, title="SMA Period Length for Bollinger Bands")
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

basis2 = vwma(price, BBlength)                                           //Notice that the basis is based on a vwma and not a sma.

vwma = plot(basis2, color=orange, title="Volume Weighted Moving Average", linewidth=2)
```