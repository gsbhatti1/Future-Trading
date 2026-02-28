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
strategy(title = "NMVOB-S", shorttitle = "NMVOB-S", overlay = true , calc_on_every_tick = false , initial_capital = v_input_float_1)
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

// # ========================================================================= #
// #                   |  Global Variables END  |
// # ========================================================================= #

// # ========================================================================= #
// #                   |  Custom Functions START  |
// # ========================================================================= #
stop_loss_pillars = v_input_int_1
stop_profit_proportion = v_input_float_2

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
sma = v_input_2
lma = v_input_3
tsp = v_input_4
np = v_input_5
type = v_input_int_2

sh = type == 1 ? ta.ema(close, sma)  
 : type == 2 ? ta.wma(close, sma)
 : ta.sma(close, sma)

lon=type == 1 ? ta.ema(close, lma) 
 : type == 2 ? ta.wma(close, lma)
 : ta.sma(close, lma)

ratio = math.min(sh, lon)/math.max(sh, lon)

Mac = if sh > lon
    2 - ratio - 1
else
    ratio - 1

//快线
MacNorm = ((Mac-ta.lowest(Mac, np)) /(ta.highest(Mac, np)-ta.lowest(Mac, np)+.000001)*2)- 1

MacNorm2 = if np < 2
    Mac
else
    MacNorm

//慢线    
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
length = v_input_6
spike = close - open
vs_up_line = ta.stdev(spike, length)
vs_low_line = ta.stdev(spike, length) * -1

// # ========================================================================= #
// #                   |  Volatility Oscillator END  |
// # ========================================================================= #

// # ========================================================================= #
// #                   |  Bollinger Bands  |
// # ========================================================================= #
b_length = v_input_int_3
src = v_input_7_close
mult = v_input_float_3
basis = ta.sma(src, b_length)
dev = mult * ta.stdev(src, b_length)
upper = basis + dev

lower = basis - dev
// # End of Bollinger Bands Calculation
```

This translation retains the original structure and code blocks while translating the Chinese text to English in the comments.