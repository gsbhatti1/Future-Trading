``` pinescript
/*backtest
start: 2023-09-18 00:00:00
end: 2023-09-25 00:00:00
period: 15h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © rouxam

// Author: ChaoZhang
// Inspired by the original work of ericlin0122

//@version=4
strategy("Backtesting DCA-Bot-Strategy", overlay=true, pyramiding=99, process_orders_on_close=true, commission_type=strategy.commission.percent, commission_value=0.1)

// Strategy Inputs
price_deviation         = input(1.0, type=input.float,  title='Price deviation to open safety orders (%)')
take_profit_percentage  = input(20.0, type=input.float, title='Target Take Profit (%)')
trailing_take_profit    = input(3.0, type=input.float, title='Trailing Take Profit (%) [0 = Disabled]')
base_order_amount       = input(10.0, type=input.float, title='base order')
safe_order_amount       = input(20.0, type=input.float, title='safe order')
safe_order_volume_scale = input(0.5, type=input.float, title='Safety order volume scale')
safe_order_step_scale   = input(1.5, type=input.float, title='Safety order step scale')
max_safe_orders         = input(8, type=input.integer,  title='Max safe orders')
from_month              = input(true, type=input.bool,  title='From Month', confirm=false)
from_day                = input(true, type=input.bool,  title='From Day', confirm=false)
from_year               = input(2021, type=input.integer, title='From Year')
to_month                = input(true, type=input.bool,  title='To Month', confirm=false)
to_day                   = input(true, type=input.bool,  title='To Day', confirm=false)
to_year                 = input(9999, type=input.integer, title='To Year')

// Strategy Variables
var float base_price = na
var int safety_order_count = 0

if (barstate.isfirst)
    base_price := close
else if (close > base_price and base_price != na)
    strategy.entry("Entry", strategy.long)

if (safety_order_count < max_safe_orders and not strategy.opentrades.exists("Entry"))
    recent_safety_order := strategy.closedtrades.get_close_time(strategy.opentrades.last_id, "Safety Order")
    
    if (not from_month or month > from_month) and 
       (not from_day or dayofmonth > from_day) and
       (not from_year or year > from_year)
       
        recent_safety_order_price := strategy.closedtrades.get_price(strategy.opentrades.last_id, "Safety Order")
        
        next_safety_order_level := recent_safety_order_price * (1 + price_deviation / 100)
        strategy.exit("Exit", "Entry", limit=next_safety_order_level, comment="Safety Order")
    
    if (safety_order_count == max_safe_orders - 1)
        safety_order_count := 0
    else 
        safety_order_count += 1

// Take Profit Logic
take_profit_level = na
if (position_size > 0 and base_price != na)
    take_profit_level := base_price * (1 + take_profit_percentage / 100)

if (trailing_take_profit != 0.0)
    ttp_max = na
    if not na(take_profit_level) and high > ttp_max 
        ttp_max := high
    strategy.exit("Trail Exit", "Entry", limit=ttp_max, comment="Trailing Take Profit")

// End of Script
```