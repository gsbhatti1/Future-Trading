> Name

1btc Start Fmex Short Unlock Strategy Posterior Outlook Bearish

> Author

gulishiduan_高频排序

> Strategy Description

FMex sorting mining short version code usage instructions. (Note the API address) (WeChat: ying5737)
(Expect a slow daily decline of over 1%, earn coins and mines; otherwise, there may be significant losses.)
Margin market risk is huge; you may face up to 100% loss at any time. There could be bugs causing 100% loss without warranty.

Principle: Random order placement in the market/
First short position with 1-1000u.//
- Check if existing orders exceed boundaries, and cancel them immediately if they do.
- Check if there is a formed position due to transactions; reduce it to below the predetermined amount if it exceeds xxu.

Several scenarios:
Global order hanging: Distinguish from market maker strategies by defining remote sorting as hanging orders. Parameters are adjustable.
Market Maker:
If maximum long position exceeds this level, approximately every 6 seconds, reduce the position.
If maximum short position exceeds this level, approximately every 6 seconds, reduce the position.
Start reducing long positions when over 1u of a long position is initiated with primary focus on short orders.
Start reducing short positions when over the short position threshold, focusing mainly on long orders for hanging.
Normal holding.

// Notes on parameters for reference; additional levels can be added
Self-bear responsibility/Parameters adjustable. WeChat: ying5737

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|Url|https://api.fmex.com|Exchange API address|
|maxPrice|30000|Maximum price in the range|
|minPrice|9000|Minimum price in the range|
|g_maxHoldingLong|5000|Maximum long position quantity|
|g_maxHoldingShort|32000|Maximum short position quantity|
|sp_baseAmountShort|25000|If short position exceeds this amount, prioritize trading long positions|
|sp_perAmount|600|Market maker order depth (depth order volume = market maker order volume * 3; normal long order volume = market maker order volume * 0.8)|
|sp_baseAmountLong|500|If the long position exceeds this number, adjust to prioritize trading short orders|
|Interval|3|Polling time interval (default parameters are acceptable)|
|RetryInterval|1000|Retrying interval in milliseconds (default parameters are acceptable)|
|Debug|true|Display retry records (default parameters are acceptable)|
|EnableErrorFilter|false|Shields common network errors from the retry record (default parameters are acceptable)|
|ApiList|GetAccount,GetDepth,GetTicker,GetRecords,GetTrades,GetOrders,SetContractType|API error tolerance list (default parameters are acceptable)|


> Source (javascript)

