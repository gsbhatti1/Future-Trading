```plaintext
Name

FTSMA-Trend-is-your-friend

Author

ChaoZhang

Strategy Description

This is my new solid strategy: if you believe that "TREND IS YOUR FRIEND" this is for you!

I have tested with many pairs and at many timeframes and have profit with just minor changes in settings.
I suggest to use it for intraday trading.

VERY IMPORTANT NOTE: this is a trend following strategy, so the target is to stay in the trade as much as possible. If your trading style is more focused on scalping and/or pullbacks, this strategy is not for you.

This strategy uses moving averages applied to Fourier waves for forecasting trend direction.

How the strategy works:
- Buy when fast MA is above mid MA and price is above slow MA, which acts as a trend indicator.
- Sell when fast MA is below mid MA and price is below slow MA, which acts as a trend indicator.

The strategy uses a lot of pyramiding orders because when you are in a flat market phase it will close 1 or 2 orders with a loss, but when a big trend starts, it will have profit in a lot of orders.
So, if you analyze carefully the strategy results, you will note that "Percent Profitable" is very low (30% in this case) because the strategy opened a lot of orders also in flat markets with small losses, BUT "Avg # bars in winning trades" is very high and overall Profit is very high: when a big trend starts, orders are kept open for long time generating big profits.

Thanks to all pinescripters mentioned in the code for their snippets.

I have also a study with alerts. Next improvement (only to whom is interested in this script and follows me): study with alerts on multiple tickers all at once. Leave a comment if you want to have access to the study.

HOW TO USE STRATEGY AND STUDY TOGETHER:
1- Add to chart the strategy first, so your workspace will be as clean as possible.
2- Open the Strategy Tester tab at footer of the page.
3- Modify settings to get best results (Profit, Profit Factor, Drawdown).
4- Add study with alerts to your chart with same setting of strategy.
I WILL PROVIDE A DETAILED QUICK INSTALLATION GUIDE WITH THE STUDY!

**Backtest**

![](https://www.fmz.com/upload/asset/1b7ceae2fe73402c7c1.png)

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1_close | 0 | Source: close, high, low, open, hl2, hlc3, hlcc4, ohlc4 |
| v_input_2 | 200 | Slow MA period |
| v_input_3 | 20 | Mid MA period |
| v_input_4 | 5 | Fast MA period |
| v_input_5 | true | Use MA |
| v_input_6 | true | First sinusoid |
| v_input_7 | 2 | Second sinusoid |
| v_input_8 | 3 | Third sinusoid |
| v_input_9 | 0 | MA Type: EMA, SMA, ALMA, FRAMA, RMA, SWMA, VWMA, WMA, LinearRegression |
| v_input_10 | false | Use linear regression? |
| v_input_11 | 13 | Linear regression length |
| v_input_12 | false | Linear regression offset |
| v_input_13 | 0 | Lookback Period: 64, 4, 8, 16, 32, 2, 128, 256, 512, 1024, 2048, 4096 |
| v_input_14 | false | Take Profit Points |
| v_input_15 | false | Stop Loss Points |
| v_input_16 | false | Trailing Stop Loss Points |
| v_input_17 | false | Trailing Stop Loss Offset Points |

> Source (PineScript)

```pinescript
/* backtest
start: 2022-04-25 00:00:00
end: 2022-05-24 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © 03.freeman

//@version=4
strategy("FTSMA", overlay=true, precision=6, initial_capital=10000, calc_on_every_tick=true, pyramiding=10, default_qty_type=strategy.fixed, default_qty_value=10000, currency=currency.EUR)
src=input(close,"Source")
slowMA=input(200,"Slow MA period")
mediumMA=input(20,"Mid MA period")
fastMA=input(5,"Fast MA period")
plotSMA=input(true,"Use MA")
sin1=input(1,"First sinusoid",minval=1)
sin2=input(2,"Second sinusoid",minval=1)
sin3=input(3,"Third sinusoid",minval=1)
smoothinput = input('EMA', title="MA Type", options=['EMA', 'SMA', 'ALMA','FRAMA','RMA', 'SWMA', 'VWMA','WMA','LinearRegression'])
linearReg=input(false, "Use linear regression?")
linregLenght=input(13, "Linear regression length")
linregOffset=input(0, "Linear regression offset")

//------FRAMA ma---------
ma(src, len) =>
    float result = 0
    int len1 = len/2
    frama_SC=200
    frama_FC=1
    e = 2.7182818284590452353602874713527
    w = log(2/(frama_SC+1)) / log(e) // Natural logarithm (ln(2/(SC+1))) workaround
    H1 = highest(high,len1)
    L1 = lowest(low,len1)
    N1 = (H1-L1)/len1
    H2_ = highest(high,len1)
    H2 = H2_[len1]
    L2_ = lowest(low,len1)
    L2 = L2_[len1]
    N2 = (H2-L2)/len1
    H3 = highest(high,len)
    L3 = lowest(low,len)
    N3 = (H3-L3)/len
    dimen1 = (log(N1+N2)-log(N3))/log(2)
    dimen = iff(N1>0 and N2>0 and N3>0,dimen1,nz(dimen1[1]))
    alpha1 = exp(w*(dimen-1))
    oldalpha = alpha1>1?1:(alpha1<0.01?0.01:alpha1)
    oldN = (2-oldalpha)/oldalpha
    N = (((frama_SC-frama_FC)*(oldN-1))/(frama_SC-1))+frama_FC
    alpha_ = 2/(N+1)
    alpha = alpha_<2/(frama_SC+1)?2/(frama_SC+1):(alpha_>1?1:alpha_)
    frama = 0.0
    frama :=(1-alpha)*nz(frama[1]) + alpha*src
    result := frama
    result

// ----------MA calculation - ChartArt and modified by 03.freeman-------------
calc_ma(src,l) => 
    _ma = smoothinput=='SMA'?sma(src, l):smoothinput=='EMA'?ema(src, l):smoothinput=='WMA'?wma(src, l):smoothinput=='LinearRegression'?linreg(src, l,0):smoothinput=='VWMA'?vwma(src,l):smoothinput=='RMA'?rma(src, l):smoothinput=='ALMA'?alma(src,l,0.85,6):smoothinput=='SWMA'?swma(src):smoothinput=='FRAMA'?ma(sma(src,1),l):na
    
//----------------------------------------------

//pi = acos(-1)
// Approximation of Pi in _n terms --- thanks to e2e4mfck
f_pi(_n) =>
    _a = 1. / (4. * _n + 2)
    _b = 1. / (6. * _n + 3)
    _pi = 0.
    for _i = _n - 1 to 0
        _a := 1 / (4. * _i + 2) - _a / 4.
        _b := 1 / (6. * _i + 3) - _b / 9.
    _pi := (4. * _a) + (4. * _b) - _pi
pi=f_pi(20)

//---Thanks to xyse----https://www.tradingview.com/script/UTPOoabQ-Low-Frequency-Fourier-Transform/
//Declaration of user-defined variables
N = input(defval=64, title="Lookback Period", typ
```