> Name

ZigZag-PA-Strategy-V41

> Author

ChaoZhang

> Strategy Description

EXPERIMENTAL:
WARNING: this strategy repaints after reloading and results are heavily curve fitted, use at your own discretion.
UPDATE: (AleksanderThor) add option for a 2nd target, to use you need to activate pyramiding with a setting of 1 manually (not possible to change programatically).

**backtest**

 ![IMG](https://www.fmz.com/upload/asset/f6c9860b59b6177205.png) 

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|false|Use Heikken Ashi Candles|
|v_input_2|true|Use Alt Timeframe|
|v_input_3|60|Alt Timeframe|
|v_input_4|true|Show Patterns|
|v_input_5|true|Display Fibonacci 0.000:|
|v_input_6|true|Display Fibonacci 0.236:|
|v_input_7|true|Display Fibonacci 0.382:|
|v_input_8|true|Display Fibonacci 0.500:|
|v_input_9|true|Display Fibonacci 0.618:|
|v_input_10|true|Display Fibonacci 0.764:|
|v_input_11|true|Display Fibonacci 1.000:|
|v_input_12|10000|Target 1 - Trade size:|
|v_input_13|0.236|Target 1 - Fib. Rate to use for Entry Window:|
|v_input_14|0.618|Target 1 - Fib. Rate to use for TP:|
|v_input_15|-0.236|Target 1 - Fib. Rate to use for SL:|
|v_input_16|false|Target 2 - Active?|
|v_input_17|10000|Target 2 - Trade size:|
|v_input_18|0.236|Target 2 - Fib. Rate to use for Entry Window:|
|v_input_19|1.618|Target 2 - Fib. Rate to use for TP:|
|v_input_20|-0.236|Target 2 - Fib. Rate to use for SL:|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-04-24 00:00
end: 2022-05-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// https://cn.tradingview.com/script/NEDEDcsP-STRATEGY-RS-ZigZag-PA-Strategy-V4-1/
//@version=4
strategy(title='[STRATEGY][RS]ZigZag PA Strategy V4.1', shorttitle='S', overlay=true, pyramiding=0, initial_capital=100000, currency=currency.USD)
useHA = input(false, title='Use Heikken Ashi Candles')
useAltTF = input(true, title='Use Alt Timeframe')
tf = input('60', title='Alt Timeframe')
showPatterns = input(true, title='Show Patterns')
showFib0000 = input(title='Display Fibonacci 0.000:', type=bool, defval=true)
showFib0236 = input(title='Display Fibonacci 0.236:', type=bool, defval=true)
showFib0382 = input(title='Display Fibonacci 0.382:', type=bool, defval=true)
showFib0500 = input(title='Display Fibonacci 0.500:', type=bool, defval=true)
showFib0618 = input(title='Display Fibonacci 0.618:', type=bool, defval=true)
showFib0764 = input(title='Display Fibonacci 0.764:', type=bool, defval=true)
showFib1000 = input(title='Display Fibonacci 1.000:', type=bool, defval=true)
zigzag() =>
    _isUp = close >= open
    _isDown = close <= open
    _direction = na
    _direction := _isUp[1] and _isDown ? -1 : _isDown[1] and _isUp ? 1 : nz(_direction[1])
    _zigzag = _isUp[1] and _isDown and _direction[1] != -1 ? highest(2) : _isDown[1] and _isUp and _direction[1] != 1 ? lowest(2) : na

_ticker = useHA ? heikenashi(tickerid) : syminfo.tickerid
sz = useAltTF ? (ta.change(time(tf)) != 0 ? request.security(_ticker, tf, zigzag()) : na) : zigzag()

plot(sz, title='zigzag', color=black, linewidth=2)

//  ||---   Pattern Recognition:

x = valuewhen(sz, sz, 4) 
a = valuewhen(sz, sz, 3) 
b = valuewhen(sz, sz, 2) 
c = valuewhen(sz, sz, 1) 
d = valuewhen(sz, sz, 0)

xab = (abs(b-a)/abs(x-a))
xad = (abs(a-d)/abs(x-a))
abc = (abs(b-c)/abs(a-b))
bcd = (abs(c-d)/abs(b-c))

//  ||-->   Functions:
isBat(_mode)=>
    _xab = xab >= 0.382 and xab <= 0.5
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.618 and bcd <= 2.618
    _xad = xad <= 0.618 and xad <= 1.000    // 0.886
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isGartley(_mode)=>
    _xab = xab >= 0.5 and xab <= 0.618 // 0.618
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.13 and bcd <= 2.618
    _xad = xad >= 0.75 and xad <= 0.875 // 0.786
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isCrab(_mode)=>
    _xab = xab >= 0.500 and xab <= 0.875    // 0.886
    _abc = abc >= 0.382 and abc <= 0.886    
    _bcd = bcd >= 2.000 and bcd <= 5.000    // 3.618
    _xad = xad >= 1.382 and xad <= 5.000    // 1.618
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiGartley(_mode)=>
    _xab = xab >= 0.500 and xab <= 0.886    // 0.618 -> 0.786
    _abc = abc >= 1.000 and abc <= 2.618    // 1.130 -> 2.618
    _bcd = bcd >= 1.500 and bcd <= 5.000    // 1.618
    _xad = xad >= 1.000 and xad <= 5.000    // 1.272
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiCrab(_mode)=>
    _xab = xab >= 0.250 and xab <= 0.500    // 0.276 -> 0.446
    _abc = abc >= 1.130 and abc <= 2.618    // 1.130 -> 2.618
    _bcd = bcd >= 1.618 and bcd <= 2.618
``` 

Note: The function definitions for `isAntiCrab` were cut off at the end of the provided text, so they are not fully included in this translation. If you need these functions completed, please provide the full code snippet or additional information.