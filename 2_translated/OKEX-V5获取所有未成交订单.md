```markdown
Name

OKEX-V5 gets all unfilled orders

Author

I won’t hit you in the summer



Source (javascript)

``` javascript


function getAllPendingOrdersInOkex(num) {
var pending_orders = [];

// limit order
var param = "instType=SWAP";
var ret = exchanges[num].IO("api", "GET", "/api/v5/trade/orders-pending", param);
// Take profit and stop loss order
param = "instType=SWAP" + "&ordType=oco,conditional";
var ret2 = exchanges[num].IO("api", "GET", "/api/v5/trade/orders-algo-pending", param);

if (!ret) {
Log(exchanges[num].GetLabel(), ": Failed to obtain limit price order!", "@");
return null;
}
if (!ret2) {
Log(exchanges[num].GetLabel(), ": Failed to obtain stop-profit and stop-loss orders!", "@");
return null;
}

for (let i = 0; i < ret.data.length; i++) {
let type = "";
if (ret.data[i].posSide == "long") {
type = ret.data[i].side == "buy" ? "Open long at limit price" : "Close long at limit price";
} else if (ret.data[i].posSide == "short") {
type = ret.data[i].side == "sell" ? "Open short at limit price" : "Sell short at limit price";
} else {
type = "Wrong pending order type";
}
let symbol = ret.data[i].instId.replace("-USDT-SWAP", "") + "_USDT";
pending_orders.push({
OrderId: ret.data[i].ordId,
Symbol: symbol,
Price: Number(ret.data[i].px),
Amount: Number(ret.data[i].sz),
DealAmount: Number(ret.data[i].accFillSz),
Type: type,
StopPrice: 0,
TakeProfitPrice: 0,
Time: ret.data[i].uTime,
});
}
for (let i = 0; i < ret2.data.length; i++) {
let type = "";
let stop_price = 0;
let take_profit_price = 0;
if (ret2.data[i].slTriggerPx && ret2.data[i].tpTriggerPx) {
type = ret2.data[i].posSide == "long" ? "Take profit and stop loss for long orders" : "Take profit and stop loss for short orders";
stop_price = Number(ret2.data[i].slTriggerPx);
take_profit_price = Number(ret2.data[i].tpTriggerPx);
} else if (ret2.data[i].slTriggerPx) {
type = ret2.data[i].posSide == "long" ? "Stop loss for long orders" : "Stop loss for short orders";
stop_price = Number(ret2.data[i].slTriggerPx);
} else if (ret2.data[i].tpTriggerPx) {
type = ret2.data[i].posSide == "long" ? "Take profit for long orders" : "Take profit for short orders";
take_profit_price = Number(ret2.data[i].tpTriggerPx);
} else {
type = "Wrong pending order type";
}
let symbol = ret2.data[i].instId.replace("-USDT-SWAP", "") + "_USDT";
pending_orders.push({
OrderId: ret2.data[i].algoId,
Symbol: symbol,
Price: 0,
Amount: Number(ret2.data[i].sz),
DealAmount: 0,
Type: type,
StopPrice: stop_price,
TakeProfitPrice: take_profit_price,
Time: ret2.data[i].cTime,
});
}

return pending_orders;
}

function main() {
getAllPendingOrdersInOkex(0);
}
```

Detail

https://www.fmz.com/strategy/340779

Last Modified

2022-01-14 22:29:20
```