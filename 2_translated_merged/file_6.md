Name

Trading terminal plug-in example

Author

Inventor Quantification-Little Dream

Strategy Description

Used to demonstrate the trading terminal plug-in embedding function.
https://www.fmz.com/api#%E4%BA%A4%E6%98%93%E6%8F%92%E4%BB%B6

Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|TransactionTimes|Number of transactions|Number of transactions|
|Amount|Coins per transaction|Coins per transaction|
|Side|Trading direction|Trading direction|


Source (javascript)

``` javascript
function main() {
    var initAcc = _C(exchange.GetAccount)
    var tbl = {
        "type": "table",
        "title": "Table",
        "cols": ["project", "content"],
        "rows": [],
    }

    for (var i = 0 ; i < TransactionTimes ; i++) {
        var info = null
        if (Side == 0) {
            info = $.Buy(Amount)
        } else if (Side == 1) {
            info = $.Sell(Amount)
        } else {
            throw "side error!"
        }

        tbl.rows.push([i + "Order number, transaction status: ", JSON.stringify(info)])
        Sleep(300)
    }

    var nowAcc = _C(exchange.GetAccount)
    Log("balance:", nowAcc.Balance)
    delete initAcc.Info
    delete nowAcc.Info
    tbl.rows.push(["Initial account:", JSON.stringify(initAcc)])
    tbl.rows.push(["Account after execution:", JSON.stringify(nowAcc)])
    return tbl
}
```


Detail

https://www.fmz.com/strategy/187708

Last Modified

2025-04-08 16:12:39