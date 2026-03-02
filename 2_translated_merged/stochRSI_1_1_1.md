```javascript
/*Parameters
stochRSI indicator parameters   Array     [14,14,3,3]
Use spot digital currency trading class library
*/
var stochRSI_P_arr = "[14,14,3,3]";


var Interval = 500;

var long = 1;
var free = 0;
var state = free; //Reset each time when opening or closing position
var buyInfo = null; //Reset each time when closing position
var sellInfo = null; //Reset each time when opening position
var initAccount = null; //Reset each time when closing position
var beginAccount = null; //No reset
var Profit = 0; //Realized profit and loss
var prefloatProfit = 0;//Previous floating profit and loss, updated by trailing stop loss
var openBalance = 0;//Opening position amount
var isCover = false;

var NowPositionInfo = {//Position information, updated each time when closing position
    avgPrice: 0,
    amount: 0 ,
    floatProfit: 0
};

function openUpdate(){//Update after opening position
    state = long;
    sellInfo = null;
}
function closeUpdate(){//Update after closing position
    state = free;
    addLevel = 0;
    buyInfo = null;
    initAccount = _C(exchange.GetAccount);
    NowPositionInfo.avgPrice = 0;
    NowPositionInfo.amount = 0;
    NowPositionInfo.floatProfit = 0;
    isCover = true;
}

function Calculate(nowAccount,nowDepth){//Calculate and update profit, floating profit and loss, average position price, and position amount
    if(typeof(nowAccount) === 'undefined' ){
        nowAccount = _C(exchange.GetAccount);
        nowDepth = _C(exchange.GetDepth);
    }
    var diff_stocks = nowAccount.Stocks - initAccount.Stocks;//Difference in coins
    var diff_balance = nowAccount.Balance - initAccount.Balance;//Difference in money
    NowPositionInfo.avgPrice = Math.abs(diff_balance) / Math.abs(diff_stocks);
    NowPositionInfo.amount = Math.abs(diff_stocks);
    NowPositionInfo.floatProfit = diff_balance + diff_stocks * nowDepth.Bids[0].Price; //Floating profit and loss of this transaction
    Profit = (initAccount.Stocks - beginAccount.Stocks) * nowDepth.Bids[0].Price + (initAccount.Balance - beginAccount.Balance); //Realized profit and loss

    //Update into interface
}

function LLV(array,period){
    if(!array || array.length - period < 0){
        throw "error:" + array;
    }
    var min = array[array.length - period];
    for(var i = array.length - period; i < array.length; i++){
        if( array[i] < min ){
            min = array[i];
        }
    }
    return min;
}

function HHV(array,period){
    if(!array || array.length - period < 0){
        throw "error:" + array;
    }
    var max = array[array.length - period];
    for(var i = array.length - period; i < array.length; i++){
        if( array[i] > max){
            max = array[i];
        }
    }
    return max;
}

function DeleteNullEle(initArr){
    var dealArr = [];
    var initArrLen = initArr.length;
    for(var i = 0,j = 0 ; i < initArrLen ; i++,j++){
        if(initArr[i] === null || isNaN(initArr[i]) ){
            j--;
            continue;
        }
        dealArr[j] = initArr[i];
    }
    return dealArr;
}

/*
LC := REF(CLOSE,1); //REF(C,1) Previous cycle's closing price
RSI:=SMA(MAX(CLOSE-LC,0),N,1)/SMA(ABS(CLOSE-LC),N,1) *100;
％K:     MA(RSI-LLV(RSI,M),P1)/MA(HHV(RSI,M)-LLV(RSI,M),P1)*100;  LLV(l,60) means: retrieve the lowest price within 60 days, can be applied to retrieve any stock
％D:MA(％K,P2);

LC := REF(CLOSE,1);
RSI:=SMA(MAX(CLOSE-LC,0),N,1)/SMA(ABS(CLOSE-LC),N,1) *100;
STOCHRSI:MA(RSI-LLV(RSI,M),P1)/MA(HHV(RSI,M)-LLV(RSI,M),P1)*100;
*/
function FstochRSI(records,n,m,p1,p2){
    var len = records.length;
    //var LC = records[len-2];//Previous cycle's closing price
    //var rsi = TA.RSI(records,n);// RSI array, talib
    var rsi = talib.RSI(records,n);
    rsi = DeleteNullEle(rsi);//test
    //Log("rsi:",rsi) //Test
    //Log("rsi:",rsi);//test
    //throw "stop";//test
    table.e5 = "rsi :" + rsi[rsi.length-1] + "rsi[-1]:" + rsi[rsi.length-2];//test

    var arr1 = [];
    var arr2 = [];
    var arr3 = [];
    var arr4 = [];
    var rsi_a = [];
    var rsi_b = [];
    var k = [];
    var d = null;

    /*Does not include current bar
    for(var a = 0 ;a < rsi.length ; a++ ){//Modified without using LLV
        for(var aa = 0 ; aa <= a; aa++ ){
            rsi_a.push(rsi[aa]);
        }
        arr1.push(rsi[a] - TA.Lowest(rsi_a,m));
    }
    for(var b = 0 ;b < rsi.length ; b++ ){//Modified without using HHV
        for(var bb = 0 ; bb <= b; bb++ ){
            rsi_b.push(rsi[bb]);
        }
        arr2.push(TA.Highest(rsi_b,m) - TA.Lowest(rsi_b,m));
    }
    */
    for(var a = 0 ;a < rsi.length ; a++ ){//Modified without using LLV
        if(a < m){
            continue;
        }
        for(var aa = 0 ; aa <= a; aa++ ){
            rsi_a.push(rsi[aa]);
        }
        arr1.push(rsi[a] - LLV(rsi_a,m));
    }
    for(var b = 0 ;b < rsi.length ; b++ ){//Modified without using HHV
        if(b < m){
            continue;
        }
        for(var bb = 0 ; bb <= b; bb++ ){
            rsi_b.push(rsi[bb]);
        }
        arr2.push(HHV(rsi_b,m) - LLV(rsi_b,m));
    }

    arr1 = DeleteNullEle(arr1);
    arr2 = DeleteNullEle(arr2);
    //Log("arr1:",arr1.length,"-",arr1);//test
    //Log("arr2:",arr2.length,"-",arr2);//test

    arr3 = talib.MA(arr1,p1);
    arr4 = talib.MA(arr2,p1);

    arr3 = DeleteNullEle(arr3);
    arr4 = DeleteNullEle(arr4);

    //Log("test");//test
    var c = 0;
    var diff = 0;
    if(arr3.length !== arr4.length){//Actual measurement shows unequal lengths
        throw "error: !=" + arr3.length + "----" + arr4.length;
        diff = arr4.length - arr3.length; //example   diff  =   10  -   6
    }else{
        //throw "error:" + arr3.length + "----" + arr4.length;
    }

    for( ;c < arr3.length ; c++ ){
        k.push(arr3[c] / arr4[c + diff] * 100);
    }
    
    d = talib.MA(k,p2);

    return [k,d,rsi];
}

function Loop(){//Main loop body
    /*
    var go_account = exchange.Go("GetAccount");
    var go_records = exchange.Go("GetRecords");
    var go_depth = exchange.Go("GetDepth");

    var account = go_account.wait(1000);
    var records = go_records.wait(1000);
    var depth = go_depth.wait(1000);
    
    if(account === null || records === null || depth === null){
        //Display exception
        return;
    }
    */
    //
    var account = _C(exchange.GetAccount);
    var records = _C(exchange.GetRecords);
    var depth = _C(exchange.GetDepth);
    //Test

    var len = records.length - 1;

    if(records.length < array_P[0] || records.length < array_P[1] || records.length < array_P[2] || records.length < array_P[3] ){
        //Output to status bar table, showing insufficient K-line length
        msg = "Insufficient K-line length, fetching...";
        return;
    }
    
    //*
    var records_close = [];
    for(var i = 0; i <= len; i++){
        records_close.push(records[i].Close);
    }
    //*/

    msg = "K line `s length:" + (len + 1);

    //var ma = TA.MA(records,3);//Test using MA3
    
    //var stochRSI = talib.STOCHRSI(records,array_P[0],array_P[1],array_P[2],array_P[3]);
    //var stochRSI = talib.STOCHRSI(records_close,14,3,3,3);
    var stochRSI = FstochRSI(records,14,14,3,3);
    var fastLine = stochRSI[0]; //stochrsi
    var slowLine = stochRSI[1]; // ma(k,3)
    
    //Log("fastLine:",fastLine);//test
    //Log("slowLine:",slowLine);//test
    //var slowLine = ma;
    //var rsi = stochRSI[2];
    
    $.Draw(records);
    $.AddZhiBiao(fastLine,records,1);
    $.AddZhiBiao(slowLine,records,2);
    if(isFirst === true){
        $.SignOP((new Date()).getTime(),null,null,3,"Chart display started!");// Test marking custom information on chart
        Log(array_P[0],array_P[1],array_P[2],array_P[3],typeof(array_P[3]));//test
        isFirst = false;
    }
    table.a4 = "fastLine[len]:" + _N(fastLine[fastLine.length-1],2);
    table.b4 = "slowLine[len]:" + _N(slowLine[slowLine.length-1],2);

    table.a5 = "fastLine[len-1]" + _N(fastLine[fastLine.length-2],2);
    table.b5 = "slowLine[len-1]" + _N(slowLine[slowLine.length-2],2);
    table.c5 = "fastLine[len-2]" + _N(fastLine[fastLine.length-3],2);
    table.d5 = "slowLine[len-2]" + _N(slowLine[slowLine.length-3],2);
    //table.e5 = "rsi:" + rsi[rsi.length - 1] + "rsi[-2]:" + rsi[rsi.length - 2] + "rsi[-3]:" + rsi[rsi.length - 3];


    table.b1 = "stock:" + account.Stocks + "#ff00ff";
    table.c1 = "Fstock:" + account.FrozenStocks + "#ff00ff";
    table.d1 = "balance:" + account.Balance + "#ff00ff";
    table.e1 = "Fbalance:" + account.FrozenBalance + "#ff00ff";
    table.b2 = "open:" + records[len].Open;
    table.c2 = "high:" + records[len].High;
    table.d2 = "low:" + records[len].Low;
    table.e2 = "close:" + records[len].Close;
    table.b3 = "bids[0].price:" + depth.Bids[0].Price;
    table.c3 = "bids[0].amount:" + depth.Bids[0].Amount;
    table.d3 = "asks[0].price:" + depth.Asks[0].Price;
    table.e3 = "asks[0].amount:" + depth.Asks[0].Amount;

    table.c4 = "avgPrice:" + NowPositionInfo.avgPrice;
    table.d4 = "amount:" + NowPositionInfo.amount;
    table.e4 = "floatProfit:" + NowPositionInfo.floatProfit;

    
    if(isCover === true){
        LogProfit(Profit);
        isCover = false;
    }
    Calculate();//
    //Log("test2");//test2
    $.UpDateChart(records);
    //Log("test2");//test2
}

var table = null;
var array_P = null;
var msg = "";//Message displayed at the top of the status bar table
var isFirst = true;

function main(){
    //Initialization
    beginAccount = _C(exchange.GetAccount);//Initial account information when program starts running
    initAccount = beginAccount;//Account information before each opening position
    table = $.TableInit(5,6);
    table.a1 = "account:" + "#ff00ff";
    table.a2 = "records[length-1]:";
    table.a3 = "depth.Bids[0]/Asks[0]:";
    table.a0 = "beginAccount:";
    table.b0 = "stock:" + beginAccount.Stocks;
    table.c0 = "Fstock:" + beginAccount.FrozenStocks;
    table.d0 = "balance:" + beginAccount.Balance;
    table.e0 = "Fbalance:" + beginAccount.FrozenBalance;

    array_P = JSON.parse(stochRSI_P_arr);// Parse stochRSI parameters
    

    while(true){
        Loop();
        $.UpDateLogStatus(msg);
        msg = "";
        Sleep(Interval);
    }
}

/*Tasks
1. Complete UI interface display
2. Write interactive module well
3. Trading logic
4. Parameter settings
5. Visual charts
*/
```