```pinescript
/*backtest
start: 2023-08-21 00:00:00
end: 2023-09-20 00:00:00
Period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
// Algokid code v. 1.00
strategy("AK_RSI 2 Strategy", overlay=true)

RS = rsi(close, 2) // Calculate the 2-period RSI value

shortMA = sma(close, 5) // 5-day simple moving average
longMA = sma(close, 200) // 200-day simple moving average

// Enter long when price breaks below the 200-day MA but above the 5-day MA and RSI(2) < 5
if (close > shortMA and close < longMA and RS < 5)
    strategy.entry("Buy", strategy.long)

// Enter short when price breaks above the 200-day MA but below the 5-day MA and RSI(2) > 90
if (close < shortMA and close > longMA and RS > 90)
    strategy.entry("Sell", strategy.short)

// Exit on re-cross of 5-day MA
if (close > shortMA)
    strategy.close("Buy")
    strategy.close("Sell")

```

Note: The Pine Script has been translated while maintaining the original code formatting. Ensure to test and optimize the script further as described in the document for better performance and risk management.