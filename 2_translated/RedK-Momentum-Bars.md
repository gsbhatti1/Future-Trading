> Name

RedK-Momentum-Bars

> Author

ChaoZhang

> Strategy Description

Momentum Bars (Mo_Bars) offers a different way to visualize (relative) momentum—using some simple TA concepts to provide a new perspective on how we read momentum changes and incorporate them into our trading.

The idea here (and the script itself) is really super simple, and is (very loosely) inspired by Elder's Impulse System (EIS), then evolved to leverage other concepts and become less cluttered and "easier to read".

Construction of Mo_Bars
-----------------------
The base concept utilizes 3 moving average lines:
- The first line is a relatively fast MA with a short length—acts as the main price tracking line.
- The second line is slightly slower than the main line—2 to 3 bars longer in length—and will by default use the open value as the source. This works better to identify when the closing price starts to move faster than the open (as in, bars more frequently close higher than they open). This line acts as the signal line. There's an added setting for an additional delay that utilizes regular WMA smoothing—the delay acts to magnify the relative displacement between the 2 MAs.
- For both these MA's, I choose to use the RSS MA (Lazy Line)—other MA types can be used, but the reason I used that MA type specifically is that it moves "gracefully"—and two Lazy Lines moving together minimize whipsaws from small price swings—I tested with other MA types and found that the RSS has an advantage there.

The third line is a much slower MA (length 5 to 6 times the fast line)—and acts as a filter or baseline. When we're above that line, we should favor long positions—we're in bull territory. When we're below that line, we favor short positions—and we're in bear territory. Adjust this line as it suits your trading style and time frame.
(I choose to use WMA as the MA type for the filter line … and there's a good reason for that—which I'll skip for now—but in future versions, we can add other selectable MA types.)

Using Mo_Bars
--------------
At a very broad level, we can use Mo_Bars similar to how we use a MACD—both are centered and unrestricted oscillators. Note the difference that Mo_Bars is based on 3 MAs rather than 2.

The Mo_Bar bar length reflects the distance between the main MA and the signal MA—plotted relative to the baseline (filter line)—that means that the length of the bar represents the relative momentum between the 2 MAs. The Mo_Bars are then colored in a way that reflects an increase or decrease in the value of that momentum (the visual here may have been inspired by another indicator recently published by one of our esteemed wizards—it worked perfectly—so due credits here :)

- In simple terms, if the main MA is below the signal MA, the bar is red—and when the main MA is above the signal MA, the bar is green. A white bar usually shows up when there's a detected change in the relative momentum direction (note that this is not the same as the trend direction—and that’s what helps show and exploit convergence and divergence—similar to a MACD).

- In the chart above, I noted few examples of how visualizing relative momentum in this way exposes areas of chop (Mo_Bars above zero but are in red or moving down, or when Mo_Bars are below zero and green or moving up)—convergence / divergence with price—and how this can act to expose the possibility of potential changes in price action or trend.

- There's so much more to play around with this setup—and maybe if there's enough interest there can be future dedicated posts on how utilize or even to evolve it further. There’s a lot of potential here, to add more filters (maybe volume based), alerts, signals…etc—so let's see the interest :)


Here’s the detailed (top chart) setup that Mo_Bars is based on—the settings for the MAs on the price charts have been matched/sync’d with the Mo_Bars settings on the lower panel to demonstrate how the script works and how it translates the MA action on the price chart to what we see below.

**Backtest**
![IMG](https://www.fmz.com/upload/asset/9c35dab96de1e2b43f.png)

> Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|v_input_source_1_close|0|Fast MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|10|Length|
|v_input_string_1|0|Type: SMA|WMA|EMA|RSS_WMA|HMA|
|v_input_source_2_close|0|Slow MA Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_2|20|Length|
|v_input_string_2|0|Type: SMA|WMA|EMA|RSS_WMA|HMA|
|v_input_int_3|3|Delay (1 = None)|
|v_input_int_4|50|Filter MA Length|
|v_input_string_3|0|Type: SMA|WMA|EMA|RSS_WMA|HMA|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-05-10 00:00:00
end: 2022-05-16 23:59:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © RedKTrader

//@version=5
indicator('[dev]RedK Momentum Bars', shorttitle='RedK MoBars v3.0', explicit_plot_zorder = true, timeframe='', timeframe_gaps=false)

// A trading system composed of 2 short Lazy Lines (preferably one open and one close - 2-3 bars apart) and a WMA long filter 
// loosely inspired by Edler Impulse
// v2.0 cleaned up code and added MA options to be able to mix and match, and experiment with various setups 
// default values (my personal preference) remain the same as in v1.0 
// for example, some traders will consider "bear territory" only below SMA50, others will use EMA30 .. and so on.
// ---------------------------------------------------------------------------------------------------------------
// MoBars v3.0: 
// updated defaults to match the most common 3x MA cross-over set-up of SMA (10, 20, 50)
// updated visuals to push the 0 line to the background of the plot (using the explcit_plot_zorder param)
// and added a
```