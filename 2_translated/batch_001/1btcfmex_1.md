> Name

1btc起fmex多头解锁策略后市看多

> Author

gulishiduan_高频排序

> Strategy Description

**FMex排序挖矿多头版本代码使用说明**

// Margin market risk is huge; you may face 100% loss at any time. There might be unknown bugs leading to a 100% loss, and we are not responsible.
// (If considering holding short or in a range-bound market, the parameters and code can be flexibly modified accordingly.)
// The current maximum position size is calculated as of now; it is recommended to keep within 0.5-3 times this amount. For instance, with 0.1B at 3x leverage, the turnover position would be approximately 2700, with a maximum position of 3200. If adjusted to 10x leverage, the turnover position would be around 9000u, and the maximum position would be 10000u; adjustments can be made between 300-500u.
// Live trading address: https://api.fmex.com Testnet: https://api.fmextest.net/ Note: First manually hold long 1-1000u.
// (Contact WeChat: ying5737)
**Strategy Principle:**

![](http://https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg)
The image is for reference.
https://wx1.sinaimg.cn/mw690/c5775633ly1gaajdxk8a8j20u10f4dhx.jpg

Random order placement in the market / This strategy defaults to maintaining a long position /
Note: First hold long 1-1000u. //
**- Detect if current orders exceed limits; cancel them immediately if they do/
- Detect if an order forms a position; reduce the position when it exceeds xxu, below the predefined limit**

**Several Order Scenarios:**

**Global Orders:**
Orders are specifically defined as remote sorting for market making strategies. Parameters can be adjusted and currently around 8 levels.

**Market Makers (Near-end Order Placement):**
Maximum long positions can be customized; if exceeded, approximately every 6 seconds the position will be reduced until it is below the custom parameter.
Maximum short positions can also be customized; if exceeded, approximately every 6 seconds the position will be reduced until it is below the custom parameter.
A reduction in long positions strategy will start when the long position exceeds a certain threshold, with orders primarily as shorts: resulting in short positions.
If the short position exceeds 1u, a reduction in short positions strategy will start, with orders mainly as longs:极易成交多单
Normal holding (random market fluctuations leading to occasional long trades)

**// Notes for parameter references, for your reference, and you can add levels accordingly. Reference:**

 order = createOrderPrice({
 symbol: "BTCUSD_P",
type: "LIMIT",
direction: "SHORT",// Choose between long or short, short or long
post_only: true,
price: lastPrice + 5.5,// Adjust the number to be a multiple of 0.5 or its multiples
quantity: sp_perAmount,
affiliate_code: "9y40d8"
})

******You are solely responsible for risk/Parameters can be adjusted, contact WeChat: ying5737******
**Optimization Directions: Add moving averages or candlestick comparisons to determine direction, optimize levels, and add customizable order volumes, etc.******

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| Url | https://api.fmex.com | Exchange API address; change to the live version if needed: https://api.fmex.com |
| maxPrice | 30000 | Maximum price in the range |
| minPrice | 9000 | Minimum price in the range |
| g_maxHoldingLong | 21000 | Maximum long position size |
| g_maxHoldingShort | 5000 | Maximum short position size |
| sp_baseAmountLong | 18000 | Position control: limit for converting to short from long positions |
| sp_baseAmountShort | 600 | Position control: limit for reducing short positions when they exceed a certain amount |
| sp_perAmount | 800 | Market maker level: single order quantity. (Market-making order quantity = market maker order quantity * 3) (Normal short order quantity = market maker order quantity * 0.6) |
| Interval | 3 | Polling time (default parameters are fine) |
| RetryInterval | 5000 | Retry interval in milliseconds (default parameters are fine) |
| Debug | true | Display retry records (default parameters are fine) |
| EnableErrorFilter | false | Hide common network error messages in retry records (default parameters are fine) |
| ApiList | GetAccount,GetDepth,GetTicker,GetRecords,GetTrades,GetOrders,SetContractType | Retry API list (default parameters are fine) |

> Source Code (JavaScript)

```javascript
// Margin market risk is huge; you may face 100% loss at any time. There might be unknown bugs leading to a 100% loss, and we are not responsible. The leverage used in this strategy is relatively small, so feel free to experience it.
// Note: By default, the near-end sorting does not start (leaves space for manual closeout). For the long version, initially hold long 1-1000u; for the short version, initially hold short 1-1000u. This is used to activate the near-end sorting.
var eName = exchange.GetName();
if (eName == "Futures_FMex") {
    exchange.IO("extend", '{"POST/v3/contracts/orders$":{"affiliate_code":"9y40d8"}}');
} else if (eName == "FCoin") {
    exchange.IO("extend", '{"POST/v2/orders$":{"affiliate_code":"9y40d8"}}');
}
exchange.IO("base", Url); // (Contact WeChat: ) This strategy is only for personal use. If used for commercial dissemination, please contact us beforehand.
var ordersInfo = {
    buyId: 0,
    buyPrice: 0,
    sellId: 0,
    sellPrice: 0,
    minPrice: 0,
    maxPrice: 0
};
var depthInfo = {
    asks: [],
    bids: []
};
var symbol = "BTCUSD_P";
function getTicker(symbol) {
    url = "/v2/market/ticker/" + symbol;
    data = _C(exchange.IO, "api", "GET", url);
    return data.data;
}
function getAccounts() {
    data = _C(exchange.IO, "api", "GET", "/v3/contracts/accounts");
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
    resultData = _C(exchange.IO, "api", "GET", "/v3/contracts/orders/open");
    return resultData.data;
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
    resultData = _C(exchange.IO, "api", "GET", "/v3/broker/auth/contracts/positions");
    return resultData.data;
}
function getMatches(id) {
    resultData = _C(exchange.IO, "api", "GET", "/v3/contracts/orders/" + id + "/matches");
    return resultData.data;
}
function getCandles(resolution, symbol) {
    resultData = _C(exchange.IO, "api", "GET", "/v2/market/candle/" + resolution + "/" + symbol);
    return resultData.data;
}
function underElephant(ticker) {
    var buyPrice = ticker[2];
    var sellPrice = ticker[4];
    var bestAskAmount = ticker[5];
    var bestBidAmount = ticker[3];
    var now = new Date().getTime();
    if (hasElephantOrder) {
        if (now - elephantOrderTime < 3000) {
            return;
        }
        // for (var index = 0; index < elephantOrder.length; index++) {
        //     cancelOrder(elephantOrder[index].id);
        //     Sleep(1000);
        // }
        hasElephantOrder = false;
    }
}
```