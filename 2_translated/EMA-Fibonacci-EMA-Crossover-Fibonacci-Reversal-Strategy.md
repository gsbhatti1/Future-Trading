``` pinescript
/*backtest
start: 2024-08-26 00:00:00
end: 2024-09-24 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA Crossover Fibonacci Reversal Strategy", overlay=true)

// Indicators
ema50 = ta.ema(close, 50)
rsi = ta.rsi(close, 14)

// Function to calculate Fibonacci levels
fibonacci_levels(high_price, low_price) =>
    // Calculate the range and the key Fibonacci levels (38.2%, 50%, 61.8%)
    range = high_price - low_price
    fib_382 = low_price + (range * 0.382)
    fib_50 = low_price + (range * 0.5)
    fib_618 = low_price + (range * 0.618)

    // Return the Fibonacci levels as an array
    [fib_382, fib_50, fib_618]
```

This translation maintains the original Pine Script code blocks, numbers, and formatting while translating the human-readable text from Chinese to English.