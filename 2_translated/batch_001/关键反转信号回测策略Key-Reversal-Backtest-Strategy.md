```markdown
#### Overview

The key reversal backtest strategy identifies key reversal signals in stock prices to determine if the current trend is reversing, in order to capture the price movement direction after the trend reversal. The strategy is based on the theory of "key reversal day". It goes long or short when detecting key reversal signals, and locks in profits by configuring take profit and stop loss.

#### Strategy Principle 
The core logic of the key reversal backtest strategy is to identify the key reversal day. According to the price movement of the stock, we can judge the current trend direction. The emergence of a key reversal signal indicates that the trend may reverse.

Specifically, for an uptrend, if the lowest price of the day breaks the new low over a period of time, but the close price is near the previous day's low, then this day is a key reversal day. This means that the bullish power is weakening and the bearish pressure is increasing, indicating the uptrend may reverse into a downtrend. The strategy will open short position on the key reversal day.

On the contrary, for a downtrend, if the lowest price of the day breaks the new low, but the close price is near the previous day's high. This is also a key reversal day, indicating that bearish power is diminishing and the downtrend may reverse into an uptrend. The strategy will open long position on the key reversal day.

By identifying the key reversal day and tracking the subsequent price movement, the strategy is able to capture the run after the price reversal.

#### Advantage Analysis
The main advantages of the key reversal backtest strategy are:

1. Capture trend reversal with large profit space. Key reversal signals often imply a change in trend direction. By judging reversal signals and tracking subsequent runs, relatively large profits can be obtained.
2. Clear rules easy to backtest. The criteria for determining key reversal days are very clear, with the new high/low price reversing the closing price of the previous day. This makes the strategy easy to backtest and helps avoid misjudgments.
3. Flexible adjustment for optimization. Take profit and stop loss levels are very flexible and can be adjusted according to market conditions and personal risk preferences for strategy optimization to reduce risk of loss.

#### Risk Analysis
The key reversal backtest strategy also has some risks:

1. Risk of misjudging reversal signals. Stock prices often have short-term adjustments. Not all key reversal signals imply a trend reversal, which may lead to misjudgments. The probability of misjudgment can be reduced by optimizing parameters and adjusting profit taking and stop loss conditions.
2. Risk of failure to reverse or reverse again after reversal. Even with an accurate judgment, prices after reversal may turn around again or the original trend may continue. This faces the risk of losses. Manage losses in a timely manner by stop loss.
3. Backtest bias. The performance of any rules and signals in live trading may deviate from backtest results and fail to reproduce backtest profits.

#### Optimization Directions
The main optimization directions for the key reversal backtest strategy:

1. Optimize take profit and stop loss settings. Calculate appropriate levels based on more historical data.
2. Add filter conditions combined with other technical indicators to avoid misjudgments. For example, confirm reversal signals with trading volume to avoid misleading by arbitrage operations.
3. Optimize tracking strategy after reversal. Price movements after reversal also have certain rules to follow. Set up subsequent tracking strategies to further increase returns.
4. Use machine learning models to judge signal quality. Train models to evaluate the reliability of each key reversal signal and avoid tracking poor quality signals.

#### Summary
The key reversal signal strategy captures price trend reversal opportunities by identifying key reversal days. The strategy rules are simple and clear, and easy to implement. The trend after reversal has large space to run, but there are also certain risks of misjudgment. By continuously optimizing parameters and filter criteria to reduce misjudgment, relatively reliable results can be obtained.

---

#### Strategy Arguments

| Argument  | Default | Description |
|-----------|---------|-------------|
| v_input_1 | true    | Enter the number of bars over which to look for a new low in prices. |
| v_input_2 | 20      | Take Profit pip |
| v_input_3 | 10      | Stop Loss pip |

#### Source (PineScript)
```pinescript
//@version=5
strategy("Key Reversal Backtest Strategy", overlay=true)

// Inputs
v_input_1 = input.bool(true, title="Look for a new low in the last N bars")
v_input_2 = input.int(20, title="Take Profit pip")
v_input_3 = input.int(10, title="Stop Loss pip")

// Strategy Logic
if (v_input_1)
    // Implement logic to identify key reversal days and determine take profit/stop loss levels
else
    strategy.exit("Profit Exit", "Long Position", profit=close - v_input_2)
    strategy.exit("Loss Exit", "Short Position", stop=v_input_3 - close)

// Add any additional Pine Script code as needed
```
```