<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

ATR Adjustable Trailing Stop Loss Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/a11fe258364185305a.png)

[trans]


This strategy uses the ATR indicator to calculate a dynamic stop loss line for risk control purposes.

#### Overview

This strategy employs the ATR indicator to compute a dynamic stop-loss line. As prices rise, the stop-loss line adjusts upward accordingly, locking in profits. When prices decline, the stop-loss line remains unchanged, preventing premature exits. The ATR indicator measures market volatility and risk; when multiplied by a coefficient, it generates a stop-loss line that controls the risk exposure of each trade.

#### Principle

The strategy combines the ATR indicator with the Highest function to calculate a dynamic stop-loss line. The specific calculation formula is as follows:

```pine
TS=highest(high-Mult*atr(Atr),Hhv)
```

Here, Atr represents the ATR period parameter, Hhv denotes the lookback period for the Highest function, and Mult is the ATR multiplier.

The idea behind this formula is to first calculate the ATR value, then multiply it by the coefficient Mult to determine the buffer range for the stop loss. Next, the Highest function identifies the highest price over the past Hhv periods, from which the stop-loss buffer range is subtracted to derive the dynamic stop-loss line TS.

As prices increase, new highs are continually reached, causing the stop-loss line to move upward and secure profits. During price declines, the stop-loss line maintains its prior high level, avoiding unnecessary exits.

#### Advantages

1. **Dynamic Stop-Loss for Timely Profit Locking**

   The stop-loss line in this strategy adjusts dynamically, tracking the highest points following price increases to promptly lock in gains. This offers an advantage over static stop-loss mechanisms.

2. **Avoidance of Unnecessary Stop-Outs**

   Fixed stop-loss levels can easily trigger during normal market retracements or overly tight stops. This strategy keeps the stop-loss line constant during price drops, preventing unwarranted exits.

3. **Adjustable Stop-Loss Magnitude**

   By adjusting the ATR period and multiplier parameters, the sensitivity of the stop-loss adjustments can be controlled, enabling varying degrees of stop-loss behavior.

4. **Controllable Risk Exposure**

   Since the stop-loss range is calculated dynamically using ATR, it allows setting appropriate stop-loss levels based on market volatility, thereby managing the risk per trade effectively.

#### Risks

1. **Overly Aggressive Stop-Loss During High Volatility**

   In highly volatile markets, ATR can surge rapidly, pushing the stop-loss line up quickly and increasing the likelihood of unnecessary stop-outs. Adjusting the ATR period parameter appropriately can help mitigate this sensitivity.

2. **Difficulty Adapting to Sharp Reversals**

   The strategy struggles with significant market reversals, where the stop-loss line might lag excessively. In such cases, reducing positions promptly is advisable to manage risk.

3. **Parameter Optimization Challenges**

   Optimizing the ATR period, Highest lookback period, and multiplier requires comprehensive tuning, which can be complex. Using stepped optimization methods with multiple combinations is recommended.

#### Optimization Directions

1. **Optimize ATR Period Parameter**

   Increasing the ATR period can reduce overly frequent adjustments of the stop-loss line but may result in larger losses per trade.

2. **Optimize Highest Period Parameter**

   Increasing the Highest period parameter makes the stop-loss line more stable, though it requires balancing with tracking responsiveness.

3. **Test Different ATR Multipliers**

   Select suitable ATR multipliers based on the characteristics of different instruments. Higher multipliers widen the stop-loss range, while lower ones reduce potential losses per trade.

4. **Combine with Trend Indicators**

   Incorporating trend indicators for auxiliary decision-making can reduce the probability of stop-loss triggers due to reversals.

#### Conclusion

Overall, this strategy features dynamic stop-loss capabilities and controllable risk, making it suitable for trending markets. However, vigilance is required regarding risks from sudden market volatility, and parameter optimization poses challenges. With proper parameter configuration, optimization, and supplementary technical analysis, this strategy can be effectively deployed in live trading.
||

This strategy uses the ATR indicator to calculate a dynamic stop loss line for risk control.

#### Overview 

