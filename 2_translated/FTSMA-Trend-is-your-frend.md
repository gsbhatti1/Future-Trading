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
smoothinput = input('EMA', title = "MA Type", options=['EMA', 'SMA', 'ALMA','FRAMA','RMA', 'SWMA', 'VWMA','WMA','LinearRegression'])
linearReg=input(false, "Use linear regression?")
linregLenght=input(13, "Linear regression lenght")
linregOffset=input(0, "Linear regression offset")

// ------ FRAMA ma ---------
ma(src, len) =>
    float result = 0
    int len1 = len / 2
    frama_SC=200
    frama_FC=1
    e = 2.7182818284590452353602874713527
    w = log(2/(frama_SC+1)) / log(e) // Natural logarithm (ln(2/(SC+1))) workaround
    H1 = highest(high, len1)
    L1 = lowest(low, len1)
    N1 = (H1-L1)/len1
    H2_ = highest(high, len1)
    H2 = H2_[len1]
    L2_ = lowest(low, len1)
    L2 = L2_[len1]
    N2 = (H2-L2)/len1
    H3 = highest(high, len)
    L3 = lowest(low, len)
    N3 = (H3-L3)/len
    dimen1 = (log(N1+N2)-log(N3))/log(2)
    dimen = iff(N1>0 and N2>0 and N3>0, dimen1, nz(dimen1[1]))
    alpha1 = exp(w*(dimen-1))
    oldalpha = alpha1 > 1 ? 1 : (alpha1 < 0.01 ? 0.01 : alpha1)
    oldN = (2 - oldalpha) / oldalpha
    N = (((frama_SC-frama_FC)*(oldN-1))/(frama_SC-1)) + frama_FC
    alpha_ = 2/(N+1)
    alpha = alpha_<2/(frama_SC+1) ? 2/(frama_SC+1) : (alpha_>1 ? 1 : alpha_)
    frama = 0.0
    frama := (1-alpha)*nz(frama[1]) + alpha*src
    result := frama
    result

// ---------- MA calculation - ChartArt and modified by 03.freeman-------------
calc_ma(src,l) => 
    _ma = smoothinput=='SMA' ? sma(src, l) : smoothinput=='EMA' ? ema(src, l) : smoothinput=='WMA' ? wma(src, l) : smoothinput=='LinearRegression' ? linreg(src, l,0) : smoothinput=='VWMA' ? vwma(src,l) : smoothinput=='RMA' ? rma(src, l) : smoothinput=='ALMA' ? alma(src,l,0.85,6) : smoothinput=='SWMA' ? swma(src) : smoothinput=='FRAMA' ? ma(sma(src,1),l) : na

//-----------------------------------------------

// pi = acos(-1)
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

// --- Thanks to xyse ---- https://www.tradingview.com/script/UTPOoabQ-Low-Frequency-Fourier-Transform/
// Declaration of user-defined variables
N = input(defval=64, title="Lookback Period", type=
```