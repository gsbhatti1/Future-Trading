``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("CCI, DMI, and MACD Strategy", overlay=true)

// Define inputs
cci_length = input(14, title="CCI Length")
overbought_level = input(100, title="Overbought Level")
oversold_level = input(-100, title="Oversold Level")

// Calculate CCI
cci_value = ta.cci(close, cci_length)

// Calculate DMI
[di_plus, di_minus, _] = ta.dmi(14, 14)

// Calculate MACD
[macd_line, signal_line, _] = ta.macd(close, 24, 52, 9)

// Define buy and sell conditions
buy_signal = ta.crossover(cci_value, oversold_level) and di_plus > di_minus and macd_line > signal_line // CCI crosses above -100, Di+ > Di-, and MACD > Signal
sell_signal = ta.crossunder(cci_value, overbought_level) and di_minus > di_plus and macd_line < signal_line // CCI crosses below 100, Di- > Di+, and MACD < Signal

// Place orders based on the signals
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.exit("Sell", "Buy")
```

This Pine Script translates the provided strategy logic into a complete script. The `buy_signal` is defined when CCI crosses above -100, DI+ > DI-, and MACD > Signal line, while the `sell_signal` is triggered when CCI crosses below 100, DI- > DI+, and MACD < Signal line. Orders are placed based on these conditions.