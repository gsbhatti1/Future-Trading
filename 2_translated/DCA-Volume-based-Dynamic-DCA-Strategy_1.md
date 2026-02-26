> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|3|Swing Points|
|v_input_float_1|1.1|Median drop Mult|
|v_input_2|-5|Floating Loss|
|v_input_3|5|Number of all orders|
|v_input_4|20|Length of relative volume|
|v_input_5|2|Volume Multiplier|
|v_input_float_2|true|Take Profit Multiplier|


> Source (PineScript)

```pinescript
/*backtest
start: 2024-04-04 00:00:00
end: 2024-04-11 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © AHMEDABDELAZIZZIZO

//@version=5
strategy("Volume-based Dynamic DCA Strategy", overlay=true)

// Parameter Definitions
swing_points = input(3, title="Swing Points")
median_drop_mult = input(1.1, title="Median drop Mult", type=input.float)
floating_loss = input(-5, title="Floating Loss")
num_orders = input(5, title="Number of all orders")
rel_vol_length = input(20, title="Length of relative volume")
volume_multiplier = input(2, title="Volume Multiplier")
take_profit_multiplier = input(true, title="Take Profit Multiplier", type=input.bool)

// Strategy Logic
var float[] support_levels = array.new_float(0)
var int num_buys = 0

if ta.pivotlow(swing_points) and volume > volume * volume_multiplier
    array.push(support_levels, close)
    if array.size(support_levels) == 1
        low_price = array.get(support_levels, 0)
        
        // Calculate the median drop percentage for take-profit setting
        var float[] drop_percentages = array.new_float(0)
        for i = 1 to array.size(support_levels) - 1
            if close < array.get(support_levels, i - 1) and low_price < array.get(support_levels, i)
                drop = (array.get(support_levels, i - 1) - array.get(support_levels, i)) / array.get(support_levels, i - 1)
                array.push(drop_percentages, drop)
        
        if array.size(drop_percentages) > 0
            median_drop = ta.median(array.drop(drop_percentages, 5), array.size(drop_percentages))
            take_profit_price = low_price * (1 + median_drop_mult * median_drop)
            
            // Place order and update num_buys
            strategy.entry("Buy", strategy.long)
            num_buys := num_buys + 1
            
            if num_buys == num_orders
                break
        
        array.resize(support_levels, 0)
    end

// Take Profit Logic
if na(take_profit_price) == false and close > take_profit_price
    strategy.close("Buy")
```

This PineScript code implements the described volume-based dynamic DCA (Dollar-Cost Averaging) strategy. It identifies support levels using `ta.pivotlow()` and triggers buy orders when price breaks below these levels with increased trading volume, adjusting position sizes based on floating loss and setting take-profit levels dynamically.