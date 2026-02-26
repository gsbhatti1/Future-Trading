``` pinescript
/*backtest
start: 2023-12-13 00:00:00
end: 2023-12-20 00:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy(title='[STRATEGY][RS]Spot/Binary Scalper V0', shorttitle='IC', overlay=true, initial_capital=100000, currency=currency.USD)
//  ||  Adapted from:
//  ||      http://www.binaryoptionsedge.com/topic/1414-ta-spot-scalping-it-works-damn-good/?hl=singh

//  ||  Ichimoku cloud:
conversionPeriods = input(title='Conversion Periods:', defval=7, minval=1),
basePeriods = 26 //input(title='Base Periods', defval=26, minval=1)
laggingSpan2Periods = 52 //input(title='Lagging Span:', defval=52, minval=1),
displacement = 26 //input(title='Displacement:', defval=26, minval=1)

f_donchian(_len) => avg(lowest(_len), highest(_len))

f_ichimoku_cloud(_conversion_periods, _base_periods, _lagging_span)=>
    _conversion_line  = (high(_conversion_periods) + low(_conversion_periods)) / 2
    _base_line        = (high(_base_periods) + low(_base_periods)) / 2
    _leading_span_a   = (_conversion_line + _base_line) / 2
    _leading_span_b   = (high(_laggingSpan2Periods) + low(_laggingSpan2Periods)) / 2
    
    cloud = [_leading_span_a, _leading_span_b]
    
    plot(cloud[0], title='Leading Span A', color=color.blue)
    plot(cloud[1], title='Leading Span B', color=color.orange)

    is_uptrend = close > cloud[0] and ta.adx(close) > 20
    is_downtrend = close < cloud[0] and ta.adx(close) > 20
    
    // Trade Rules:
    if (is_uptrend)
        strategy.entry("Long", strategy.long)
    
    if (is_downtrend)
        strategy.entry("Short", strategy.short)

    // Stop Loss and Take Profit
    stop_loss = v_input_7 * pointsize
    take_profit = v_input_8 * pointsize
    
    strategy.exit("Take Profit or Stop Loss", from_entry="Long", stop=stop_loss, limit=take_profit)
    strategy.exit("Take Profit or Stop Loss", from_entry="Short", stop=-stop_loss, limit=-take_profit)

// Strategy Arguments
v_input_1 = 7
v_input_2 = 14
v_input_3 = 20
v_input_4 = true
v_input_5 = "04:00-15:00"
v_input_6 = true
v_input_7 = 150
v_input_8 = 200

// Source (PineScript)
f_ichimoku_cloud(v_input_1, basePeriods, laggingSpan2Periods)
```