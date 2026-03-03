``` pinescript
/*backtest
start: 2022-11-27 00:00:00
end: 2023-12-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © XaviZ

//@version=4
strategy(title = "Dynamic Grid Trading Management", shorttitle = "DGM", overlay = true, pyramiding = 1000, default_qty_value = 0)

// ———————————————————— Inputs

WOption             = input('PRICE',        " 》 WIDTH TYPE",                                                   options = ['PRICE','% PP'])
Width               = input(500,            " 》 WIDTH",                type = input.float,     minval = 0)
ppPeriod            = input('Month',        " 》 PP PERIOD",                                                    options = ['Day','Week','15D','Month'])
BuyType             = input("CASH",         " 》 BUY TYPE",                                                     options = ["CONTRACTS","CASH","% EQUITY"])
BuyQ                = input(10000,          " 》 QUANTITY TO BUY",      type = input.float,     minval = 0)
SellType            = input('CONTRACTS',    " 》 SELL TYPE",                                                    options = ["CONTRACTS","CASH","% EQUITY"])
SellQ               = input(2,              " 》 QUANTITY TO SELL",     type = input.float,     minval = 0)

// ———————————————————— Vars

// ————— Buy Price & Sell Price
var float OpenPrice = na
OpenPrice := nz(OpenPrice[1])

// ————— Final Buy Price & Final Sell Price
var float FinalBuyPrice = na
FinalBuyPrice  := nz(FinalBuyPrice[1])
var float FinalSellPrice = na
FinalSellPrice := nz(FinalSellPrice[1])
var float FinalOpenPrice = na
FinalOpenPrice := nz(FinalOpenPrice[1])

// ————— Average Price
var int nBuys = na
nBuys := nz(nBuys[1])
var int nSells = na
nSells := nz(nSells[1])
var float sumBuy = na
sumBuy := nz(sumBuy[1])
var float sumSell = na
sumSell := nz(sumSell[1])
var float sumQtyBuy = na
sumQtyBuy := nz(sumQtyBuy[1])
var float sumQtySell = na
sumQtySell := nz(sumQtySell[1])
var float AveragePrice = na
AveragePrice := nz(AveragePrice[1])

// ———————————————————— Logic

if (WOption == 'PRICE')
    gridWidth = Width
else if (WOption == '% PP')
    gridWidth = Width * 0.01

if (ppPeriod == "Day")
    ppLength = 1
else if (ppPeriod == "Week")
    ppLength = 7
else if (ppPeriod == "15D")
    ppLength = 15
else 
    ppLength = 30

// ————— Determine Buy and Sell Levels
for i = 1 to ppLength
    var float levelBuyPrice = na
    levelBuyPrice := OpenPrice + gridWidth * (i - 1)
    
    strategy.entry("Buy" + tostring(i), strategy.long, qty = BuyQ)
    // Add a trailing stop or other conditions for buying
    
    if (levelBuyPrice > FinalBuyPrice)
        FinalBuyPrice := levelBuyPrice

for i = 1 to ppLength
    var float levelSellPrice = na
    levelSellPrice := OpenPrice + gridWidth * (i - 1)
    
    strategy.close("Sell" + tostring(i), comment = "Selling at " + str.tostring(levelSellPrice))
    // Add a trailing stop or other conditions for selling
    
    if (levelSellPrice > FinalSellPrice)
        FinalSellPrice := levelSellPrice

// ————— Calculate Average Price
AveragePrice := sumBuy / (sumQtyBuy + sumQtySell) if nBuys + nSells > 0 else na

// ———————————————————— Plotting and Alerts
plot(AveragePrice, color = color.blue)
alertcondition(AveragePrice > FinalSellPrice, title = "Profit Alert", message = "You have made a profit!")
```

This Pine Script code implements the Dynamic Grid Trading Management strategy. It includes input parameters for setting up grid levels and determining when to buy and sell based on price movements. The script also calculates an average price and provides alerts for potential profits.