``` pinescript
/*backtest
start: 2022-04-25 00:00:00
end: 2022-05-24 23:59:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
indicator(title='EMA RSI ADX Scalping Alerts', shorttitle="ERA Scalper", overlay=true)

// Define MA Inputs and group them
maType = input.string(title="MA Type", options=["EMA", "SMA", "WMA", "VWMA", "HMA", "RMA", "DEMA", "TEMA", "LSMA", "ZLSMA"], defval="EMA", group='MA Settings')
emaSource = input.source(title='MA Source', defval=close, group='MA Settings')
emaLength = input.int(title='MA Length', defval=50, minval=1, maxval=999, group='MA Settings')

// Other Moving Avarage Calculations
e1 = ta.ema(emaSource, emaLength)
e2 = ta.ema(e1, emaLength)
dema = 2 * e1 - e2

ema1 = ta.ema(emaSource, emaLength)
ema2 = ta.ema(ema1, emaLength)
ema3 = ta.ema(ema2, emaLength)
tema = 3 * (ema1 - ema2) + ema3

lsmaOffset = input.int(title="LSMA Offset", defval=0, minval=0, maxval=100, tooltip='Only used if you choose the LSMA and ZLSMA(Zero Lag LSMA) Option between MA Types', group='MA Settings')
lsma = ta.linreg(emaSource, emaLength, lsmaOffset)
lsma2 = ta.linreg(lsma, emaLength, lsmaOffset)
eq = lsma-lsma2
zlsma = lsma+eq

// Switch between different MA Types
emaValue = switch maType
    "EMA" => ta.ema(emaSource, emaLength)
    "SMA" => ta.sma(emaSource, emaLength)
    "WMA" => ta.wma(emaSource, emaLength)
    "VWMA" => ta.vwma(emaSource, emaLength)
    "HMA" => ta.hma(emaSource, emaLength)
    "RMA" => ta.rma(emaSource, emaLength) 
    "DEMA" => dema
    "TEMA" => tema 
    "LSMA" => lsma
    "ZLSMA" => zlsma
    =>
        runtime.error("No matching MA type found.")
        float(na)
    
// Define RSI inputs and group them
rsiSource = input.source(title='RSI Source', defval=close, group='RSI Settings')
rsiLength = input.int(title='RSI Length', defval=3, minval=0, maxval=100, group='RSI Settings')
rsiValuee = ta.rsi(rsiSource, rsiLength)
rsiOverbought = input.int(title='RSI Overbought Level', defval=80, group='RSI Settings')
rsiOversold = input.int(title='RSI Oversold Level', defval=20, group='RSI Settings')

// Define overbought and oversold conditions
isRsiOB = rsiValuee >= rsiOverbought
isRsiOS = rsiValuee <= rsiOversold

// ADX Inputs and calculation of the value
adxlen = input.int(5, title='ADX Smoothing', group='ADX Settings')
dilen = input.int(5, title='DI Length', group='ADX Settings')
dirmov(len) =>
    up = ta.change(high)
    down = -ta.change(low)
    plusDM = na(up) ? na : up > down and up > 0 ? up : 0
    minusDM = na(down) ? na : down > up and down > 0 ? down : 0
    truerange = ta.rma(ta.tr, len)
    plus = fixnan(100 * ta.rma(plusDM, len) / truerange)
    minus = fixnan(100 * ta.rma(minusDM, len) / truerange)
    [plus, minus]
adx(dilen, adxlen) =>
    [plus, minus] = dirmov(dilen)
    sum = plus + minus
    adx = 100 * ta.rma(math.abs(plus - minus) / (sum == 0 ? 1 : sum), adxlen)
    adx
sig = adx(dilen, adxlen)

// Define the input and value where it is considered that there i
```