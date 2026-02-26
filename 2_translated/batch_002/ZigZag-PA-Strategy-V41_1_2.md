```pinescript
/*backtest
start: 2022-04-24 00:00:00
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

// ||---   Pattern Recognition:

x = valuewhen(sz, sz, 4)
a = valuewhen(sz, sz, 3)
b = valuewhen(sz, sz, 2)
c = valuewhen(sz, sz, 1)
d = valuewhen(sz, sz, 0)

xab = (abs(b-a)/abs(x-a))
xad = (abs(a-d)/abs(x-a))
abc = (abs(b-c)/abs(a-b))
bcd = (abs(c-d)/abs(b-c))

// ||-->   Functions:
isBat(_mode)=>
    _xab = xab >= 0.382 and xab <= 0.5
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.618 and bcd <= 2.618
    _xad = xad <= 0.618 and xad <= 1.000    // 0.886
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiBat(_mode)=>
    _xab = xab >= 0.500 and xab <= 0.886    // 0.618
    _abc = abc >= 1.000 and abc <= 2.618    // 1.13 --> 2.618
    _bcd = bcd >= 1.618 and bcd <= 2.618    // 2.0  --> 2.618
    _xad = xad >= 0.886 and xad <= 1.000    // 1.13
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAltBat(_mode)=>
    _xab = xab <= 0.382
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 2.0 and bcd <= 3.618
    _xad = xad <= 1.13
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isButterfly(_mode)=>
    _xab = xab <= 0.786
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.618 and bcd <= 2.618
    _xad = xad >= 1.27 and xad <= 1.618
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiButterfly(_mode)=>
    _xab = xab >= 0.236 and xab <= 0.886    // 0.382 - 0.618
    _abc = abc >= 1.130 and abc <= 2.618    // 1.130 - 2.618
    _bcd = bcd >= 1.000 and bcd <= 1.382    // 1.27
    _xad = xad >= 0.500 and xad <= 0.886    // 0.618 -> 0.786
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isCrab(_mode)=>
    _xab = xab >= 0.500 and xab <= 0.875    // 0.886
    _abc = abc >= 0.382 and abc <= 0.886    
    _bcd = bcd >= 2.000 and bcd <= 5.000    // 3.618
    _xad = xad >= 1.382 and xad <= 5.000    // 1.618
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiCrab(_mode)=>
    _xab = xab >= 0.250 and xab <= 0.500    // 0.276 -> 0.446
    _abc = abc >= 1.130 and abc <= 2.618    // 1.130 -> 2.618
    _bcd = bcd >= 1.618 and bcd <= 2.618    
    _xad = xad >= 1.000 and xad <= 5.000    // 1.272
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isGartley(_mode)=>
    _xab = xab >= 0.5 and xab <= 0.618 // 0.618
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.13 and bcd <= 2.618
    _xad = xad >= 0.75 and xad <= 0.875 // 0.786
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isAntiGartley(_mode)=>
    _xab = xab >= 0.500 and xab <= 0.886    // 0.618 -> 0.786
    _abc = abc >= 1.000 and abc <= 2.618    // 1.130 -> 2.618
    _bcd = bcd >= 1.500 and bcd <= 5.000    // 1.618
    _xad = xad >= 1.000 and xad <= 5.000    // 1.272
    _xab and _abc and _bcd and _xad and (_mode == 1 ? d < c : d > c)

isABCD(_mode)=>
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.13 and bcd <= 2.618
    _abc and _bcd and (_mode == 1 ? d < c : d > c)
```

This script should now accurately reflect the original content, including the backtest configuration parameters. Please ensure that all variable names and logic are correctly retained for functionality.