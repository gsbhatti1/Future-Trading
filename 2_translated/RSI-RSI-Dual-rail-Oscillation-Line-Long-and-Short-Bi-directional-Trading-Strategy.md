> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|vrsi_length|14|RSI period length|
|upper_band_multiplier|2.0|Multiplier for upper rail calculation|
|lower_band_multiplier|2.0|Multiplier for lower rail calculation|
|sma_length|50|Moving average period length|
|long_signal_condition|"crossed_below"|Long signal condition: "crossed_below" or "breakout"|
|short_signal_condition|"crossed_above"|Short signal condition: "crossed_above" or "breakout"|
|pyramid_enabled|True|Enable pyramiding (adding to existing trades)|
|max_open_positions|int(10)|Maximum number of open positions at any time|
|take_profit_percentage|5.0|Take profit percentage in decimal form|
|stop_loss_percentage|2.0|Stop loss percentage in decimal form|
|trailing_stop_enabled|True|Enable trailing stop loss|
|trailing_stop_offset|3.0|Trailing stop offset in percentage|
|only_long|False|Go long only (disable short signals)|
|only_short|False|Go short only (disable long signals)|
|reverse_signals|False|Reverse trading direction based on conditions|
|backtest_period|"1Y"|Backtest period for optimization tests|
|optimization_runs|int(50)|Number of runs for optimization testing|