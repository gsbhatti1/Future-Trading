> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|9|WMA Length|
|v_input_int_2|21|MMA Length|
|v_input_float_1|5|Stop Loss (%)|
|v_input_float_2|5|Take Profit (%)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("WMA vs MMA Crossover Strategy with SL/TP", shorttitle="WMA_MMA_Cross_SL_TP", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// Définition des périodes pour les moyennes mobiles
wmaLength = input.int(9, title="WMA Length")
mmaLength = input.int(21, title="MMA Length")

// Paramètres de Stop Loss et Take Profit en pourcentage
stopLossPercentage = input.float(5, title="Stop Loss (%)") / 100
takeProfitPercentage = input.float(5, title="Take Profit (%)") / 100

// Calcul des moyennes mobiles
wma = ta.wma(close, wmaLength)
mma = ta.sma(close, mmaLength)

// Génération des signaux d'achat et de vente
buySignal = ta.crossover(wma, mma)
sellSignal = ta.crossunder(wma, mma)

// Positionnement des ordres selon les conditions de stop loss et take profit
if (buySignal)
    strategy.entry("Buy", strategy.long)
    
    // Définition du prix d'entrée pour le stop loss et le take profit
    entryPrice = close
    
    strategy.exit("SL_TP", "Buy", stop=entryPrice * (1 - stopLossPercentage), limit=entryPrice * (1 + takeProfitPercentage))

if (sellSignal)
    strategy.entry("Sell", strategy.short)
    
    // Définition du prix d'entrée pour le stop loss et le take profit
    entryPrice = close
    
    strategy.exit("SL_TP", "Sell", stop=entryPrice * (1 + stopLossPercentage), limit=entryPrice * (1 - takeProfitPercentage))
```

This PineScript code defines a trading strategy that uses the crossover of Weighted Moving Average (WMA) and Simple Moving Average (SMA) to generate buy and sell signals. The script also incorporates stop loss and take profit levels based on predefined percentages.