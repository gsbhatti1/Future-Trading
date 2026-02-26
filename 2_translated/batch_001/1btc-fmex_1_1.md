---

Name

1btc起fmex多头解锁策略后市看多

Author

gulishiduan_高频排序

Strategy Description

**FMex排序挖矿多头版本代码使用说明**

//Margin market risk is significant, you may face up to 100% loss. There may be unknown bugs causing a 100% loss; the developer is not liable.
//(If considering holding short or in a range-bound market, parameters and code thresholds can be flexibly modified accordingly.)
//Currently, the maximum position size (conversion calculation), it's recommended to keep within 0.5-3 times the leverage. For example, with 0.1B at a 3x leverage, the converted position would be approximately 2700u, and the maximum position is 3200u; if adjusted to 10x leverage, then the converted position would be 9000u, and the maximum position would be 10000u. The quantity can be adjusted between 300-500u.
//Production URL: https://api.fmex.com Test Network: https://api.fmextest.net//Note: Manually open a long position of 1-1000u first.
//(Contact WeChat: ying5737)

**Strategy Principle:**

![](http://https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg)
Image for reference only
https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg

Random order placement / The strategy defaults to favoring long positions/
Note: Initially hold a long position of 1-1000u.//
**- Detect if existing orders exceed the limit, and cancel them immediately if they do/
- Check if there is any formation of a position due to trade; if it exceeds xxu, reduce the position to below the set position**

**Several Order Placement Scenarios:**

**Global Orders:**
Defined as remote sorting. Parameters can be adjusted, currently around 8 levels.

**Market Makers (Near-end order placement):**
Maximum long position is user-defined. If greater than this position, approximately every 6 seconds reduce the position until it falls below the defined parameter.
Maximum short position is user-defined. If greater than this position, approximately every 6 seconds reduce the position until it falls below the defined parameter.
If positions exceed the long position threshold, initiate a strategy to reduce long positions with orders as shorts: sell off empty positions.
If positions exceed 1u for short positions, initiate a strategy to reduce short positions with orders as longs: prone to instantly sell long positions
Normal holdings (random fill of buy orders due to market fluctuations)

**//Remarks on parameters are for reference only, additional levels can be added.** Reference example:

```javascript
order = createOrderPrice({
    symbol: "BTCUSD_P",
    type: "LIMIT",
    direction: "SHORT",//Choose between long and short, short or long
    post_only: true,
    price: lastPrice + 5.5,//Adjustable digit, 0.5 or multiples of 0.5
    quantity: sp_perAmount,
    affiliate_code: "9y40d8"
})
```

******Risk自负/Parameters are adjustable, contact WeChat: ying5737**
**Optimization Directions: Integrate moving averages or candlestick comparisons to determine direction, optimize level settings, and add custom order quantities/etc.******

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|Url|https://api.fmex.com|Exchange API address; use https://api.fmex.com for the production version|
|maxPrice|30000|Upper price limit of the range|
|minPrice|9000|Lower price limit of the range|
|g_maxHoldingLong|21000|Maximum long position size|
|g_maxHoldingShort|5000|Maximum short position size|
|sp_baseAmountLong|18000|Position control: Limit for converting from long to short positions|
|sp_baseAmountShort|600|Position control: Threshold for reducing short positions when they exceed the limit|
|sp_perAmount|800|Market maker sorting: Single quantity. (Depth order single quantity = Market maker single quantity * 3) (Normal short order single quantity = Market maker single quantity * 0.6)|
|Interval|3|Polling interval (default parameters are acceptable)|
|RetryInterval|5000|Retrying interval in milliseconds (default parameters are acceptable)|
|Debug|true|Display retry records (default parameters are acceptable)|
|EnableErrorFilter|false|Shield common network error messages from display during retries (default parameters are acceptable)|
|ApiList|GetAccount, GetDepth, GetTicker, GetRecords, GetTrades, GetOrders, SetContractType|Retry API list (default parameters are acceptable)|

> Source Code (JavaScript)

```javascript
//Margin market risk is significant, you may face up to 100% loss. There may be unknown bugs causing a 100% loss; the developer is not liable. The leverage used by this strategy is relatively small and can be safely experienced.
//Note: Default near-end sorting does not start (to reserve space for manual closing), initially hold a long position of 1-1000u, short position of 1-1000u to activate the near-end sorting
var eName = exchange.GetName();
if (eName == "Futures_FMex") {
    exchange.IO("extend", '{"POST/v3/contracts/orders$":{"affiliate_code":"9y40d8"}}');
} if (eName == "FCoin") {
    exchange.IO("extend", '{"POST/v2/orders$":{"affiliate_code":"9y40d8"}}');
}
exchange.IO("base", Url); //（Contact WeChat:）The strategy is for personal use only; please contact us before using it for commercial purposes.
var ordersInfo = {
    buyId: 0,    buyPrice: 0,    sellId: 0,    sellPrice: 0,    minPrice: 0,    maxPrice: 0
}
var depthInfo = {
    asks: [],
    bids: []
}
var symbol = "BTCUSD_P"
function getTicker(symbol) {
    url = "/v2/market/ticker/" + symbol;
    data = _C(exchange.IO,"api", "GET", url);
    return data.data;
}    
function getAccounts() {
    data = _C(exchange.IO,"api", "GET", "/v3/contracts/accounts")
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
    resultData = exchange.IO("api", "POST", "/v3/contracts/orders/" + id + "/cancel");//+ id 
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
}
```