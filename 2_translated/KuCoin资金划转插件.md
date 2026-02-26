Name

KuCoin fund transfer plug-in

Author

makebit



Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|assets|USDT|Transfer currency|
|amount|10000|Transfer amount|
|typeIndex|0|Transfer type: Transfer from spot account to USDT contract account<br>Transfer from USDT contract account to spot account|


Source (javascript)

``` javascript
var adress = ['/api/v1/transfer-in','/api/v3/transfer-out'][typeIndex]

function UsdtTransfer( e , cur , amount ){
    var params = ''
    var currency = cur
    var transfer amount = amount
    var exname = e.GetName()
    if(exname == 'Futures_KuCoin'){
        if( typeIndex == 0 ){
            paraStr = '&payAccountType=TRADE'
        }else if( typeIndex == 1 ){
            paraStr = '&recAccountType=TRADE'
        }

        params = "amount="+amount+"&currency="+currency + paraStr
        ret = e.IO("api","POST",adress, params )
        Log(currency, "Transfer quantity:", amount, ret)
    }
}

function main() {
    UsdtTransfer(exchange, assets, amount)
}
```


Detail

https://www.fmz.com/strategy/428110

Last Modified

2023-09-28 17:27:49