The strategy uses the ATR indicator to calculate a dynamic stop loss line. When prices rise, the stop loss line will move up with prices to lock in profits. When prices fall, the stop loss line remains unchanged to avoid being stopped out. The ATR indicator can measure market volatility and risk. Multiplying it by a coefficient generates the stop loss line, thus controlling the risk exposure per trade.

#### Principles

The strategy uses the ATR indicator and Highest function to calculate the dynamic stop loss line. The specific formula is:

```pine
TS=highest(high-Mult*atr(Atr),Hhv) 
```

Where Atr is the ATR period parameter, Hhv is the lookback period parameter of the Highest function, and Mult is the ATR coefficient.

The logic is to first calculate the ATR value, then multiply it by the Mult coefficient to get the range of the stop loss buffer zone. Then use the Highest function to find the highest high in the past Hhv periods, and subtract the stop loss buffer zone to obtain the dynamic stop loss line TS.

When prices rise, the highest high will be constantly updated, driving the stop loss line to move up and locking in profits. When prices fall, the stop loss line will maintain the previous high point to avoid being stopped out.

#### Advantages

1. Dynamic stop loss for timely profit taking

The stop loss line adjusts dynamically to track the highest point after price rises, allowing timely profit taking. This is superior to fixed stop loss.

2. Avoid unnecessary stop loss

Fixed stop loss lines can easily be triggered by normal pullbacks or overtight stops. This strategy keeps the stop loss unchanged during price declines to avoid unnecessary stops.

3. Adjustable stop loss range 

By tuning the ATR period and multiplier parameters, the sensitivity of the stop loss adjustment can be controlled for different degrees of stops.

4. Controllable risk

The ATR dynamically calculates the stop loss range, allowing reasonable stop loss ranges according to market volatility for risk control per trade.

#### Risks

1. Stop loss too aggressive during high volatility

When volatility spikes, ATR rises quickly and drives the stop loss line up rapidly, increasing the chance of unnecessary stops. The ATR period can be adjusted to make the line less sensitive.

2. Difficult to adapt to sharp reversals

The strategy struggles to adapt to sharp reversals. The stop loss line may lag too much and needs timely position reduction.

3. Difficult optimization

Optimizing the ATR period, Highest period and multiplier parameters together can be challenging. Stepped parameter sweep testing is recommended.

#### Optimization

1. Optimize ATR Period

Increase ATR period to reduce overly frequent stop line adjustment, but at the cost of larger loss per stop.

2. Optimize Highest Period

Increase Highest period to make the line more stable, but balance tracking speed.

3. Test different ATR coefficients

Choose proper ATR multipliers according to instrument characteristics. Larger multipliers widen stops, smaller ones decrease loss per stop.

4. Add trend filter

Adding a trend filter reduces the chance of stops being triggered by reversals.

#### Summary

The strategy has the advantage of dynamic stops and controllable risks. It fits trending markets but watch out for volatility spikes and difficult parameter optimization. With proper settings, optimization and additional techniques, it can be applied for live trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|5|Atr Period|
|v_input_2|10|HHV Period|
|v_input_3|2.5|Multiplier|
|v_input_4|true|Barcolor|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-17 00:00:00
end: 2023-10-24 00:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ceyhun

//@version=4
strategy("ATR Trailing Stoploss Strategy ",overlay=true)

Atr=input(defval=5,title="Atr Period",minval=1,maxval=500)
Hhv=input(defval=10,title="HHV Period",minval=1,maxval=500)
Mult=input(defval=2.5,title="Multiplier",minval=0.1)
Barcolor=input(true,title="Barcolor")

TS=highest(high-Mult*atr(Atr),Hhv),barssince(close>highest(high-Mult*atr(Atr),Hhv) and close>close)
Color=iff(close>TS,color.green,iff(close<TS,color.red,color.black))
barcolor(Barcolor? Color:na)

plot(TS,color=Color,linewidth=3,title="ATR Trailing Stoploss")

Buy  = crossover(close,TS)
Sell = crossunder(close,TS)

if Buy
    strategy.entry("Buy", strategy.long, comment="Buy")
    
if Sell
    strategy.entry("Sell", strategy.short, comment="Sell")
```

> Detail

https://www.fmz.com/strategy/430150

> Last Modified

2023-10-25 15:08:04