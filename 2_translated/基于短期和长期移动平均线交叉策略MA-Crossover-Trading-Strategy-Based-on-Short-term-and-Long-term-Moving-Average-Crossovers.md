> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|34|Short SMA Length|
|v_input_2|89|Long SMA Length|
|v_input_3|8|Holding Period in Candles|


> Strategy Source Code

```python
# MA Crossover Trading Strategy Based on Short-term and Long-term Moving Average Crossovers

def init():
    # Set up the short and long simple moving averages
    global short_sma, long_sma
    short_sma = input.int("v_input_1", title="Short SMA Length", minval=1, defval=34)
    long_sma = input.int("v_input_2", title="Long SMA Length", minval=1, defval=89)
    holding_period = input.int("v_input_3", title="Holding Period in Candles", minval=1, defval=8)
    
    # Define the time frame for observing the crossovers
    observe_time = timeperiod("08:00", "10:00")

def on_bar_open():
    # Check for crossover during the defined time frame
    if observe_time:
        # Calculate the short and long SMAs
        short_sma_value = sma(close, short_sma)
        long_sma_value = sma(close, long_sma)
        
        # Generate buy signal
        if short_sma_value > long_sma_value and not is_long_position:
            buy()
        
        # Generate sell signal
        if short_sma_value < long_sma_value and not is_short_position:
            sell()

def on_bar_close():
    # Check if the holding period is reached and exit the position
    if is_long_position and bar_index - enter_bar_index >= holding_period:
        exit_long()
    elif is_short_position and bar_index - enter_bar_index >= holding_period:
        exit_short()

def on_stop_loss():
    # Execute stop loss when the stop loss condition is triggered
    if is_long_position:
        exit_long()
    elif is_short_position:
        exit_short()
```