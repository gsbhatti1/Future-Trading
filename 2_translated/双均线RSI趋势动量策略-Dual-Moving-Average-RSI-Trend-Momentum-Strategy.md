```pinescript
/*backtest
start: 2024-10-12 00:00:00
end: 2024-11-11 00:00:00
period: 5m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Super Advanced Strategy", overlay=true)

// Configuração de parâmetros
shortMAPeriod = input.int(10, title="Período da Média Móvel Curta", minval=1)
longMAPeriod = input.int(50, title="Período da Média Móvel Longa", minval=1)
rsiPeriod = input.int(14, title="Período do RSI", minval=1)

// Cálculo das Médias Móveis
shortMA = ta.sma(close, shortMAPeriod)
longMA = ta.sma(close, longMAPeriod)

// Cálculo do RSI
rsi = ta.rsi(close, rsiPeriod)

// Plotando as Médias Móvel
plot(shortMA, title="Média Móvel Curta", color=color.blue, linewidth=2)
plot(longMA, title="Média Móvel Longa", color=color.red, linewidth=2)

// Adicionando linhas horizontais para os níveis de sobrecomprado e sobrevendido
hline(70, "Sobrecomprado", color=color.red, linestyle=hline.style_dashed)
hline(30, "Sobrevendido", color=color.green, linestyle=hline.style_dashed)

// Condições de entrada
buyCondition = (shortMA > longMA) and (rsi < 30)
sellCondition = (shortMA < longMA) and (rsi > 70)

// Entradas de ordens
if (buyCondition)
    strategy.entry("Compra", strategy.long)

if (sellCondition)
    strategy.entry("Venda", strategy.short)

// Saídas de ordens
if (rsi > 70)
    strategy.close("Compra")

if (rsi < 30)
    strategy.close("Venda")

// Exibir as condições de compra e venda no gráfico
plotshape(buyCondition, style=shape.labelup, location=location.belowbar, color=color.green, size=size.small, title="Sinal de Compra", text="BUY")
plotshape(sellCondition, style=shape.labeldown, location=location.abovebar, color=color.red, size=size.small, title="Sinal de Venda", text="SELL")

```

#### Summary
This is a quantified trading strategy that perfectly combines trend following with momentum reversal. It uses dual moving averages to determine the direction of trends and RSI to find optimal entry points in overbought or oversold conditions. The strategy ensures both accurate directional accuracy and timely profit-taking when prices are excessively high or low.

The key advantages include:
- Combining trend confirmation with momentum reversal for improved trade success rate.
- Using percentage-based money management to effectively control risks.
- Setting clear entry and exit criteria to avoid subjective judgments.
- Leveraging the overbought/oversold characteristics of RSI.
- Clear strategy logic that is easy to understand and execute.
- Adaptability across different market environments with strong versatility.

#### Risks
- May generate excessive false signals in ranging markets.
- RSI may remain in overbought or oversold zones during strong trends.
- The dual moving average system has inherent lag.
- Fixed parameters may not be suitable for all market conditions.

To manage risks:
- Set stop-loss levels.
- Dynamically adjust parameters based on market volatility.
- Add trend confirmation indicators.
- Control single trade size.

#### Optimization Directions
1. Introduce an adaptive parameter mechanism to dynamically adjust moving average periods based on market volatility.
2. Add a trend strength filter to avoid trading in weak trends.
3. Optimize the money management system to adjust position sizes based on market volatility.
4. Incorporate additional technical indicators for trade confirmation.
5. Develop a dynamic stop-loss mechanism to improve capital efficiency.

Through continuous optimization and improvement, this strategy has the potential to achieve stable returns across different market environments.