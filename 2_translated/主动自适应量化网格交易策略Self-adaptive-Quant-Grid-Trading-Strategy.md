``` pinescript
/*backtest
start: 2024-01-02 00:00:00
end: 2024-02-01 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("(IK) Grid Script", overlay=true, pyramiding=14, close_entries_rule="ANY", default_qty_type=strategy.cash, initial_capital=100.0, currency="USD", commission_type=strategy.commission.percent, commission_value=0.1)
i_autoBounds    = input(group="Grid Bounds", title="Use Auto Bounds?", defval=true, type=input.bool)                             // calculate upper and lower bound of the grid automatically? This will theoretically be less profitable, but will certainly require less attention
i_boundSrc      = input(group="Grid Bounds", title="(Auto) Bound Source", defval="Hi & Low", options=["Hi & Low", "Average"])     // should bounds of the auto grid be calculated from recent High & Low, or from a Simple Moving Average
i_boundLookback = input(group="Grid Bounds", title="(Auto) Bound Lookback", defval=250, type=input.integer)                     // how many bars to look back for auto bounds calculation 
i_boundDev      = input(group="Grid Bounds", title="(Auto) Bound Deviation", defval=0.1, type=input.float)                       // deviation from high/low or average used in auto bounds
i_upperBound    = input(group="Grid Settings", title="(Manual) Upper Boundry", defval=0.285, type=input.float)                   // upper bound for manual grid setting
i_lowerBound    = input(group="Grid Settings", title="(Manual) Lower Boundry", defval=0.225, type=input.float)                   // lower bound for manual grid setting
i_gridLines     = input(group="Grid Settings", title="(?Grid Lines) Grid Line Quantity", defval=8, type=input.integer)            // number of grid lines to be used

```