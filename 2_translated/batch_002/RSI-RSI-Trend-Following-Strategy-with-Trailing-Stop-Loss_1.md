> Name

RSI Trend Following Strategy with Trailing Stop Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1929faab3fb964b59cb.png)
[trans]

## Overview

This strategy is an automated trading strategy that utilizes the RSI indicator to identify trends, confirms the trend with moving averages, and sets stop-loss and take-profit levels. It goes long when RSI is above 68 and the current moving average crosses above the previous moving average; it goes short when RSI is below 28 and the current moving average crosses below the previous moving average. Stop-loss and take-profit points are also set accordingly.

## Strategy Logic

The strategy primarily uses the RSI indicator to identify overbought and oversold conditions to determine trends. An RSI above 70 indicates an overbought zone, while below 30 indicates an oversold zone. The trend is confirmed using golden cross and death cross signals from moving averages. Specific trading signals are as follows:

**Long Signal**: RSI greater than 68 and current moving average crossing above the previous moving average — go long.
**Short Signal**: RSI less than 28 and current moving average crossing below the previous moving average — go short.

Stop-loss and take-profit settings vary by point level, ranging from more relaxed to stricter:
- **Long Take Profit**: Take profit half position at 1.4% above high, full exit at 0.8% above high.
- **Long Stop Loss**: Set stop loss at 2% below entry price.

- **Short Take Profit**: Take profit half position at 0.4% below low, full exit at 0.8% below low.
- **Short Stop Loss**: Set stop loss at 2% above entry price.

Additionally, when trend reverses (e.g., RSI breaking below 30 while long), close all positions at market price; when RSI breaks above 60 while short, close all short positions at market price.

## Advantages

1. Uses RSI indicator to judge overbought/oversold conditions, avoiding chasing highs and selling lows.
2. Moving averages filter out non-mainstream directional operations.
3. Progressive take-profit setup maximizes profits.
4. Higher stop-loss points give appropriate space for trends.
5. Reversal-based clearing strategy quickly responds to unexpected events.

## Risks

1. Improper RSI parameter settings may lead to poor identification results.
2. Improper moving average parameter settings may result in ineffective filtering.
3. Overly loose stop-loss points increase risk of expanded losses.
4. Overly tight take-profit points prevent maximum profitability.
5. Misjudgment in reversal clearing strategies causes unnecessary losses.

To mitigate these risks, parameters should be tested and optimized multiple times. Stop-loss and take-profit settings should be appropriately adjusted based on market volatility. Clearing strategies should be carefully reviewed to avoid losses due to misinterpretation of indicators.

## Optimization Directions

Further optimization can focus on several aspects:

1. Add more filtering indicators to improve signal accuracy, such as volume filters.
2. Adjust stop-loss strategies to trail highest/lowest prices for dynamic trailing stops.
3. Change partial take-profit to trailing take-profit to maximize gains.
4. Add data source switching for different instruments with varying cycle parameters.
5. Consider futures holding costs and dynamically adjust stop-loss/take-profit accordingly.

## Summary

Overall, this is a relatively mature and reliable trend-following strategy. It uses RSI to identify overbought/oversold conditions to determine trade direction and employs moving averages for trend confirmation. Appropriate stop-loss and progressive take-profit mechanisms allow it to capture good returns during trending markets. With proper parameter tuning, it performs excellently in trending conditions. Further optimization can yield even better performance.

||

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_3|true|Start Date|
|v_input_int_4|6|Start Month|
|v_input_int_5|2022|Start Year|
|v_input_1|2|Return Precision|
|v_input_int_1|4|(?RSI Settings)RSI Length|
|v_input_source_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_string_1|0|(?MA Settings)MA Type: SMA|Bollinger Bands|EMA|SMMA (RMA)|WMA|VWMA|
|v_input_int_2|23|MA Length|
|v_input_float_1|2|BB StdDev|


> Source (PineScript)

