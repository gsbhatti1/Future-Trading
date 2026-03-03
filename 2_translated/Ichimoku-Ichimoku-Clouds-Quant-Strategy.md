``` pinescript
/*backtest
start: 2023-01-25 00:00:00
end: 2024-01-31 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5

//  -----------------------------------------------------------------------------
//  Copyright © 2024 Skyrex, LLC. All rights reserved.
//  -----------------------------------------------------------------------------

//  Version: v2.1
//  Release: Jan 22, 2024

strategy(title = "Advanced Ichimoku Clouds Strategy Long and Short", shorttitle="Ichimoku Clouds QS", overlay=false)

v_input_string_1 = input.string("yourBotSourceUuid", title="?Trading Bot Settings sourceUuid:")
v_input_string_2 = input.string("yourBotSecretToken", title="secretToken:")

// Trading Period Settings
start_date = input.time(timestamp("2023-01-01T00:00:00"), title="?Trading Period Settings Trade Start Date/Time")
end_date = input.time(timestamp("2025-01-01T00:00:00"), title="Trade Stop Date/Time")

// Trading Mode Settings
trading_mode_long = input.string("0", title="(?Trading Mode Settings)Trading Mode: Long|Short", options=["Long", "Short"])
entry_signals_long = input.string("0", title="(?Long Mode Signals - set up if Trading Mode: Long)Select Entry Signal (Long): Bullish All|Bullish Strong|Bullish Neutral|Bullish Weak|Bullish Strong and Neutral|Bullish Neutral and Weak|Bullish Strong and Weak|None")
exit_signals_long = input.string("0", title="Select Exit Signal (Long): Bearish Weak|Bearish Strong|Bearish Neutral|None|Bearish Strong and Neutral|Bearish Neutral and Weak|Bearish Strong and Weak|Bearish All")
entry_signals_short = input.string("0", title="(?Short Mode Signals - set up if Trading Mode: Short)Select Entry Signal (Short): None|Bearish Strong|Bearish Neutral|Bearish Weak|Bearish Strong and Neutral|Bearish Neutral and Weak|Bearish Strong and Weak|Bearish All")
exit_signals_short = input.string("0", title="Select Exit Signal (Short): None|Bullish Strong|Bullish Neutral|Bullish Weak|Bullish Strong and Neutral|Bullish Neutral and Weak|Bullish Strong and Weak|Bullish All")

// Risk Management
take_profit_percent = input.float(0, title="(?Risk Management)Take Profit, % (0 - disabled)")
stop_loss_percent = input.float(0, title="Stop Loss, % (0 - disabled)")

// Indicator Settings
tenkan_sen = input.int(9, title="?Indicator Settings Tenkan")
kijun_sen = input.int(26, title="Kijun", minval=1)
chikou_span = input.int(52, title="Chikou", minval=1)
offset = input.int(26, title="Offset", minval=0)

// Display Settings
show_tenkan = input.bool(false, title="Show Tenkan Line")
show_kijun = input.bool(false, title="Show Kijun Line")
show_senkou_a = input.bool(true, title="Show Senkou A Line")
show_senkou_b = input.bool(true, title="Show Senkou B Line")
show_chikou = input.bool(false, title="Show Chikou Line")

// Calculate Ichimoku Cloud Indicators
tenkan_sen_line = ta.sma(close, tenkan_sen)
kijun_sen_line = ta.sma(close, kijun_sen)
chikou_span_line = close[lag]
senkou_a = (tenkan_sen_line + kijun_sen_line) / 2
senkou_b = ta.ema(senkou_a, offset)

// Strategy Logic
if (start_date <= time and end_date >= time)
    if (trading_mode_long == "Long")
        // Enter long position based on entry signals
        if (entry_signals_long != "None" and ... and ...)
            strategy.entry("Long", strategy.long)
        
        // Exit long position based on exit signals
        if (exit_signals_long != "None" and ... and ...)
            strategy.exit("Exit Long", from_entry="Long")
    
    if (trading_mode_short == "Short")
        // Enter short position based on entry signals
        if (entry_signals_short != "None" and ... and ...)
            strategy.entry("Short", strategy.short)
        
        // Exit short position based on exit signals
        if (exit_signals_short != "None" and ... and ...)
            strategy.exit("Exit Short", from_entry="Short")

// Risk Management Logic
if (take_profit_percent > 0)
    take_profit_price = strategy.position_avg_cost + (strategy.position_avg_cost * take_profit_percent / 100)
    strategy.exit("Take Profit", from_entry="Long" or "Short", limit=take_profit_price)

if (stop_loss_percent > 0)
    stop_loss_price = strategy.position_avg_cost - (strategy.position_avg_cost * stop_loss_percent / 100)
    strategy.exit("Stop Loss", from_entry="Long" or "Short", stop=stop_loss_price)

// Display Indicators
plot(tenkan_sen_line, title="Tenkan Line", color=color.new(color.blue, 0), linewidth=2) if show_tenkan
plot(kijun_sen_line, title="Kijun Line", color=color.new(color.red, 0), linewidth=2) if show_kijun
plot(senkou_a, title="Senkou A Line", color=color.new(color.lime, 0), linewidth=2) if show_senkou_a
plot(senkou_b, title="Senkou B Line", color=color.new(color.orange, 0), linewidth=2) if show_senkou_b
plot(chikou_span_line, title="Chikou Span", color=color.new(color.gray, 0), linewidth=1) if show_chikou

```

This script provides the necessary configurations and logic for a multi-period strategy based on Ichimoku Clouds indicators. Ensure to fill in the conditions (e.g., `... and ...`) with specific trading signals checks as per your requirements.