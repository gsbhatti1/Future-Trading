> Name

Ichimoku Cloud Quantitative Strategy - Ichimoku-Clouds-Quant-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/153b14ed8bc9c5ea17a.png)
[trans]
## Overview

This strategy is based on the Ichimoku Cloud indicator, combining Tenkan line, Kijun line, leading line, and cloud charts to identify buying and selling signals and automate trading. It integrates both the standard Ichimoku model and the customization functionality of the TradingView strategy tester, suitable for both novice and experienced traders.

## Strategy Logic

The strategy utilizes the standard Ichimoku model, including Tenkan line, Kijun line, leading line, Senkou A, and Senkou B lines. It identifies trading signals by comparing crosses between these lines.

Specifically, a bullish signal is generated when the Tenkan line crosses above the Kijun line, and a bearish signal when the Tenkan line crosses below the Kijun line. Additionally, the relative position of the crossing Tenkan line to the cloud charts is checked to categorize the signals as strong, neutral, or weak. For example, if the Tenkan line is above both Senkou A and Senkou B lines during the cross, it is a strong bullish signal.

The strategy provides extensive customization parameters for users to freely combine entry and exit signals to build their own trading systems.

## Advantages

1. Combines the advanced technical analysis of Ichimoku with the customizability of TradingView's strategy tester.
2. Provides various parameter settings suitable for different trading styles.
3. Real-time visualized cloud charts, providing clear trend identification.
4. Parameters can be optimized through backtesting to enhance performance.

## Risks

1. Ichimoku models tend to generate false signals, which need confirmation from candlesticks.
2. Too many parameters can confuse novice traders.
3. Cloud charts have a lagging nature and are not ideal for chasing surges or reversals.
4. Backtest results do not guarantee live trading performance; remain cautious when live trading.

## Enhancement Opportunities

1. Optimize parameters to find the best combination.
2. Add filters with other indicators to screen false signals.
3. Incorporate stop loss and profit-taking logic to control risk per trade.
4. Consider impacts of product, timeframes, etc., on the strategy.
5. Conduct real-trade validation and parameter tuning.

## Conclusion

As a new generation of technical analysis tools, Ichimoku combined with TradingView's visualization and strategy development capabilities provides powerful support for quantitative trading. This strategy fully utilizes both to build an automated trading system. Although it still requires further enhancement, it has already demonstrated significant application potential. With continuous improvements in parameter tuning and functionality expansion, this strategy is likely to become one of the mainstream quantitative trading strategies.

||

## Overview

This strategy is based on the Ichimoku Cloud indicator, combining Tenkan line, Kijun line, leading line, and cloud charts to identify buying and selling signals and automate trading. It integrates both the standard Ichimoku model and the customization functionality of the TradingView strategy tester, suitable for both novice and experienced traders.

## Strategy Logic

The strategy utilizes the standard Ichimoku model, including Tenkan line, Kijun line, leading line, Senkou A, and Senkou B lines. It identifies trading signals by comparing crosses between these lines.

Specifically, a bullish signal is generated when the Tenkan line crosses above the Kijun line, and a bearish signal when the Tenkan line crosses below the Kijun line. Additionally, the relative position of the crossing Tenkan line to the cloud charts is checked to categorize the signals as strong, neutral, or weak. For example, if the Tenkan line is above both Senkou A and Senkou B lines during the cross, it is a strong bullish signal.

The strategy provides extensive customization parameters for users to freely combine entry and exit signals to build their own trading systems.

## Advantages

1. Combines the advanced technical analysis of Ichimoku with the customizability of TradingView's strategy tester.
2. Provides various parameter settings suitable for different trading styles.
3. Real-time visualized cloud charts, providing clear trend identification.
4. Parameters can be optimized through backtesting to enhance performance.

## Risks

1. Ichimoku models tend to generate false signals, which need confirmation from candlesticks.
2. Too many parameters can confuse novice traders.
3. Cloud charts have a lagging nature and are not ideal for chasing surges or reversals.
4. Backtest results do not guarantee live trading performance; remain cautious when live trading.

## Enhancement Opportunities

1. Optimize parameters to find the best combination.
2. Add filters with other indicators to screen false signals.
3. Incorporate stop loss and profit-taking logic to control risk per trade.
4. Consider impacts of product, timeframes, etc., on the strategy.
5. Conduct real-trade validation and parameter tuning.

## Conclusion

As a new generation of technical analysis tools, Ichimoku combined with TradingView's visualization and strategy development capabilities provides powerful support for quantitative trading. This strategy fully utilizes both to build an automated trading system. Although it still requires further enhancement, it has already demonstrated significant application potential. With continuous improvements in parameter tuning and functionality expansion, this strategy is likely to become one of the mainstream quantitative trading strategies.

| Argument | Default | Description |
| --- | --- | --- |
| v_input_string_1 | yourBotSourceUuid | (?Trading Bot Settings) sourceUuid: |
| v_input_string_2 | yourBotSecretToken | secretToken: |
| v_input_1 | timestamp(2023-01-01T00:00:00) | (?Trading Period Settings) Trade Start Date/Time |
| v_input_2 | timestamp(2025-01-01T00:00:00) | Trade Stop Date/Time |
| v_input_string_3 | 0 | (?Trading Mode Settings) Trading Mode: Long | Short |
| v_input_string_4 | 0 | (?Long Mode Signals - set up if Trading Mode: Long) Select Entry Signal (Long): Bullish All | Bullish Strong | Bullish Neutral | Bullish Weak | Bullish Strong and Neutral | Bullish Neutral and Weak | Bullish Strong and Weak | None |
| v_input_string_5 | 0 | Select Exit Signal (Long): Bearish Weak | Bearish Strong | Bearish Neutral | None | Bearish Strong and Neutral | Bearish Neutral and Weak | Bearish Strong and Weak | Bearish All |
| v_input_string_6 | 0 | (?Short Mode Signals - set up if Trading Mode: Short) Select Entry Signal (Short): None | Bearish Strong | Bearish Neutral | Bearish Weak | Bearish Strong and Neutral | Bearish Neutral and Weak | Bearish Strong and Weak | Bearish All |
| v_input_string_7 | 0 | Select Exit Signal (Short): None | Bullish Strong | Bullish Neutral | Bullish Weak | Bullish Strong and Neutral | Bullish Neutral and Weak | Bullish Strong and Weak | Bullish All |
| v_input_float_1 | false | (?Risk Management) Take Profit, % (0 - disabled) |
| v_input_float_2 | false | Stop Loss, % (0 - disabled) |
| v_input_int_1 | 9 | (?Indicator Settings) Tenkan |
| v_input_int_2 | 26 | Kijun |
| v_input_int_3 | 52 | Chikou |
| v_input_int_4 | 26 | Offset |
| v_input_3 | false | (?Display Settings) Show Tenkan Line |
| v_input_4 | false | Show Kijun Line |
| v_input_5 | true | Show Senkou A Line |
| v_input_6 | true | Show Senkou B Line |
| v_input_7 | false | Show Chikou Line |

> Source (PineScript)

```pinescript
//@version=5

//  -----------------------------------------------------------------------------
//  Copyright © 2024 Skyrex, LLC. All rights reserved.
//  -----------------------------------------------------------------------------

//  Version: v2.1
//  Release: Jan 22, 2024

strategy(title = "Advanced Ichimoku Clouds Strategy Long and Short", ...
```