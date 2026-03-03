Name

OKex Futures Test for Newbies

Author

District Class Quantification

Strategy Description

OKex futures can be complicated to use, so I wrote this framework to make it easier for new users to understand and use. Note that ETH is priced at $10 per coin.

Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|Interval|10|Polling period (seconds)|
|mnum|20|30 minute line period|
|initRatio|0.5|Initial position ratio|


Source (javascript)

``` javascript
/*backtest
start: 2019-01-01 00:00:00
end: 2019-10-10 00:00:00
Period: 1d
exchanges: [{"eid":"OKEX","currency":"ETH_USDT","stocks":0}]
args: [["OpMode",1,10989],["MaxAmount",1,10989],["TradeFee",0.001,10989]]
*/
//After registering for Bihu https://m.bihu.com/signup?i=1ewtKO&s=4&c=4
//Search for IoT blockchain and you can contact the author area leader
var isInit = 1; // Indicates initial state
function oper(){
    var allAmount;
    var cashRatio;
    var lastPrice;
    var wantRatio;
    var wantOper=0;//The expected operation, 0 does not operate, 1 buys, -1 sells
    var mhigh;
    var mlow;

    var mrecords = exchange.GetRecords(PERIOD_M30);
    //High and low points within a certain period
    mhigh=TA.Highest(mrecords, mnum, 'High');
    mlow=TA.Lowest(mrecords, mnum, 'Low');

    var midLine = (mhigh+mlow)/2;

    var ticker = _C(exchange.GetTicker);
    var nowPrice=ticker.Sell;
    var account = _C(exchange.GetAccount);
    var objid;
    var order;

    if (isInit == 1) { //Initialization state is the default warehouse;
        /*exchange.SetDirection("sell");
        objid = exchange.Sell(nowPrice,Math.floor(nowPrice*account.Stocks*0.2/10)); //Okex must be rounded
        order = exchange.GetOrder(objid); //The parameter id is the order number, you need to fill in the number of the order you want to query

        if (objid) { //If the purchase is successful
            isInit=2; //Initialization successful
            account = _C(exchange.GetAccount);
            Log(account);
            Log("fair price",midLine,"high point",mhigh,"low point",mlow);
            Log("Information about the order just placed, ID:", order.Id, "Price:", order.Price, "Amount:", order.Amount,
            "DealAmount:", order.DealAmount, "type:", order.Type);
        }*/

        exchange.SetDirection("buy");
        objid = exchange.Buy(nowPrice,Math.floor(nowPrice*account.Stocks*0.2/10)); //Okex must be rounded
        order = exchange.GetOrder(objid); //The parameter id is the order number, you need to fill in the number of the order you want to query

        if (objid) { //If the purchase is successful
            isInit=2; //Initialization successful
            account = _C(exchange.GetAccount);
            Log(account);
            Log("fair price",midLine,"high point",mhigh,"low point",mlow);
            Log("Information about the order just placed, ID:", order.Id, "Price:", order.Price, "Amount:", order.Amount,
            "account.Stocks:", account.Stocks, "type:", order.Type);
        }

        exchange.SetDirection("buy");
        objid = exchange.Buy(nowPrice,Math.floor(nowPrice*account.Stocks*0.2/10)); //Okex must be rounded
        order = exchange.GetOrder(objid); //The parameter id is the order number, you need to fill in the number of the order you want to query

        if (objid) { //If the purchase is successful
            isInit=2; //Initialization successful
            account = _C(exchange.GetAccount);
            Log(account);
            Log("fair price",midLine,"high point",mhigh,"low point",mlow);
            Log("Information about the order just placed, ID:", order.Id, "Price:", order.Price, "Amount:", order.Amount,
            "DealAmount:", order.DealAmount, "type:", order.Type);
        }
    }else if(isInit==2){ //Daily operation detection
        //Print untraded positions
        var orders = _C(exchange.GetOrders);

        for (var i = 0; i < orders.length; i++) {
            Log("Place an order",orders[i]);
        }

        var positions = exchange.GetPosition();
        Log("number of positions",positions.length);
        for (i = 0; i < positions.length; i++) { //The next two long orders will be merged into one order
            if (positions[i].Type == PD_LONG) {
                //exchange.SetDirection("closebuy");
                //exchange.Sell(nowPrice,positions[i].Amount);
            } else {
                // exchange.SetDirection("closesell");
                // exchange.Buy(nowPrice,positions[i].Amount);
            }
            Log("position",positions[i]);
        }
        //If there is no pending order or holding order
        if(orders.length<2){//&&positions.length==0){
            isInit=3;
            account = _C(exchange.GetAccount);
            Log("Dealed");
            Log(account);
        }
    }else{
    }
}

function main() {
    var initAccount = _C(exchange.GetAccount);
    Log(initAccount);
    exchange.SetContractType("quarter") // For example, set to OKEX futures current week contract
    exchange.SetMarginLevel(5); //Set leverage to 5 times
    while (true) {
        oper();
        Sleep(Interval*1000);
    }
}
```


Detail

https://www.fmz.com/strategy/170842

Last Modified

2020-02-20 19:45:23