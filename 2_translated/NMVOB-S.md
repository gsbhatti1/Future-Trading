> Name

NMVOB-S

> Author

ChaoZhang

> Strategy Description

**backtest**

 ![IMG](https://www.fmz.com/upload/asset/198ea25e0b20cb3e586.png) 

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_float_1|50000|Initial Capital|
|v_input_int_1|5|Leverage|
|v_input_1|false|Stop Loss Pillars Number|
|v_input_float_2|true|Take Profit Ratio|
|v_input_2|13|MACD Fast MA|
|v_input_3|21|MACD Slow MA|
|v_input_4|9|MACD Trigger|
|v_input_5|50|MACD Normalize|
|v_input_int_2|true|(MACD) 1=Ema, 2=Wma, 3=Sma|
|v_input_6|100|VS Period|
|v_input_int_3|34|Bollinger Bands Period|
|v_input_7_close|0|Boollinger Bands Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_float_3|2|StdDev|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-04-10 00:00:00
end: 2022-05-09 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5

// # ========================================================================= #
// #                   |   STRATEGY  |
// # ========================================================================= #
strategy(title = "NMVOB-S", shorttitle = "NMVOB-S", overlay = true , calc_on_every_tick = false , initial_capital = 0)
// # ========================================================================= #
// #                   |  Global Variables START  |
// # ========================================================================= #
var current_trend = int(na)
var open_order_type = int(na)
var stop_loss_price = float(na)
var stop_profit_price = float(na)
var sl = float(na)
var open_order_price = float(na)
var open_type_flag = int(na)
var stop_profit_flag = 0

var macd_signal_position = 0
var macd_signal_type = int(na)

var start_price = input.float(50000, "Initial Capital")
var gg = input.int(5, "Leverage")

// # ========================================================================= #
// #                   |  Global Variables END  |
// # ========================================================================= #

// # ========================================================================= #
// #                   |  Custom Functions START  |
// # ========================================================================= #
stop_loss_pillars = input(defval = 0, title = "Stop Loss Pillars Number")
stop_profit_proportion = input.float(1,"Take Profit Ratio")

calculate_stop_loss() =>
    if current_trend == 1
        stop_loss_price_buy = low
        if stop_loss_pillars == 0
            stop_loss_price_buy
        else
            for i = 1 to stop_loss_pillars 
                if low[i] < stop_loss_price_buy
                    stop_loss_price_buy := low[i]
                else if low[i] > stop_loss_price_buy
                    stop_loss_price_buy
            stop_loss_price_buy
    else
        stop_loss_price_sell = high
        if stop_loss_pillars == 0
            stop_loss_price_sell
        else
            for i = 1 to stop_loss_pillars 
                if high[i] < stop_loss_price_sell
                    stop_loss_price_sell
                else if high[i] > stop_loss_price_sell
                    stop_loss_price_sell := high[i]
            stop_loss_price_sell

calculate_stop_profit(cur_stop_loss_price) =>
    value = math.abs(close - cur_stop_loss_price) * stop_profit_proportion
    if current_trend == 1
        close + value
    else
        close - value   

// # ========================================================================= #
// #                   |  Custom Functions END  |
// # ========================================================================= #


// # ========================================================================= #
// #                   |   Normalized MACD  |
// # ========================================================================= #
sma = input(13,title='MACD Fast MA')
lma = input(21,title='MACD Slow MA')
tsp = input(9,title='MACD Trigger')
np = input(50,title='MACD Normalize')
type = input.int(1,minval=1,maxval=3,title="(MACD) 1=Ema, 2=Wma, 3=Sma")

sh = type == 1 ? ta.ema(close,sma)  
 : type == 2 ? ta.wma(close, sma)
 : ta.sma(close, sma)

lon=type == 1 ? ta.ema(close,lma) 
 : type == 2 ? ta.wma(close, lma)
 : ta.sma(close, lma)

ratio = math.min(sh,lon)/math.max(sh,lon)

Mac = if sh>lon
    2 - ratio - 1
else
    ratio - 1
// Fast Line
MacNorm = ((Mac-ta.lowest(Mac, np)) /(ta.highest(Mac, np)-ta.lowest(Mac, np)+.000001)*2)- 1

MacNorm2 = if np < 2
    Mac
else
    MacNorm
// Slow Line    
Trigger = ta.wma(MacNorm2, tsp)

if ta.crossover(source1 = MacNorm, source2 = Trigger) 
    macd_signal_position := 0
    macd_signal_type := 1
else if ta.crossunder(source1 = MacNorm, source2 = Trigger) 
    macd_signal_position := 0
    macd_signal_type := 0
else
    macd_signal_position += 1

// # ========================================================================= #
// #                   |   Normalized MACD  |
// # ========================================================================= #


// # ========================================================================= #
// #                   |  Volatility Oscillator START  |
// # ========================================================================= #
length = input(100, title="VS Period")
spike = close - open
vs_up_line = ta.stdev(spike,length)
vs_low_line = ta.stdev(spike,length) * -1
// # ========================================================================= #
// #                   |  Volatility Oscillator END  |
// # ========================================================================= #


// # ========================================================================= #
// #                   |  Bollinger Bands  |
// # ========================================================================= #
b_length = input.int(34, minval=1 , title="Bollinger Bands Period")
src = input(close, title="Boollinger Bands Source")
mult = input.float(2.0, minval=0.001, maxval=50, title="StdDev")
basis = ta.sma(src, b_length)
dev = mult * ta.stdev(src, b_length)
upper = basis + dev
lo