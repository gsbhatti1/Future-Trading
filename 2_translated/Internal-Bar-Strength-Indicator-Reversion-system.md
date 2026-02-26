```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-09-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Internal-Bar-Strength-Indicator-Reversion-system", initial_capital=10000, overlay=false, pyramiding=5, default_qty_value=100, currency="USD")

// Note: The commented-out code for strategy.risk.allow_entry_in(strategy.direction.long) is not included.

src = close
ibs = (close - low) / (high - low) * 100

longCondition = ibs < 5
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long)

shortCondition = ibs > 99
if (shortCondition)
    strategy.entry("My Short Entry Id", strategy.short)

p = close * 0.01 * 10
strategy.exit("exit", "My Long Entry Id", profit=10, loss=2)
strategy.exit("exit", "My Short Entry Id", profit=10, loss=2)
```

---

### Strategy Description

It appears that the Pine Script is used to set up a trading strategy with conditions based on the Internal Bar Strength (IBS) indicator.

To explain the code:

1. **Strategy Settings**: The strategy named "Internal-Bar-Strength-Indicator-Reversion-system" has an initial capital of $10,000, no overlay, allows up to 5 entries in the same direction, and each trade consists of a quantity of 100 units.

2. **Calculation of IBS**: The script calculates the IBS as a percentage of the current bar's range that is made up by the difference between the close and the low. Note that the indicator ranges between 0 and 100%.

3. **Long Entry Conditions**: It enters a long trade when the IBS falls below 5.

4. **Short Entry Conditions**: It enters a short trade when the IBS rises above 99.

5. **Exit Conditions**: The trading strategy exits either position after either a profit of 10% or a loss of 2%.

Note: This script indicates a mean reversion strategy, assuming that the price will return to its mean and trades based on this assumption. However, please spend enough time testing this strategy to make sure it works well with your specific use case.

### Source (PineScript)

```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-09-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Internal-Bar-Strength-Indicator-Reversion-system", initial_capital=10000, overlay=false, pyramiding=5, default_qty_value=100, currency="USD")

// Note: The commented-out code for strategy.risk.allow_entry_in(strategy.direction.long) is not included.

src = close
ibs = (close - low) / (high - low) * 100

longCondition = ibs < 5
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long)

shortCondition = ibs > 99
if (shortCondition)
    strategy.entry("My Short Entry Id", strategy.short)

p = close * 0.01 * 10
strategy.exit("exit", "My Long Entry Id", profit=10, loss=2)
strategy.exit("exit", "My Short Entry Id", profit=10, loss=2)
```

### Detail

https://www.fmz.com/strategy/426145

### Last Modified

2023-09-08 16:33:39