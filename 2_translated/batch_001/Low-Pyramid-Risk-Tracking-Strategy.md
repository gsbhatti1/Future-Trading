> Name

Low-Pyramid-Risk-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/190799ca3c70c5fb0ef.png)
[trans]

This strategy identifies potential low points in price movement through a combination of different indicators and gradually builds positions through pyramiding to reduce risk. The strategy also incorporates functions such as stop loss, take profit, and trailing stop loss to effectively control risk.

## Strategy Overview

The strategy first uses the difference between RSI and EMA RSI to identify potential price lows. To filter out false signals, the strategy also combines moving average and multi-timeframe stochastic indicators for confirmation. Once the low point signal is confirmed, long positions will be gradually built at slightly lower prices from that point through pyramiding. The strategy allows up to 12 tracking orders to be opened, with the size of each order increasing in sequence, which can effectively diversify risks. All orders will follow an overall stop loss to exit, while allowing to set take profit separately for each order. To further control risks, the strategy also sets an overall stop loss based on equity percentage.

## Strategy Principle

The strategy consists of three main modules: low point identification, pyramid tracking and risk control.

**Low Point Identification Module**: Uses the difference between RSI and its EMA to identify potential price lows. To improve accuracy, moving average indicator and multi-timeframe stochastic indicators are introduced for signal filtering. Only when price is below moving average and stochastic K line is below 30 will the validity of the low point signal be confirmed.

**Pyramid Tracking Module**: Is the core of this strategy. Once the low point signal is confirmed, the strategy will open the first position at 0.1% below that low point. Afterwards, as long as price keeps falling and is below a certain percentage of average entry price, more long orders will be added. The size of new orders will increase in sequence, for example the third order is 3 times the first order size. This pyramid tracking approach helps averaging risks. The strategy allows up to 12 tracking orders.

**Risk Control Module**: Includes three aspects. First is the overall stop loss based on highest price in recent periods. All orders will follow this stop loss. Second is independent take profit setting for each order, which allows to close order based on certain percentage of entry price. Third is overall stop loss based on percentage of account equity, which is the strongest risk control method.

## Strategy Advantages

- Pyramid tracking reduces risk of individual orders while diversifying overall risk
- Combination of indicators improves accuracy of low point identification  
- Overall stop loss, take profit and trailing stop functions effectively control risk
- Equity stop loss protects account from significant losses  
- Parameters can be tuned to balance risk vs reward

## Strategy Risks

- Low point identification still has some limitation, may miss best entry point or get into false signal
- Facing adverse market when adding orders may increase loss  
- Needs relatively long period to reflect the advantage   
- Inappropriate parameter setting may lead to insufficient risk control   

To reduce above risks, some aspects can be optimized:

1. Change or add indicators to improve low point identification accuracy  
2. Optimize number of orders, intervals, take profit percentage etc to lower risk per order
3. Moderately tighten stop loss level to protect profits  
4. Test different products with good liquidity and large fluctuation

## Strategy Optimization  

There is still room for further optimization of this strategy:  

1. Try introducing more advanced techniques like machine learning for low point identification
2. Dynamically adjust order quantity, stop loss level etc based on market condition  
3. Add box stop loss mechanism to avoid expanding losses
4. Add re-entry mechanism  
5. Optimize parameters for stocks and crypto currencies  

## Summary

This strategy effectively reduces risks of individual orders through pyramid tracking approach, and overall stop loss, take profit, trailing stop functions also play very good role of risk control. But there is still room for improving low point identification and other aspects. If more advanced techniques can be introduced, dynamic adjustment of parameters can be added, combined with parameter optimization, the strategy's return-to-risk ratio will significantly improve.