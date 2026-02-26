```pinescript
/*backtest
start: 2022-04-09 00:00:00
end: 2022-05-08 23:59:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © EltAlt

//@version=5

//  -----------------------------------------------------------------------------
//
//  Authors:  @EltAlt
//  Revision: v3.00
//  Date:     09-May-2022
//
//  Description
//  =============================================================================
//  This indicator displays the Moving Average Convergence and Divergence (MACD) of individually configured Fast, Slow and Signal Moving Averages.
//  Buy and sell alerts can be set based on moving average crossovers, consecutive convergence/divergence of the moving averages,
//  and directional changes in the histogram moving averages. 
//
//  The Fast, Slow and Signal Moving Averages can be set to:
//  Exponential Moving Average (EMA)
//  Volume-Weighted Moving Average (VWMA)
//  Simple Moving Average (SMA)
//  Weighted Moving Average (WMA)
//  Hull Moving Average (HMA)
//  Exponentially Weighted Moving Average (RMA) (SMMA)
//  Symmetrically Weighted Moving Average (SWMA)
//  Arnaud Legoux Moving Average (ALMA)
//  Double EMA (DEMA)
//  Double SMA (DSMA)
//  Double WMA (DWMA)
//  Double RMA (DRMA)
//  Triple EMA (TEMA)
//  Triple SMA (TSMA)
//  Triple WMA (TWMA)
//  Triple RMA (TRMA)
//  Linear regression curve Moving Average (LSMA)
//  Variable Index Dynamic Average (VIDYA)
//  Fractal Adaptive Moving Average (FRAMA)

if you have a strategy that can buy based on External Indicators use 'Backtest Signal' which returns a 1 for a Buy and a 2 for a sell.
'Backtest Signal' is plotted to display none, so change the Style Settings for the chart if you need to see it for testing.

**backtest**

![IMG](https://www.fmz.com/upload/asset/430e6d9ce16dd5530d.png)

> Strategy Arguments

| Argument  | Default | Description |
|-----------|---------|-------------|
| v_input_string_1 | 0 | (Moving Averages) Fast Moving Average Type: EMA|SMA|WMA|VWMA|HMA|RMA|LSMA|Double EMA|Double SMA|Double WMA|Double RMA|Triple EMA|Triple SMA|Triple WMA|Triple RMA|SWMA|ALMA|VIDYA|FRAMA |
| v_input_1_close | 0 | Fast Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
| v_input_int_1 | 12 | Fast Length |
| v_input_string_2 | 0 | Slow Moving Average Type: SMA|EMA|WMA|VWMA|HMA|RMA|LSMA|Double EMA|Double SMA|Double WMA|Double RMA|Triple EMA|Triple SMA|Triple WMA|Triple RMA|SWMA|ALMA|VIDYA|FRAMA |
| v_input_2_close | 0 | Slow Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
| v_input_int_2 | 26 | Slow Length |
| v_input_string_3 | 0 | Signal Moving Average Type: SMA|EMA|WMA|VWMA|HMA|RMA|LSMA|Double EMA|Double SMA|Double WMA|Double RMA|Triple EMA|Triple SMA|Triple WMA|Triple RMA|SWMA|ALMA|VIDYA|FRAMA |
| v_input_int_3 | 9 | Signal Length |
| v_input_3 | 0.85 | (Alma) ALMA Offset |
| v_input_float_1 | 6 | ALMA Sigma |
| v_input_int_4 | true | (Frama) FRAMA lower shift limit (FC) |
| v_input_int_5 | 198 | FRAMA upper shift limit (SC) |
| v_input_bool_1 | true | (Buy / Sell Moving Averages) Buy Moving Average Crossover |
| v_input_bool_2 | true | Sell Moving Average Crossover |
| v_input_bool_3 | false | Buy Moving Average Crossing Zero |
| v_input_bool_4 | false | Sell Moving Average Crossing Zero |
| v_input_bool_5 | false | (Buy / Sell Histogram Moving Averages) Buy Histogram MA Positive |
| v_input_bool_6 | false | Sell Histogram MA Negative |
| v_input_int_6 | 5 | Histogram MA Length |
| v_input_string_4 | 0 | Histogram MA Type: EMA|VWMA|SMA|WMA|HMA|RMA|ALMA|Double EMA|Double SMA|Double WMA|Double RMA|Triple EMA|Triple SMA|Triple WMA|Triple RMA|LSMA|VIDYA|FRAMA |
| v_input_bool_7 | false | (Buy / Sell Histogram Rising / Falling) Buy MA Histogram Rising |
| v_input_bool_8 | false | Buy Histogram Rising Only Below Zero |
| v_input_int_7 | true | Consecutive Rising Bars to Trigger Buy |
| v_input_bool_9 | false | Sell MA Histogram Falling |
| v_input_bool_10 | false | Sell Histogram Falling Only Above Zero |
| v_input_int_8 | true | Consecutive Falling Bars to Trigger Sell |
| v_input_bool_11 | true | (Long / Short Signals) Generate Close Signals for Long / Short Positions |
| v_input_int_9 | true | Open Long = |
| v_input_int_10 | 2 | Close Long = |
| v_input_int_11 | -1 | Open Short = |
| v_input_int_12 | -2 | Close Short = |
| v_input_bool_12 | true | (Plot Options) Plot Alerts |
| v_input_bool_13 | true | Plot Moving Average |
| v_input_bool_14 | true | Plot Signal |
| v_input_bool_15 | true | Plot Histogram |
| v_input_bool_16 | true | Plot Histogram Moving Average |
| v_input_4 | #2962FF | (Color Settings) MACD Line |
| v_input_5 | #FF6D00 | Signal Line |
| v_input_6 | #26A69A | Histogram Above Grow |
| v_input_7 | #B2DFDB | Fall |
| v_input_8 | #FFCDD2 | Histogram Below Grow |
| v_input_9 | #FF5252 | Fall |

```