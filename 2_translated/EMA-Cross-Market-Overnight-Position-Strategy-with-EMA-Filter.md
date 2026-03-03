> Name

Cross-Market-Overnight-Position-Strategy-with-EMA-Filter

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/7837116f837f4fe619.png)

[trans]
This strategy is a cross-market overnight position strategy based on the EMA technical indicator, designed to capture trading opportunities before market close and after market open. The strategy achieves intelligent trading in different market environments through precise time control and technical indicator filtering.

#### Strategy Overview
The strategy mainly gains returns by entering at specific times before market close and exiting at specific times after the next day's market open. Combined with EMA indicators for trend confirmation, it seeks trading opportunities across multiple global markets (US, Asia, Europe). The strategy also integrates automated trading functionality for unattended operation.

#### Strategy Principle
1. Time Control: Enter at fixed times before close and exit at fixed times after open based on different market trading hours.
2. EMA Filtering: Use optional EMA indicators to validate entry signals.
3. Market Selection: Support trading time adaptation for US, Asian, and European markets.
4. Weekend Protection: Force position closure before Friday's close to avoid holding risks over the weekend.

#### Strategy Advantages
1. Multi-market Adaptability: Flexible adjustment of trading times according to different market characteristics.
2. Comprehensive Risk Control: Includes weekend position closure protection mechanism.
3. High Automation Level: Supports automated trading interface integration.
4. Flexible Parameters: Customizable trading times and technical indicator parameters.
5. Trading Cost Consideration: Includes commission and slippage settings.

#### Strategy Risks
1. Market Volatility Risk: Overnight positions may face gap risk.
2. Time Dependency: Strategy effectiveness affected by market time period selection.
3. Technical Indicator Limitations: Single EMA indicator may show lag.
Suggestions: Set stop-loss limits, add more technical indicators for validation.

#### Strategy Optimization Directions
1. Add more technical indicator combinations.
2. Introduce volatility filtering mechanism.
3. Optimize entry and exit time selection.
4. Add adaptive parameter adjustment functionality.
5. Enhance risk control module.

#### Summary
This strategy achieves a reliable overnight trading system through precise time control and technical indicator filtering. The strategy design comprehensively considers practical requirements, including multi-market adaptation, risk control, and automated trading elements, demonstrating strong practical value. Through continuous optimization and improvement, this strategy has the potential to achieve stable returns in live trading.

||

This strategy is a cross-market overnight position strategy based on the EMA technical indicator, designed to capture trading opportunities before market close and after market open. The strategy achieves intelligent trading in different market environments through precise time control and technical indicator filtering.

#### Strategy Overview
The strategy mainly gains returns by entering at specific times before market close and exiting at specific times after the next day's market open. Combined with EMA indicators for trend confirmation, it seeks trading opportunities across multiple global markets (US, Asia, Europe). The strategy also integrates automated trading functionality for unattended operation.

#### Strategy Principle
1. Time Control: Enter at fixed times before close and exit at fixed times after open based on different market trading hours.
2. EMA Filtering: Use optional EMA indicators to validate entry signals.
3. Market Selection: Support trading time adaptation for US, Asian, and European markets.
4. Weekend Protection: Force position closure before Friday's close to avoid holding risks over the weekend.

#### Strategy Advantages
1. Multi-market Adaptability: Flexible adjustment of trading times according to different market characteristics.
2. Comprehensive Risk Control: Includes weekend position closure protection mechanism.
3. High Automation Level: Supports automated trading interface integration.
4. Flexible Parameters: Customizable trading times and technical indicator parameters.
5. Trading Cost Consideration: Includes commission and slippage settings.

#### Strategy Risks
1. Market Volatility Risk: Overnight positions may face gap risk.
2. Time Dependency: Strategy effectiveness affected by market time period selection.
3. Technical Indicator Limitations: Single EMA indicator may show lag.
Suggestions: Set stop-loss limits, add more technical indicators for validation.

#### Strategy Optimization Directions
1. Add more technical indicator combinations.
2. Introduce volatility filtering mechanism.
3. Optimize entry and exit time selection.
4. Add adaptive parameter adjustment functionality.
5. Enhance risk control module.

#### Summary
This strategy achieves a reliable overnight trading system through precise time control and technical indicator filtering. The strategy design comprehensively considers practical requirements, including multi-market adaptation, risk control, and automated trading elements, demonstrating strong practical value. Through continuous optimization and improvement, this strategy has the potential to achieve stable returns in live trading.

||

> Source (PineScript)

```pinescript
//@version=5
strategy("Overnight Positioning with EMA Confirmation - Strategy [presentTrading]", overlay=true, precision=3, commission_value=0.02, commission_type=strategy.commission.percent, slippage=1, currency=currency.USD, default_qty_type=strategy.percent_of_equity, default_qty_value=10, initial_capital=10000)

// Input parameters
entryMinutesBeforeClose = input.int(20, title="Minutes Before Close to Enter", minval=1)
exitMinutesAfterOpen = input.int(20, title="Minutes After Open to Exit", minval=1)
emaLength = input.int(100, title="EMA Length", minval=1)
emaTimeframe = input.timeframe("240", title="EMA Timeframe")
useEMA = input.bool(true, title="Use EMA Filter")

// Market Selection Input
marketSelection = input.string("US", title="Select Market", options=["US", "Asia", "Europe"])

// Timezone for each market
marketTimezone = marketSelection == "US" ? "America/New_York" :
                 marketSelection == "Asia" ? "Asia/Tokyo" :
                 "Europe/London"  // Default to London for Europe

// Market Open and Close Times for each market
var float marketOpenTime = na
var float marketCloseTime = na

if (marketSelection == "US")
    marketOpenTime := time("America/New_York", "0930")
    marketCloseTime := time("America/New_York", "1600")
else if (marketSelection == "Asia")
    marketOpenTime := time("Asia/Tokyo", "0930")
    marketCloseTime := time("Asia/Tokyo", "1500")
else
    marketOpenTime := time("Europe/London", "0800")
    marketCloseTime := time("Europe/London", "2100")

// Logic for entering and exiting trades based on the selected market's open and close times, adjusted by entry and exit minutes.
```