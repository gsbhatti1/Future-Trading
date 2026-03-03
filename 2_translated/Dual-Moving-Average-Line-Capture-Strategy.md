``` pinescript
/*backtest
start: 2023-12-05 00:00:00
end: 2023-12-06 22:00:00
period: 15m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This close code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © AugustoErni

//@version=5
strategy('Bollinger Bands Modified (Stormer)', overlay=true)

bbL                   = input.int(20, title='BB Length/Comprimento da Banda de Bollinger', minval=1, step=1, tooltip='Calculate the length of the Bollinger Bands')
stdDev                = input.float(0.38, title='BB Standard Deviation/Desvio Padrão da Banda de Bollinger', minval=0.01, step=0.01, tooltip='Set the standard deviation for the Bollinger Bands')
emaL                  = input.int(80, title='EMA Length/Comprimento da Média Móvel Exponencial', minval=1, step=1, tooltip='Calculate the length of the EMA lines')
highH                 = input.int(7, title='Highest High Length/Comprimento da Alta Maior', minval=1, step=1, tooltip='Determine the period for the highest high calculation')
lowL                  = input.int(7, title='Lowest Low Length/Comprimento da Baixa Menor', minval=1, step=1, tooltip='Determine the period for the lowest low calculation')
tp                     = input.float(1.6, title='Target Take Profit/Objetivo de Lucro Alvo', minval=0.5, step=0.1, tooltip='Set the target take profit multiplier')
checkTrend            = input.bool(true, title='Check Trend EMA/Verificar Tendência da Média Móvel Exponencial', tooltip='Enable to use EMA trend as a filter for entry signals')
addCrossover          = input.bool(false, title='Add Another Crossover Check/Adicionar Mais uma Verificação de Cruzamento Superior', tooltip='Enable to add an additional crossover check above the main one')
addCrossunder         = input.bool(false, title='Add Another Crossunder Check/Adicionar Mais uma Verificação de Cruzamento Inferior', tooltip='Enable to add an additional crossunder check below the main one')
showInsideBar         = input.bool(true, title='Show Inside Bar Pattern/Mostrar Padrão de Inside Bar', tooltip='Enable to show inside bar pattern')

// Bollinger Bands
src = close
[bbU, bbM, bbD] = ta.bband(src, bbL, stdDev)

// EMA Lines
emal = ta.ema(close, emaL)
emam = ta.ema(close, emaL * 2)

// Logic
longCond1   = emal > emam and close > bbU
longCond2   = highest(high[highH]) > highest(high[highH - 1])
shortCond1  = emal < emam and close < bbD
shortCond2  = lowest(low[lowL]) < lowest(low[lowL - 1])

// Main Logic for Entry
if (checkTrend)
    longCond1 := longCond1 and ta.crossover(emal, emam) and highH > 0
    shortCond1 := shortCond1 and ta.crossunder(emal, emam) and lowL > 0

var float stopLossLong = na
var float takeProfitLong = na
var float stopLossShort = na
var float takeProfitShort = na

if (longCond1)
    strategy.entry("Long", strategy.long)
    if (na(stopLossLong))
        stopLossLong := lowest(low[lowL])
    takeProfitLong := emal * tp
else if (shortCond1)
    strategy.entry("Short", strategy.short)
    if (na(stopLossShort))
        stopLossShort := highest(high[highH])
    takeProfitShort := emam / tp

// Stop Loss and Take Profit Logic
if (showInsideBar)
    insideBar = ta.barssince(not barmerge.islastbar) == 0
else
    insideBar = true

if (longCond1 and insideBar)
    strategy.exit("Take Profit Long", "Long", stop=stopLossLong, limit=takeProfitLong)
if (shortCond1 and insideBar)
    strategy.exit("Take Profit Short", "Short", stop=stopLossShort, limit=takeProfitShort)

// Plotting
plot(bbU, color=color.blue, title='Bollinger Upper Band')
plot(bbM, color=color.gray, title='Bollinger Middle Band')
plot(bbD, color=color.red, title='Bollinger Lower Band')
plot(emal, color=color.green, title='EMA Line (Short)')
plot(emam, color=color.orange, title='EMA Line (Long)')

```