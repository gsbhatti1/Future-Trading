``` pinescript
// Uzun pozisyon açma koşullarını tanımlayalım
longCondition1 = rsiValue < rsiOversold // RSI oversold seviyesinin altındaysa
longCondition2 = adx > 20 // ADX 20'den büyükse
longCondition3 = ta.crossover(plus, minus) // +DI > -DI ise

// Kısa pozisyon açma koşullarını tanımlayalım
shortCondition1 = rsiValue > rsiOverbought // RSI overbought seviyesinin üstündeyken
shortCondition2 = adx > 20 // ADX 20'den büyükse
shortCondition3 = ta.crossunder(plus, minus) // +DI < -DI ise

// Uzun pozisyon açma koşullu işlemler
if (longCondition1 and longCondition2 and longCondition3)
    strategy.entry("Long", strategy.long)

// Kısa pozisyon açma koşullu işlemler
if (shortCondition1 and shortCondition2 and shortCondition3)
    strategy.entry("Short", strategy.short)

// Trailing stop loss uygulama
trailingStopPrice = na(strategy.position_avg_price) ? strategy.position_avg_price : strategy.position_avg_price - (strategy.position_avg_price * trailing_stop_loss_factor)
stopPrice = ta.lowest(low, bar_index + 1) // Bir sonraki barın en düşük fiyat
if (strategy.position_size > 0 and low < stopPrice)
    strategy.exit("Trail Exit", "Long")
if (strategy.position_size < 0 and high > stopPrice)
    strategy.exit("Trail Exit", "Short")

// Grafik üzerindeki gösterim
plot(adx, color=color.blue, title="ADX Value")
hline(rsiOversold, "RSI Oversold Level", color=color.red)
hline(rsiOverbought, "RSI Overbought Level", color=color.green)
```

The Pine Script code has been completed with the necessary conditions for both long and short positions. The trailing stop loss logic has also been added to lock in profits while allowing flexibility based on market movements.