> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|timestamp(01 Nov 2020 13:30 +0000)|Start Date Filter|
|v_input_2|timestamp(1 Nov 2022 19:30 +0000)|End Date Filter|
|v_input_3|70|Sobre Compra|
|v_input_4|30|Sobre Venta|
|v_input_5|14|Periodos|
|v_input_6|14|Logintud media movil|
|v_input_7|2|SL %|
|v_input_8|5|TP %|


> Source (PineScript)

```pinescript
// RSI Cross Cycle Trading Strategy

//@version=5
strategy("RSI Cross-Cycle Trading Strategy", shorttitle="RSI-CCS")

sobrecompra = input.float(70, title="Sobre Compra")
sobreventa = input.float(30, title="Sobre Venta")
periodos = input.int(14, title="Periodos")
periodos_media = input.int(14, title="Longitud media movil")

// RSI Calculation
rsi = ta.rsi(close, periodos)

// Moving Average of RSI
rsi_ema = ta.ema(rsi, periodos_media)

// Buy and Sell Signals
es_compra = rsi > rsi_ema ? true : na
es_venta = rsi < rsi_ema ? true : na

// Plot RSI and EMA
plot(rsi, title="RSI", color=color.blue)
hline(sobrecompra, "Sobre Compra", color=color.red)
hline(sobreventa, "Sobre Venta", color=color.green)

// Trading Logic
if (es_compra[1] == true and not na(es_venta[1]))
    strategy.entry("Compra", strategy.long)

if (es_venta[1] == true and not na(es_compra[1]))
    strategy.close("Compra")

// Stop Loss and Take Profit in Percentage
stop_loss_percent = input.float(2, title="SL %")
take_profit_percent = input.float(5, title="TP %")

stop_price = na
take_price = na

if (strategy.opentrades > 0)
    stop_price := strategy.position_avg_price * (1 - stop_loss_percent / 100)
    take_price := strategy.position_avg_price * (1 + take_profit_percent / 100)

// Plot Stop Loss and Take Profit Levels
plot(stop_price, color=color.red, title="Stop Loss")
plot(take_price, color=color.green, title="Take Profit")
```
```