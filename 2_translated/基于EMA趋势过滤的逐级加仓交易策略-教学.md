> Name

Trend Filtering Step-by-Step Position Increasing Trading Strategy - Teaching

> Author

Inventor Quantitative - XiaoXiaoMeng



> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|targetProfit|Target Profit|Target Profit|
|amount|Order Volume|Order Volume|
|totalEq|Initial Total Equity|Initial Total Equity|
|isReset|Reset|Reset|
|pricePrecision|Price Precision|Price Precision|
|amountPrecision|Order Volume Precision|Order Volume Precision|
|isSimulate|If the added exchange object is the API KEY of OKEX_V5 simulation disk, check this option to switch to the simulation disk|OKEX_V5 Simulation Disk Option|
|ratio|Addition and Liquidation Distance Ratio|Addition and Liquidation Distance Ratio|
|contractType|Contract Code|Contract Code|
|isAmountForUSDT|Place orders in U, write 100 to indicate a position value of 100U|Place Orders in U|
|oneCtValue|One contract value, one coin per contract on Binance, for example, one ETH contract is worth 0.1 ETH on OKX.|Contract Value|
|setAddCounter|Force set the number of additions to recover when switching devices|Force Set Number of Additions|
|reserve|Margin Reserve Percentage|Margin Reserve Percentage|
|marginLevel||Leverage Ratio|
|maxAddCounter|Maximum Addition Count|Maximum Addition Count|
|isDoubling|Whether to double the addition, check for doubling addition|Double Addition Option|
|interval|Polling Interval|Polling Interval|
|isMaxAddCounterClear|Clear position when reaching maximum addition count|Clear Position When Reaching Maximum Addition Count|


> Source (javascript)

``` javascript
/*backtest
start: 2024-10-01 00:00:00
end: 2025-04-23 00:00:00
period: 1h
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
args: [["targetProfit",20],["amount",20],["amountPrecision",3],["isAmountForUSDT",true]]
*/

function getTotalEquity_OKEX_V5() {
    var totalEquity = null 
    var ret = exchange.IO("api", "GET", "/api/v5/account/balance", "ccy=USDT")
    if (ret) {
        try {
            totalEquity = parseFloat(ret.data[0].details[0].eq)
        } catch(e) {
            Log("Failed to get total equity!")
            return null
        }
    }
    return totalEquity
}

function getTotalEquity_Binance() {
    var totalEquity = null 
    var ret = exchange.GetAccount()
    if (ret) {
        try {
            totalEquity = parseFloat(ret.Info.totalWalletBalance)
        } catch(e) {
            Log("Failed to get total equity!")
            return null
        }
    }
    return totalEquity
}

function getTotalEquity() {
    var exName = exchange.GetName()
    if (exName == "Futures_OKCoin") {
        return getTotalEquity_OKEX_V5()
    } else if (exName == "Futures_Binance") {
        return getTotalEquity_Binance()
    } else {
        throw "Unsupported exchange"
    }
}

function ceilToDecimals(value, decimals) {
    const factor = Math.pow(10, decimals);
    return Math.ceil(value * factor) / factor;
}

function cancelAll() {
    while (1) {
        var orders = _C(exchange.GetOrders)
        if (orders.length == 0) {
            break
        }
        for (var i = 0 ; i < orders.length ; i++) {
            exchange.CancelOrder(orders[i].Id, orders[i])
            Sleep(interval)
        }
        Sleep(interval)
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

function plotRecords(c, buyOrder, sellOrder, pos) {
    var bars = _C(exchange.GetRecords)
    if (bars.length == 0) {
        return  
    }

    bars.forEach(function(bar, index) {
        c.begin(bar)
        if (index == bars.length - 1) {
            if (buyOrder) {
                c.hline(buyOrder.Price, "buy", "rgba(255, 0, 0, 0.2)", "dotted")
            }
            if (sellOrder) {
                c.hline(sellOrder.Price, "sell", "rgba(0, 255, 0, 0.2)", "dotted")
            }
            if (pos && pos.length == 1) {
                c.hline(pos[0].Price, "pos", "rgba(0, 0, 255, 0.2)", "dashed")
            }
        }
        c.close()
    })
}

var buyOrderId = null
var sellOrderId = null
var logStatusMsgBuff = ""

function main() {
    var exName = exchange.GetName()    
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

    exchange.SetContractType(contractType)
    exchange.SetPrecision(pricePrecision, amountPrecision)
    Log("Set precision", pricePrecision, amountPrecision)
    exchange.SetMarginLevel(marginLevel)

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

    var addCounter = _G("addCounter")
    if (!addCounter) {
        addCounter = 1
        if (setAddCounter != -1) {
            addCounter = setAddCounter
        }
        _G("addCounter", addCounter)
    } else {
        addCounter -= 1
    }

    let c = KLineChart({
        overlay: true
    })
    
    var isLock = false 
    while (true) {
        var ticker = _C(exchange.GetTicker)        
        var pos = _C(exchange.GetPosition)
        if (pos.length > 1) {
            Log(pos)
            throw "Multiple positions exist"
        }

        var r = _C(exchange.GetRecords, 60 * 60)
        var ema = TA.EMA(r, 60)
        if (Math.abs(ticker.Last - ema[ema.length - 2]) / ema[ema.length - 2] > 0.03) {
            cancelAll()
            isLock = true 
        }
        if (Math.abs(ticker.Last - ema[ema.length - 2]) / ema[ema.length - 2] < 0.02) {
            isLock = false 
        }
        if (isLock) {
            LogStatus(_D(), "Paused, threshold detected: ", _N(Math.abs(ticker.Last - ema[ema.length - 2]) / ema[ema.length - 2], 3), logStatusMsgBuff)
            plotRecords(c, null, null, pos)
            Sleep(interval)
            continue 
        }
```