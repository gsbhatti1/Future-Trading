``` pinescript
/*backtest
start: 2024-12-06 00:00:00
end: 2025-01-04 08:00:00
period: 2h
basePeriod: 2h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Estratégia com Bandas de Bollinger e Sinal de Retorno", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=200)

// Configurações das Bandas de Bollinger
length = input.int(20, title="Período da média")
mult = input.float(2.0, title="Desvio padrão")
bbBasis = ta.sma(close, length)
bbUpper = bbBasis + mult * ta.stdev(close, length)
bbLower = bbBasis - mult * ta.stdev(close, length)

// Configuração para a distância da média
percent_threshold = input.float(3.5, title="Distância da média (%)") / 100

dist_from_mean = 0.0
trigger_condition = false
if not na(bbBasis)
    dist_from_mean := math.abs(close - bbBasis) / bbBasis
    trigger_condition := dist_from_mean >= percent_threshold

// Variáveis para identificar o estado do afastamento
var bool is_outside = false
var color candle_color = color.new(color.white, 0)

if trigger_condition
    is_outside := true

if is_outside and close <= bbUpper and close >= bbLower
    is_outside := false
    candle_color := color.new(color.blue, 0) // Atribui uma cor válida
else
    candle_color := color.new(color.white, 0)

// Aplicar cor às velas
barcolor(candle_color)

// Plotar Bandas de Bollinger
plot(bbBasis, color=color.yellow, title="Média")
plot(bbUpper, color=color.red, title="Banda Superior")
plot(bbLower, color=color.green, title="Banda Inferior")

// Lógica de entrada e saída
longCondition = not is_outside and close > bbUpper
if (longCondition)
    strategy.entry("Buy", strategy.long)
    
shortCondition = is_outside and close < bbLower
if (shortCondition)
    strategy.entry("Sell", strategy.short)

// Marcar sinal de entrada e saída na barra de candlestick
plotshape(series=longCondition, location=location.belowbar, color=color.blue, style=shape.labeldown, text="Buy")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.labelup, text="Sell")
```

This Pine Script code defines a strategy based on Bollinger Bands and mean reversion principles. It includes the necessary calculations for setting up Bollinger Bands, monitoring price deviation from the moving average, and triggering buy/sell signals when prices return to within the Bollinger Bands after significant deviations. The script also visualizes the signals by coloring the bars and marking them on the chart.