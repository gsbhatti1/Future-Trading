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
    _conversion_line = (highest(n(_conversion_periods)) + lowest(n(_conversion_periods))) / 2
    _base_line = (highest(n(_base_periods)) + lowest(n(_base_periods))) / 2
    leadingSpanA = (_conversion_line + _base_line) / 2
    leadingSpanB = (highest(n(_lagging_span)) + lowest(n(_lagging_span))) / 2
    
    cloud_upper = max(leadingSpanA, leadingSpanB)
    cloud_lower = min(leadingSpanA, leadingSpanB)
    
    plot(cloud_upper, color=color.blue, title='Upper Cloud')
    plot(cloud_lower, color=color.blue, title='Lower Cloud')

// ADX
adx_length = input(title='Length', defval=14, minval=1)
adx_threshold = 20

// Trade rules:
long_entry = crossover(_conversion_line, close) and adx >= adx_threshold
short_entry = crossunder(_conversion_line, close) and adx >= adx_threshold

if (long_entry or short_entry)
    if (v_input_4)
        // Trading session check
        time_in_session = v_input_5
        if not(time(timeframe.period, time.time(), timeformat.hour, timeformat.minute) in time_in_session)
            strategy.entry('Long', strategy.long)
            strategy.exit('Exit Long', 'Long', stop=_v_input_7, limit=_v_input_8)
        else
            strategy.close('Long')
            
    if (not v_input_4 or time_in_session.includes(time.time()))
        strategy.entry('Long', strategy.long)
        strategy.exit('Exit Long', 'Long', stop=_v_input_7, limit=_v_input_8)

// Plotting
plot(_conversion_line, color=color.red, title='Conversion Line')
plot(_base_line, color=color.green, title='Base Line')

```