> Name

Final-Formula-by-TraderShaman

> Author

TraderShaman

> Strategy Description

TWITTER: https://twitter.com/TraderShaman

TELEGRAM: https://t.me/tradershaman

Hello.

You can see the performance of my trades in the charts.
For all my charts: https://www.fmz.com/user/6261c777972a854f5c0460520f9206bd

You can also view more details and earnings rates on TraderWagon:
https://www.traderwagon.com/en/portfolio/3886?ref=zoh4wq9

By becoming a member of the trade platform called TraderWagon, which was established in partnership with Binance, it is possible to copy my positions with one click at the rate of your own volume.

For special - discount membership with reduced commission rates:
https://www.traderwagon.com/en/register?ref=zoh4wq9

With the slogan "Variable formulas for the volatile market", I update the values of the formula I have been working on for a long time on a daily basis. It is not possible for fixed formulas to remain healthy in this volatile market in the long run.

I make futures transactions on 4 or 5 coins that I have determined by examining detailed historical correlations. I also make changes in these coins when I deem necessary.

I update my volume and transaction rate daily according to the formulas I have created after careful and long-term studies.

I prevent liquidation to the maximum extent with carefully determined different profit taking and cost reduction points.


However, these transactions are not entirely risk-free.

I promise not high gains, but small, lossless and stable gains.

https://www.traderwagon.com/en/portfolio/3886?ref=zoh4wq9

TELEGRAM: https://t.me/tradershaman

TWITTER: https://twitter.com/TraderShaman

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|targetProfit|5|Target profit percentage|
|amount|0.05|Order amount|
|totalEq|-1|Initial total equity|
|isReset|false|Reset flag|
|pricePrecision|2|Price precision|
|amountPrecision|2|Amount precision|
|isSimulate|false|OKEX_V5 simulation option|
|SpecifyPosField||Specify position field to display|
|showLine|false|Show line chart|


> Source (javascript)

``` javascript
// OKEX V5 Get total equity
function getTotalEquity_OKEX_V5() {
    var totalEquity = null 
    var ret = exchange.IO("api", "GET", "/api/v5/account/balance", "ccy=USDT")
    if (ret) {
        try {
            totalEquity = parseFloat(ret.data[0].details[0].eq)
        } catch(e) {
            Log("Failed to get account total equity!")
            return null
        }
    }
    return totalEquity
}

// Binance Futures
function getTotalEquity_Binance() {
    var totalEquity = null 
    var ret = exchange.GetAccount()
    if (ret) {
        try {
            totalEquity = parseFloat(ret.Info.totalWalletBalance)
        } catch(e) {
            Log("Failed to get account total equity!")
            return null
        }
    }
    return totalEquity
}

// dYdX
function getTotalEquity_dYdX() {
    var totalEquity = null 
    var ret = exchange.GetAccount()
    if (ret) {
        totalEquity = ret.Balance
    }
    return totalEquity
}

function getTotalEquity() {
    var exName = exchange.GetName()
    if (exName == "Futures_OKCoin") {
        return getTotalEquity_OKEX_V5()
    } else if (exName == "Futures_Binance") {
        return getTotalEquity_Binance()
    } else if (exName == "Futures_dYdX") {
        return getTotalEquity_dYdX()
    } else {
        throw "Unsupported exchange"
    }
}

function cancelAll() {
    while (1) {
        var orders = _C(exchange.GetOrders)
        if (orders.length == 0) {
            break
        }
        for (var i = 0 ; i < orders.length ; i++) {
            exchange.CancelOrder(orders[i].Id, orders[i])
            Sleep(500)
        }
        Sleep(500)
    }
}

function trade(distance, price, amount) {
    var tradeFunc = null 
    if (distance == "buy") {
        tradeFunc = exchange.Buy
    } else if (distance == "sell") {
        tradeFunc = exchange.Sell
    } else if (distance == "closebuy") {
        tradeFunc = exchange.Sell
    } else {
        tradeFunc = exchange.Buy
    }
    exchange.SetDirection(distance)
    return tradeFunc(price, amount)
}

function openLong(price, amount) {
    return trade("buy", price, amount)
}

function openShort(price, amount) {
    return trade("sell", price, amount)
}

function coverLong(price, amount) {
    return trade("closebuy", price, amount)
}

function coverShort(price, amount) {
    return trade("closesell", price, amount)
}

var buyOrderId = null
var sellOrderId = null

function main() {
    var exName = exchange.GetName()
    
    // Switch to OKEX V5 simulation if required
    if (isSimulate && exName == "Futures_OKCoin") {
        exchange.IO("simulate", true)
    }

    if (isReset) {
        _G(null)
        LogReset(1)
        LogProfitReset()
        LogVacuum()
        Log("All data reset", "#FF0000")
    }

    exchange.SetContractType("swap")
    exchange.SetPrecision(pricePrecision, amountPrecision)
    Log("Setting precision", pricePrecision, amountPrecision)

    if (totalEq == -1 && !IsVirtual()) {
        var recoverTotalEq = _G("totalEq")
        if (!recoverTotalEq) {
            var currTotalEq = getTotalEquity()
            if (currTotalEq) {
                totalEq = currTotalEq
                _G("totalEq", currTotalEq)
            } else {
                throw "Failed to get initial equity"
            }
        } else {
            totalEq = recoverTotalEq
        }
    }

    while (1) {
        var ticker = _C(exchange.GetTicker)
        var pos = _C(exchange.GetPosition)
        if (pos.length > 1) {
            Log(pos)
            throw "Multiple positions open"
        }
        
        // Based on state
        if (pos.length == 0) {   // No position held, calculate profit
            if (!IsVirtual()) {
                var currTotalEq = getTotalEquity()
                if (currTotalEq) {
                    LogProfit(currTotalEq - totalEq, "Current total equity:", currTotalEq)
                }
            }

            buyOrderId = openLong(ticker.Last - targetProfit, amount)
            sellOrderId = openShort(ticker.Last + targetProfit, amount)
        } else if (pos[0].Type == PD_LONG) {   // Long position held
```