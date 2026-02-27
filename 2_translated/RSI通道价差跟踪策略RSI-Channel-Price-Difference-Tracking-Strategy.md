> Name

RSI Channel Price Difference Tracking Strategy RSI-Channel-Price-Difference-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/14b49b2be28d01440da.png)
 [trans]

## Overview

The RSI Channel Price Difference Tracking strategy generates trading signals by tracking the fluctuations of RSI indicators within threshold channels, combined with price breakouts. The strategy aims to capture fast buy and sell bursts in the crypto market.

## Strategy Logic

1. Use Hull Moving Average to smooth the RSI and generate smoothed RSI indicators, including RSI for closing price, highest price, lowest price, and median price.
2. Set the RSI channel range to 55-45. When RSI enters into the 55-45 channel, it indicates entering into a shock zone.
3. When closing price RSI drops back from the upper limit of the channel, and the closing price is lower than the median price, it indicates that the price is under pressure; however, at this time, the median price RSI is still above the upper limit of the channel, indicating that the median price still has buying power. This meets the logic of tracking median price breakouts, so a buy signal is generated.
4. When closing price RSI bounces back from the lower limit of the channel, and the closing price is higher than the median price, it indicates that the price has support; but at this time, the median price RSI falls below the lower limit of the channel, indicating that the median price has greater pressure. This meets the logic of tracking median price breakouts, so a sell signal is generated.
5. The highest price RSI and lowest price RSI indicators are used to promptly identify invalid trading signals and realize quick stop losses.

## Advantages of the Strategy

1. Using median price breakouts to track the strong direction of the median price meets the idea of trend tracking.
2. When RSI fluctuates within the threshold channel, it indicates entering into a shock zone. At this time, using median price to track the strong direction of the median price avoids being trapped in range-bound shocks.
3. The highest price RSI and lowest price RSI indicators are used to quickly identify invalid trading signals and realize fast stop losses, which can effectively control losses.

## Risks of the Strategy

1. Improper RSI parameter settings may cause too sensitive or slow responses.
2. The significance of median price breakouts is not always reliable, and the median price itself may also fluctuate.
3. High volatility in crypto markets, over-loose stop loss settings may lead to magnified losses.

Solutions:

- Optimize RSI parameters to make proper responses to price changes
- Combine more indicators to judge the reliability of median price breakouts
- Tighten stop loss settings appropriately to prevent huge losses

## Directions for Strategy Optimization

1. Combine more indicators to judge the breakout direction of the median price

Introduce indicators like Bollinger Bands to judge whether the median price is close to the upper or lower bands, thus improving the accuracy of judging the breakout direction of the median price.

2. Introduce machine learning models to assist in judgment

Use LSTM and other deep learning models to predict future trends of the median price and assist in determining whether the median price can successfully break out in a certain direction.

3. Use adaptive stop loss

Dynamically adjust stop loss positions based on market volatility. For example, tighten stop loss positions appropriately when volatility rises; loosen stop loss positions appropriately when volatility declines.

## Summary

The RSI Channel Price Difference Tracking Strategy generates trading signals by tracking RSI fluctuations within channels combined with price breakouts, aiming to capture fast buy/sell bursts in crypto markets. The strategy effectively combines trend tracking and range identification methods and can still obtain good trading signals when price differences narrow. Meanwhile, the fast stop loss mechanism also makes the risks of the strategy controllable. The next step is to further improve the reliability and profitability of the strategy by combining more indicator judgments and machine learning predictions.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|13|(?=== RSI ===)Period|
|v_input_2|55|(?=== Mid Channel ===)Upper|
|v_input_3|45|Lower|
|v_input_4|70|(?=== Over ===)Overbought|
|v_input_5|30|Oversold|
|v_input_6|3|(?=== Hull MA ===)Period|


> Source (PineScript)

``` pinescript
//@version=4
```