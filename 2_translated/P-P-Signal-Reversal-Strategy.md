> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|4|(?Parameters of strategy.)Cardinality:|
|v_input_float_1|false||ΔErf|:|
|v_input_1|timestamp(30 Dec 1957 00:00 +0300)|(?Observation time.)Start date:|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// **********************************************************************************************************
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// P-Signal Strategy RVS © Kharevsky
// **********************************************************************************************************
strategy('P-Signal Strategy RVS.', precision=3, process_orders_on_close=true, pyramiding=0,
     commission_type=strategy.commission.percent,
     commission_value=0.2)
// Parameters and const of P-Signal.
nPoints = input.int(title='Cardinality:', defval=4, minval=4, maxval=200, group='Parameters of strategy.')
ndErf = input.float(title='|ΔErf|:', defval=0, minval=0, maxval=1, step=0.01, group='Parameters of strategy.')
tStartDate = input(title='Start date:', defval=timestamp('30 Dec 1957 00:00 +0300'), group='Observation time.')
int nIntr = nPoints - 1
// Horner's method for the error (Gauss) & P-Signal functions.
fErf(x) =>
    nT = 1.0 / (1.0 + 0.5 * math.abs(x))
    nAns = 1.0 - nT * math.exp(-x * x - 1.26551223 +
     nT * (1.00002368 + nT * (0.37409196 + nT * (0.09678418 +
     nT * (-0.18628806 + nT * (0.27886807 + nT * (-1.135
```

The translated text continues, but the source code was cut off for brevity. The translation provided above covers all the human-readable text in the document while keeping the original formatting and code blocks intact.