``` javascript
// Margin market risk is huge; you may face up to 100% loss. There could be bugs causing 100% loss without warranty. The leverage used in this strategy is relatively small, so feel free to experience it.
// Note: Default near-end sorting not activated (leaves space for manual liquidation), long version first positions 1u-1000u, short version first positions 1u-1000u, activates near-end sorting
var eName = exchange.GetName();
if (eName == "Futures_FMex") {
    exchange.IO("extend", '{"POST/v3/contracts/orders$":{"affiliate_code":"9y40d8"}}');
} else if (eName == "FCoin") {
    exchange.IO("extend", '{"POST/v2/orders$":{"affiliate_code":"9y40d8"}}');
}
exchange.IO("base", Url); // (Contact WeChat: ying5737) Strategy for personal use only, please contact us in advance if you plan to commercialize it.
var ordersInfo = {
    buyId: 0,    buyPrice: 0,    sellId: 0,    sellPrice: 0,    minPrice: 0,    maxPrice: 0
};
var depthInfo = {
    asks: [],
    bids: []
};
var symbol = "BTCUSD_P";
function getTicker(symbol) {
    url = "/v2/market/ticker/" + symbol;
    data = _C(exchange.IO,"api", "GET", url);
    return data.data;
}
function getAccounts() {
    data = _C(exchange.IO,"api", "GET", "/v3/contracts/accounts");
    return data.data;
}
function createOrderPrice(body) {
    parameter = "symbol=" + body.symbol + "&type=" + body.type + "&direction=" + body.direction + "&post_only=" + body.post_only +  "&price=" + body.price + "&quantity=" + body.quantity + "&affiliate_code=9y40d8";   
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders", parameter);
    return resultData;
}
function createOrder(body) {
    parameter = "symbol=" + body.symbol + "&type=" + body.type + "&direction=" + body.direction + "&quantity=" + body.quantity + "&affiliate_code=9y40d8";   
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders", parameter);    
    return resultData;
}
function getOrders() {
    resultData = _C(exchange.IO,"api", "GET", "/v3/contracts/orders/open");
    return resultData.data
}
function cancelOrder(id) {
    if (typeof(id) == 'undefined') {
        return
    }
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders/" + id + "/cancel"); 
    return resultData;    
}
function cancelAllOrder() {
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders/cancel");
    return resultData;    
}
function getPosition() {
    resultData = _C(exchange.IO,"api", "GET", "/v3/broker/auth/contracts/positions");
    return resultData.data;
}
function getMatches(id) {
    resultData = _C(exchange.IO,"api", "GET", "/v3/contracts/orders/" + id + "/matches");
    return resultData.data;
}
function getCandles(resolution, symbol) {
    resultData = _C(exchange.IO,"api", "GET", "/v2/market/candles/" + resolution + "/" + symbol);
    return resultData.data;
}

function cleanPosition() {
    res = getPosition();    
    res.results.forEach(function(it) {
        if (it.symbol == symbol) {
            if (it.quantity) {
                if (it.quantity > g_maxHoldingLong && it.direction.toUpperCase() == 'LONG') { 
                    data = createOrder({symbol: symbol,type: "MARKET",direction: "SHORT",quantity:sp_perAmount * 2
                    });
                    Log("LONG exceeds max holding, reducing");
                }
                if (it.quantity > g_maxHoldingShort && it.direction.toUpperCase() == 'SHORT') {
                    data = createOrder({symbol: symbol,type: "MARKET",direction: 'LONG',quantity: sp_perAmount * 2
                    });
                    Log("SHORT exceeds max holding, reducing");
                }
            }
        }
    });
}
// add new 
var hasElephantOrder = false
// var elephantOrder  = []
var elephantOrderTime = 0
function underElephant (ticker) {
    var buyPrice = ticker[2] 
    var sellPrice = ticker[4] 
    var bestAskAmount = ticker[5];
    var bestBidAmount = ticker[3];
    var now = new Date().getTime()
    if (hasElephantOrder) {
        if (now - elephantOrderTime < 3000) {
            return
        }
       // for (var index = 0; index < elephantOrder.length; index++) {
       //     cancelOrder(elephantOrder[index].id)
       //     Sleep(1000)
       // }
       hasElephantOrder = false
    }
    if (bestBidAmount > 40000 && bestBidAmount > bestAskAmount * 2) {
        // If the bid price is greater than X ten thousand and the bid amount is more than twice the ask amount, place an order.
        // Wait for cancellation. Re-check and re-order.       
       // elephantOrder.push(order.data)
      //  order = createOrderPrice({symbol: symbol,type: "LIMIT",direction: "LONG",post_only: true,price: buyPrice - 2,quantity: sp_perAmount * 2 })
      //  Log("Elephant order to buy 4 LONG" );
       order = createOrderPrice({symbol: symbol,type: "LIMIT",direction: "LONG",post_only: true,price: buyPrice - 3,quantity: sp_perAmount * 3})
       Log("Elephant order to buy 6 LONG" );
       // elephantOrder.push(order.data)
        order = createOrderPrice({symbol: symbol,type: "LIMIT",direction: "LONG",post_only: true,price: buyPrice - 4,quantity: sp_perAmount * 3})
        Log("Elephant order to buy 8 LONG" );        
        // elephantOrder.push(order.data)
        order = createOrderPrice
```