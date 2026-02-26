``` pinescript
/*backtest
start: 2023-09-04 00:00:00
end: 2023-09-11 00:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
// Copyright nilux: https://www.tradingview.com/u/nilux/
// Based on the original of dasanc: https://www.tradingview.com/u/dasanc/

strategy("Enhanced Fish Net Strategy", "EFS Mod Backtest", default_qty_type = strategy.percent_of_equity, default_qty_value = 100, initial_capital = 100000, slippage = 5)
Price = input.source(close, "Source")
Length = input(20,"Period")
transform = input("Inphase-Quadrature","Use Transform?",options=["Hilbert","Inphase-Quadrature","False"])
min = input(108,"Min. Period")
buyTreshold = input(-2.41, title = "Buy Treshold (-)", type = float, defval=-2.0, minval = -2.50, maxval = -0.01, step = 0.01)
sellTreshold = input(2.43, title = "Sell Treshold (+)", type = float, defval=2.0, minval = 0.01, maxval = 2.50, step = 0.01)

// === SL and TP ===
fixedSL = input(title="SL Activation", defval=300)
trailSL = input(title="SL Trigger", defval=1)
fixedTP = input(title="TP Activation", defval=150)
trailTP = input(title="TP Trigger", defval=50)

// === BACKTEST RANGE ===
FromMonth = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
FromDay   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
FromYear  = input(defval = 2019, title = "From Year", minval = 2015)
ToMonth   = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
ToDay     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
ToYear    = input(defval = 9999, title = "To Year", minval = 2015)
start     = timestamp(FromYear, FromMonth, FromDay, 00, 00)
finish    = timestamp(ToYear, ToMonth, ToDay, 23, 59)
window()  => time >= start and time <= finish ? true : false

getIQ(src,min,max) =>
    PI = 3.14159265359
    P = src - src[7]
    lenIQ = 0.0
    lenC = 0.0
    imult = 0.635
    qmult = 0.338
    inphase = 0.0
    quadrature = 0.0
    re = 0.0
    im = 0.0
    deltaIQ = 0.0
    instIQ = 0.0
    V = 0.0
    
    inphase := 1.25*(P[4] - imult*P[2]) + imult*nz(inphase[3])
    quadrature := P[2] - qmult*P + qmult*nz(quadrature[2])
    re := 0.2*(inphase*inphase[1] + quadrature*quadrature[1]) + 0.8*nz(re[1])
    im := 0.2*(inphase*quadrature[1] - inphase[1]*quadrature) + 0.8*nz(im[1])
    if (re!= 0.0)
        deltaIQ := atan(im/re)
    for i=0 to max
        V := V + deltaIQ[i]
        if (V > 2*PI and instIQ == 0.0)
            instIQ := i
    if (instIQ == 0.0)
        instIQ := nz(instIQ[1])
    lenIQ := 0.25*instIQ + 0.75*nz(lenIQ[1],1)
    length = lenIQ<min ? min : lenIQ


getHT(src) =>
    Price = src
    Imult = .635
    Qmult = .338
    PI = 3.14159
    InPhase = 0.0
    Quadrature = 0.0
    Phase = 0.0
    DeltaPhase = 0.0
    InstPeriod = 0.0
    Period = 0.0
    Value4 = 
```