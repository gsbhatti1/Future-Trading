```markdown
Name

Python version of simple grid strategy teaching

Author

Inventor Quantification-Little Dream

Strategy Description

https://www.fmz.com/bbs-topic/4877


Source(python)

```python
'''
backtest
start: 2019-07-01 00:00:00
end: 2020-01-03 00:00:00
Period: 1m
exchanges: [{"eid":"OKEX","currency":"BTC_USDT"}]
'''

import json

# Parameters
beginPrice = 5000
endPrice = 8000
distance=20
pointProfit=50
amount = 0.01
minBalance = 300

# Global variables
arrNet = []
arrMsg = []
acc=None

def findOrder (orderId, NumOfTimes, ordersList = []):
    for j in range(NumOfTimes) :
        orders=None
        if len(ordersList) == 0:
            orders = _C(exchange.GetOrders)
        else :
            orders = ordersList
        for i in range(len(orders)):
            if orderId == orders[i]["Id"]:
                return True
        Sleep(1000)
    return False

def cancelOrder (price, orderType):
    orders = _C(exchange.GetOrders)
    for i in range(len(orders)) :
        if price == orders[i]["Price"] and orderType == orders[i]["Type"]:
            exchange.CancelOrder(orders[i]["Id"])
            Sleep(500)

def checkOpenOrders (orders, ticker):
    global arrNet, arrMsg
    for i in range(len(arrNet)) :
        if not findOrder(arrNet[i]["id"], 1, orders) and arrNet[i]["state"] == "pending" :
            orderId = exchange.Sell(arrNet[i]["coverPrice"], arrNet[i]["amount"], arrNet[i], ticker)
            if orderId :
                arrNet[i]["state"] = "cover"
                arrNet[i]["id"] = orderId
            else :
                # Undo
                cancelOrder(arrNet[i]["coverPrice"], ORDER_TYPE_SELL)
                arrMsg.append("Pending order failed!" + json.dumps(arrNet[i]) + ", time:" + _D())

def checkCoverOrders (orders, ticker):
    global arrNet, arrMsg
    for i in range(len(arrNet)) :
        if not findOrder(arrNet[i]["id"], 1, orders) and arrNet[i]["state"] == "cover" :
            arrNet[i]["id"] = -1
            arrNet[i]["state"] = "idle"
            Log(arrNet[i], "Node is closed and reset to idle state.", "#FF0000")


def onTick () :
    global arrNet, arrMsg, acc

    ticker = _C(exchange.GetTicker)
    for i in range(len(arrNet)):
        if i != len(arrNet) - 1 and arrNet[i]["state"] == "idle" and ticker.Sell > arrNet[i]["price"] and ticker.Sell < arrNet[i + 1]["price"]:
            acc = _C(exchange.GetAccount)
            if acc.Balance < minBalance :
                arrMsg.append("Insufficient funds" + json.dumps(acc) + "!" + ", time:" + _D())
                break

            orderId = exchange.Buy(arrNet[i]["price"], arrNet[i]["amount"], arrNet[i], ticker)
            if orderId :
                arrNet[i]["state"] = "pending"
                arrNet[i]["id"] = orderId
            else :
                # Cancel order
                cancelOrder(arrNet[i]["price"], ORDER_TYPE_BUY)
                arrMsg.append("Pending order failed!" + json.dumps(arrNet[i]) + ", time:" + _D())
            Sleep(1000)
            orders = _C(exchange.GetOrders)
            checkOpenOrders(orders, ticker)
            Sleep(1000)
            orders = _C(exchange.GetOrders)
            checkCoverOrders(orders, ticker)

tbl = {
    "type" : "table",
    "title" : "Grid Status",
    "cols" : ["Node Index", "Details"],
    "rows" : [],
}

for i in range(len(arrNet)) :
    tbl["rows"].append([i, json.dumps(arrNet[i])])

errTbl = {
    "type" : "table",
    "title" : "record",
    "cols" : ["Node Index", "Details"],
    "rows" : [],
}

orderTbl = {
    "type" : "table",
    "title" : "orders",
    "cols" : ["Node Index", "Details"],
    "rows" : [],
}

while len(arrMsg) > 20 :
    arrMsg.pop(0)

for i in range(len(arrMsg)) :
    errTbl["rows"].append([i, json.dumps(arrMsg[i])])

for i in range(len(orders)) :
    orderTbl["rows"].append([i, json.dumps(orders[i])])

LogStatus(_D(), "\n", acc, "\n", "arrMsg length:", len(arrMsg), "\n", "`" + json.dumps([tbl, errTbl, orderTbl]) + "`")


def main():
    global arrNet
    for i in range(int((endPrice - beginPrice) / distance)):
        arrNet.append({
            "price" : beginPrice + i * distance,
            "amount" : amount,
            "state" : "idle", # pending / cover / idle
            "coverPrice" : beginPrice + i * distance + pointProfit,
            "id" : -1,
        })

    while True:
        onTick()
        Sleep(500)
```

> Detail

https://www.fmz.com/strategy/180385

> Last Modified

2020-01-04 14:42:23
```