``` pinescript
// © CRabbit
//@version=5

// Starting with $100 and using 10% of the account per trade
strategy("RSI Template", shorttitle="RSI", overlay=false, initial_capital=100, default_qty_value=10, default_qty_type=strategy.percent_of_equity)

// RSI Indicator
ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "Bollinger Bands" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

rsiLengthInput = input.int(4, minval=1, title="RSI Length", group="RSI Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
maLengthInput = input.int(23, title="MA Length", group="MA Settings")
bbMultInput = input.float(2.0, minval=0.001, maxval=50, title="BB StdDev", group="MA Settings")

up = ta.rma(math.max(ta.change(rsiSourceInput), 0), rsiLengthInput)
down = ta.rma(-math.min(ta.change(rsiSourceInput), 0), rsiLengthInput)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
rsiMA = ma(rsi, maLengthInput, maTypeInput)
isBB = maTypeInput == "Bollinger Bands"

plot(rsi, "RSI", color=#7E57C2)
plot(rsiMA, "RSI-based MA", color=color.green)
rsiUpperBand = hline(70, "RSI Upper Band", color=#787B86)
hline(50, "RSI Middle Band", color=color.new(#787B86, 50))
rsiLowerBand = hline(30, "RSI Lower Band", color=#787B86)
fill(rsiUpperBand, rsiLowerBand, color=color.rgb(126, 87, 194, 90), title="RSI Background Fill")


// Configure backtest start date with inputs
startDate = input.int(title="Start Date", defval=1, minval=1, maxval=31)
startMonth = input.int(title="Start Month", defval=6, minval=1, maxval=12)
startYear = input.int(title="Start Year", defval=2022, minval=1800, maxval=2100)

// See if this bar's time happened on/after start date
afterStartDate = (time >= timestamp(syminfo.timezone,
     startYear, startMonth, startDate, 0, 0))


// Long and Short buy strategy
// Submit a market open/ close Long order, but only on/after start date
if (afterStartDate)
    if rsi > 68 and (rsiMA > rsiMA[1])
        strategy.entry("Long Order", strategy.long, comment="ENTER-LONG")
    if rsi < 30
        strategy.close("Long Order", alert_message="L-CL")

strategy.exit("L-TP1", from_entry="Long Order", limit=high * 1.004, qty_percent=50, alert_message="L-TP1" + str.tostring(high * 1.004))
strategy.exit("L-TP2", from_entry="Long Order", limit=high * 1.008, qty_percent=100, alert_message="L-TP2" + str.tostring(high * 1.008))
strategy.exit("Exit Long", from_entry="Long Order", stop=low * 0.98, alert_message="L-SL" + str.tostring(low * 0.98))        


// Submit a market Open/ Close Short order, but only on/after start date
if (afterStartDate)
    if rsi < 28 and (rsiMA < rsiMA[1])
        strategy.entry("Short Order", strategy.short, comment="ENTER-SHORT")
    if rsi > 60
        strategy.close("Short Order", alert_message="S-CL")    

strategy.exit("S-TP1", from_entry="Short Order", limit=low * 0.996, qty_percent=50, alert_message="S-TP1" + str.tostring(low * 0.996))
strategy.exit("S-TP2", from_entry="Short Order", limit=low * 0.992, qty_percent=100, alert_message="S-TP2" + str.tostring(low * 0.992))
strategy.exit("Exit Short", from_entry="Short Order", stop=high * 1.02, alert_message="S-SL" + str.tostring(high * 1.02))

// MONTHLY TABLE //

prec      = input(2, title = "Return Precision")

new_month = month(time) != month(time[1])
new_year  = year(time)  != year(time[1])

eq = strategy.equity

bar_pnl = eq / eq[1] - 1

cur_month_pnl = 0.0
cur_year_pnl  = 0.0

// Current Monthly P&L
cur_month_pnl := new_month ? 0.0 : 
                 (1 + cur_month_pnl[1]) * (1 + bar_pnl) - 1 

// Current Yearly P&L
cur_year_pnl := new_year ? 0.0 : 
                 (1 + cur_year_pnl[1]) * (1 + bar_pnl) - 1  

// Arrays to store Yearly and Monthly P&Ls
var month_pnl  = array.new_float(0)
var month_time = array.new_int(0)

var year_pnl  = array.new_float(0)
var year_time = array.new_int(0)

if (not na(cur_month_pnl[1]) and (new_month or barstate.islast))
    array.push(month_pnl , cur_month_pnl[1])
    array.push(month_time, time[1])

if (not na(cur_year_pnl[1]) and (new_year or barstate.islast))
    array.push(year_pnl , cur_year_pnl[1])
    array.push(year_time, time[1])

// Monthly P&L Table    
var monthly_table = table(na)

if (barstate.islast)
    monthly_table := table.new(position.bottom_right, columns = 14, rows = array.size(year_pnl) + 1, border_width = 1)

    table.cell(monthly_table, 0,  0, "",     bgcolor = #cccccc)
    table.cell(monthly_table, 1,  0, "Jan",  bgcolor = #cccccc)
    table.cell(monthly_table, 2,  0, "Feb",  bgcolor = #cccccc)
    table.cell(monthly_table, 3,  0, "Mar",  bgcolor = #cccccc)
    table.cell(monthly_table, 4,  0, "Apr",  bgcolor = #cccccc)
    table.cell(monthly_table, 5,  0, "May",  bgcolor = #cccccc)
    table.cell(monthly_table, 6,  0, "Jun",  bgcolor = #cccccc)
    table.cell(monthly_table, 7,  0, "Jul",  bgcolor = #cccccc)
    table.cell(monthly_table, 8,  0, "Aug",  bgcolor = #cccccc)
    table.cell(monthly_table, 9,  0, "Sep",  bgcolor = #cccccc)
    table.cell(monthly_table, 10, 0, "Oct",  bgcolor = #cccccc)
    table.cell(monthly_table, 11, 0, "Nov",  bgcolor = #cccccc)
    table.cell(monthly_table, 12, 0, "Dec",  bgcolor = #cccccc)
    table.cell(monthly_table, 13, 0, "Year", bgcolor = #999999)


    for yi = 0 to array.size(year_pnl) - 1
        table.cell(monthly_table, 0,  yi + 1, str.tostring(year(array.get(year_time, yi))), bgcolor = #cccccc)
        
        y_color = array.get(year_pnl, yi) > 0 ? color.new(color.green, transp = 50) : color.new(color.red, transp = 50)
        table.cell(monthly_table, 13, yi + 1, str.tostring(math.round(array.get(year_pnl, yi) * 100, prec)), bgcolor = y_color)
        
    for mi = 0 to array.size(month_time) - 1
        m_row   = year(array.get(month_time, mi))  - year(array.get(year_time, 0)) + 1
        m_col   = month(array.get(month_time, mi)) 
        m_color = array.get(month_pnl, mi) > 0 ? color.new(color.green, transp = 70) : color.new(color.red, transp = 70)
        
        table.cell(monthly_table, m_col, m_row, str.tostring(math.round(array.get(month_pnl, mi) * 100, prec)), bgcolor = m_color)      

```

> Detail

https://www.fmz.com/strategy/434679

> Last Modified

2023-12-08 11:41:31