> Name

1btc起fmex多头解锁策略后市看多

> Author

gulishiduan_高频排序

> Strategy Description

**FMex排序挖矿多头版本代码使用说明**

//Margin trading market carries significant risk; you may face a 100% loss at any time. There might be unknown bugs leading to a 100% loss, and we are not responsible.
//(If considering holding short or facing a range-bound market, corresponding parameters and code barriers can be flexibly adjusted.)
//Currently, the maximum position (conversion calculation) is recommended within 0.5-3 times. If you have 0.1B, with a 3x leverage, the converted position will be approximately 2700, with a maximum of 3200. Adjusting to 10x leverage would set the converted position at 9000u and a maximum of 10000u; the trade volume can be adjusted between 300-500u.
//Live trading address: https://api.fmex.com Testnet: https://api.fmextest.net//Note: Manually open long position with 1u to 1000u first.
//(Contact WeChat: ying5737)
**Strategy Principle:**

![](http://https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg)
Image for reference only
https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg

Random order placement to fill the market / The strategy defaults to maintaining a long position.
Note: First, manually open a long position with 1u-1000u.//
**- Detect if existing orders exceed limits; cancel such an order immediately if they do/
- Detect if any position is formed and reduce it below the set position size if the quantity exceeds xxu/**

**Several types of pending orders:**

**Global Orders:**
Defined specifically as far-end orders for arbitrage strategies. Parameters can be adjusted, currently around 8 levels.

**Market Makers (Near-end Order Book):**
Maximum long positions are customizable; if they exceed this position, approximately every 6 seconds, the position is reduced until it falls below the custom parameter.
The maximum short positions are also customizable; if they exceed this position, approximately every 6 seconds, the position is reduced until it falls below the custom parameter.
A reduction in long positions is triggered when a long position exceeds the defined threshold, with orders primarily focused on short: filled with empty positions.
A reduction in short positions is initiated when a short position exceeds 1u, with orders mainly for long: highly likely to be quickly filled by new buy orders.
Normal position (random fill of buy orders based on market fluctuations).

**//Comments and descriptions in the parameters are for reference only; additional levels can also be added as needed.** Refer to:

```javascript
order = createOrderPrice({
  symbol: "BTCUSD_P",
  type: "LIMIT",
  direction: "SHORT", // choose between long or short, 'short' or 'long'
  post_only: true,
  price: lastPrice + 5.5, // adjust the number to a multiple of 0.5
  quantity: sp_perAmount,
  affiliate_code: "9y40d8"
})
```

******
Disclaimer / Parameters can be adjusted; contact WeChat: ying5737
Optimization directions: Add moving averages or candlestick comparisons for direction determination, optimize level settings, and add customizable trade volumes.
******

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|Url|https://api.fmex.com|Trading API address; use the production version if needed: https://api.fmex.com|
|maxPrice|30000|Upper price limit of the range|
|minPrice|9000|Lower price limit of the range|
|g_maxHoldingLong|21000|Maximum long position size|
|g_maxHoldingShort|5000|Maximum short position size|
|sp_baseAmountLong|18000|Position control: restriction for converting to short from long positions|
|sp_baseAmountShort|600|Position control: restriction for converting to long from short positions|
|sp_perAmount|800|Market maker order quantity. (The depth level quantity is three times the market maker order quantity; normal empty orders are 60% of the market maker order quantity)|
|Interval|3|Polling interval (default parameters apply)|
|RetryInterval|5000|Retry interval in milliseconds for fault tolerance (default parameters apply)|
|Debug|true|Display retry records (default parameters apply)|
|EnableErrorFilter|false|Suppress common network error messages when displaying retry records (default parameters apply)|
|ApiList|GetAccount, GetDepth, GetTicker, GetRecords, GetTrades, GetOrders, SetContractType|Fault-tolerant API list (default parameters apply)|


> Source (javascript)

```javascript
//Margin trading market carries significant risk; you may face a 100% loss at any time. There might be unknown bugs leading to a 100% loss, and we are not responsible. This strategy uses relatively small leverage, so it can be safely experienced.
//Note: The near-end order placement is not automatically enabled by default (reserves space for manual liquidation), long version initially opens a position with 1u-1000u, short version opens a position with 1u-1000u to activate the near-end order book.
var eName = exchange.GetName();
if (eName == "Futures_FMex") {
    exchange.IO("extend", '{"POST/v3/contracts/orders$":{"affiliate_code":"9y40d8"}}');
} 
if (eName == "FCoin") {
    exchange.IO("extend", '{"POST/v2/orders$":{"affiliate_code":"9y40d8"}}');
}
exchange.IO("base", Url); // (Contact WeChat: ) The strategy is for personal use only; if used for commercial purposes, prior contact is required.
var ordersInfo = {
    buyId: 0,
    buyPrice: 0,
    sellId: 0,
    sellPrice: 0,
    minPrice: 0,
    maxPrice: 0
}
var depthInfo = {
    asks: [],
    bids: []
}
var symbol = "BTCUSD_P"
function getTicker(symbol) {
    url = "/v2/market/ticker/" + symbol;
    data = _C(exchange.IO, "api", "GET", url);
    return data.data;
}    
function getAccounts() {
    data = _C(exchange.IO, "api", "GET", "/v3/contracts/accounts")
    return data.data;
}
function createOrderPrice(body) {
    parameter = "symbol=" + body.symbol + "&type=" + body.type + "&direction=" + body.direction + "&post_only=" + body.post_only +  "&price=" + body.price + "&quantity=" + body.quantity + "&affiliate_code=9y40d8";   
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders", parameter)
    return resultData;
}
function createOrder(body) {
    parameter = "symbol=" + body.symbol + "&type=" + body.type + "&direction=" + body.direction + "&quantity=" + body.quantity + "&affiliate_code=9y40d8";   
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders", parameter)    
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
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders/" + id + "/cancel"); //+ id 
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
    resultData = _C(exchange.IO, "api", "GET", "/candle/" + resolution + "/" + symbol);
    return resultData.data;
}
function underElephant(ticker) {
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
} ```