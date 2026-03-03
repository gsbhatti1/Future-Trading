> Name

ZigZag-Pattern-Recognition-Short-term-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1c7ac130c08e22119f3.png)
 [trans]
## Overview  

This strategy identifies candlestick patterns based on the ZigZag indicator and sets entry windows, take profit, and stop loss prices using Fibonacci retracements for short-term trading. The strategy supports 13 types of patterns for both long and short trends, including Bat, Butterfly, Gartley etc.

## Strategy Logic  

1. Identify potential reversal points using the ZigZag indicator
2. Calculate the most recent 4 reversal points and check if they match any of the 13 predefined patterns
3. Enter trade if a pattern is matched and price enters the Fibonacci 0.382 retracement area  
4. Set take profit to 0.618 retracement level, stop loss to -0.618 retracement level
5. Valid patterns include common ones like Bat, Butterfly, Gartley, as well as some reverse patterns such as Anti-Bat, Anti-Butterfly etc

## Advantage Analysis  

1. The ZigZag indicator effectively filters out market noise and identifies clearer trend reversal points  
2. Multiple patterns increase opportunities to enter trades while controlling risks
3. Fibonacci retracement levels standardize entry, take profit, and stop loss

## Risk Analysis  

1. The ZigZag indicator is sensitive to parameters, optimization is needed to find the best parameter combination  
2. Too many fitted patterns increase curve fitting risks, real trading performance may underperform backtest results  
3. Only the most recent 4 reversal points considered, more complex patterns are ignored
4. No re-test of retracement breakouts considered, may cause premature stop loss  

## Optimization Directions  

1. Optimize ZigZag parameters to find the best combination 
2. Add validity checks for patterns, e.g., confirmation of key points by closing prices
3. Expand pattern library to increase entry opportunities  
4. Add re-test mechanism of retracements to lower stop loss risks

## Conclusion  

This strategy identifies trend reversal points using the ZigZag indicator and candlestick patterns, and sets standardized entry/exit logic with Fibonacci retracement zones. With optimized parameters and adjusted stop loss mechanisms, it has the potential to achieve good real trading results. The key is finding the best parameter combinations and tuning stop losses accordingly.

[/trans]

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
|v_input_12|true|Trade size:|
|v_input_13|0.382|Fib. Rate to use for Entry Window:|
|v_input_14|0.618|Fib. Rate to use for TP:|
|v_input_15|-0.618|Fib. Rate to use for SL:|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title='[STRATEGY][RS]ZigZag PA Strategy V4', shorttitle='S', overlay=true)
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
    _direction = _isUp[1] and _isDown ? -1 : _isDown[1] and _isUp ? 1 : nz(_direction[1])
    _zigzag = _isUp[1] and _isDown and _direction[1] != -1 ? highest(2) : _isDown[1] and _isUp and _direction[1] != 1 ? lowest(2) : na

_ticker = useHA ? heikenashi(syminfo.tickerid) : syminfo.tickerid
sz = useAltTF ? (ta.change(time(tf)) != 0 ? request.security(_ticker, tf, zigzag()) : na) : zigzag()

plot(sz, title='zigzag', color=color.black, linewidth=2)

// Pattern Recognition:
x = ta.valuewhen(sz, sz, 4)
a = ta.valuewhen(sz, sz, 3)
b = ta.valuewhen(sz, sz, 2)
c = ta.valuewhen(sz, sz, 1)
d = ta.valuewhen(sz, sz, 0)

xab = (abs(b-a)/abs(x-a))
xad = (abs(a-d)/abs(x-a))
abc = (abs(b-c)/abs(a-b))
bcd = (abs(c-d)/abs(b-c))

// Functions:
isBat(_mode) =>
    _xab = xab >= 0.382 and xab <= 0.5
    _abc = abc >= 0.382 and abc <= 0.886
    _bcd = bcd >= 1.618
```