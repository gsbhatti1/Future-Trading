> Name

Three-EMA System Exodus

> Author

Exodus[Strategy Writer]

> Strategy Description

This system is a two-way contract strategy that takes long or short positions based on certain conditions. The order volume is equal to the number of contracts; when using Binance, the order volume will be in BTC units; when using Huobi, the order volume unit is in lots.
【Updated 7-31】
The parameters of this strategy are suitable for operation on a 1-hour timeframe, but since the trading frequency during the hour is too low, it has been updated to a minute-level timeframe. However, manual adjustment of parameters may be required for the minute level.

Below are the backtest results based on hourly cycles.
**** April 27 - July 25 ****
Initial Capital: $300, Order Volume: 0.04 BTC
![IMG](https://www.fmz.com/upload/asset/1f4e9984f53d575c506c1.png)
**** January 1 - July 25 ****
Initial Capital: $300, Order Volume: 0.03 BTC (0.04 order volume resulted in insufficient capital)
Please backtest to determine your own order volume if you wish to use this strategy live.
![IMG](https://www.fmz.com/upload/asset/1f47c59a9ac1f93694193.png)

If you make money, consider supporting the author.
![IMG](https://www.fmz.com/upload/asset/1f4c36c1fca8b23e727c7.jpg)

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|afterEmaCrossTime|4|After an EMA crossover, how many bars must pass before MACD conditions are met for trading to be allowed|
|buyVolume|0.016|Trade volume (0.016 BTC)|
|stopLossRate|true|Stop loss rate (not including leverage)|
|winLossRate|5|Profit-to-loss ratio|
|period|60|Timeframe (in minutes)|
|EMA1|8|Fastest EMA cycle period|
|EMA2|34|Middle speed EMA cycle period|
|EMA3|89|Slowest EMA cycle period|
|MACD1|16|MACD parameter 1|
|MACD2|26|MACD parameter 2|
|MACD3|9|MACD parameter 3|

> Source (JavaScript)

```javascript
/*backtest
start: 2021-04-27 00:00:00
end: 2021-07-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT","balance":300}]
args: [["afterEmaCrossTime",4],["buyVolume",0.04],["winLossRate",5]]
*/

function GetCrossStatus(a, lastA, b, lastB) {
    let lastStatus = lastA < lastB;
    let curStatus = a < b;
    let crossStatus = 0; //0表示没有交叉，1表示金叉，2表示死叉
    //判断金叉还是死叉,同时判断此刻大于0轴或者小于0轴,因为在此系统中要求金叉时macd>0才有意义，死叉时macd<0才有意义
    if (curStatus != lastStatus) //状态不同时表示金叉或者死叉了
    {
        if (a > b) {
            crossStatus = 1; //金叉
        }
        if (a < b)
            crossStatus = 2; //死叉
    }
    return crossStatus;
}
var lastOpenTime;

function GetCurRecord(records) {
    return records[records.length - 1];
}

function GetCurTime(records) {
    return GetCurRecord(records).Time;
}

function GetCurPrice(records) {
    return GetCurRecord(records).Close;
}

function Open(direction) {
    let pos = exchange.GetPosition()[0];

    if (pos != null) {
        return;
    }
    let amount = buyVolume;
    if (direction == 1) { //做多
        Log("做多", amount);
        exchange.SetDirection("buy");
        exchange.Buy(-1, amount);
    }
    if (direction == 2) { //做空
        Log("做空", amount);
        exchange.SetDirection("sell");
        exchange.Sell(-1, amount);
    }
    
}

function Close(ticker, fastLine, midLine) {
    let pos = exchange.GetPosition()[0];

    if (pos == null) {
        return;
    }
    
    if (pos.Type == PD_LONG) {
        if (ticker.Last < pos.Price * (1 - stopLossRate / 100) || ticker.Last > pos.Price * (1 + (stopLossRate * winLossRate) / 100)) {
            Log("平多, 开仓价为:", pos.Price, "本次盈利:", pos.Profit);
            exchange.SetDirection("closebuy");
            exchange.Sell(-1, pos.Amount);
            
        }
    }
    if (pos.Type == PD_SHORT) {
        if (ticker.Last > pos.Price * (1 + stopLossRate / 100) || ticker.Last < pos.Price * (1 - (stopLossRate * winLossRate) / 100)) {
            Log("平空, 开仓价为:", pos.Price, "本次盈利:", pos.Profit);
            exchange.SetDirection("closesell");
            exchange.Buy(-1, pos.Amount);
        }
    }
}




var lastEmaCrossTime = 0;
var lastMacdCrossTime = 0;

function NearMacdCross(time) {
    //Log("MACD", time, lastMacdCrossTime, time - lastMacdCrossTime);
    return time - lastMacdCrossTime <= afterEmaCrossTime * 1000 * 3600;
}

function NearEmaCross(time) {
    //Log("EMA", time, lastMacdCrossTime, time - lastMacdCrossTime);
    return time - lastEmaCrossTime <= afterEmaCrossTime * 1000 * 3600;
}


var emaMeet = 0; //0表示不满足，1满足做多条件，2满足做空条件
var macdMeet = 0; //判断MACD是否满足条件,0表示不满足，1表示做多条件满足，2表示做空条件满足
function main() {
    exchange.SetContractType("swap");
    while (1) {
        let r = exchange.GetRecords(PERIOD_M1 * period);

        //************均线EMA****************
        let emaChart8 = TA.EMA(r, EMA1);
        let emaChart34 = TA.EMA(r, EMA2);
        let emaChart89 = TA.EMA(r, EMA3);

        let ema8 = emaChart8;
        let curEma8 = ema8[emaChart8.length - 1];
        let lastEma8 = ema8[emaChart8.length - 2];

        let ema34 = emaChart34;
        let curEma34 = ema34[emaChart34.length - 1];
        let lastEma34 = ema34[emaChart34.length - 2];

        let ema89 = emaChart89;
        let curEma89 = ema89[emaChart89.length - 1];
        let lastEma89 = ema89[emaChart89.length - 2];

        //判断8均线和34均线的死叉和金叉，当金叉时如果当前实体在ema89均线以上做多，当死叉时如果实体在ema89以下时做空      
        let ticker = exchange.GetTicker();
        let low = ticker.Low;
        let high = ticker.High;
        let close = ticker.Close;

        Close(ticker, curEma8, curEma34);

        //auto Open(ticker, curEma8, curEma34);  // This line was commented out and not translated

        //************MACD****************
        let macd = macdChart[1];
        let dif = macdChart[0];
        let curMacd = macd[curMacd];
        let lastMacd = macd[lastMacd];
        let curDif = dif[curDif];
        let lastDif = dif[lastDif];

        //判断金叉还是死叉,同时判断此刻大于0轴或者小于0轴
        if (curMacd < 0 != lastMacd < 0) {

            if (curMacd > 0) {
                macdMeet = 1;
                Log("macd金叉", lastMacd, curMacd);
                lastMacdCrossTime = GetCurTime(r);
            }
            if (curMacd < 0) {
``` 

It seems the script was cut off. The rest of the function should handle the MACD crossover logic and possibly open positions based on these conditions. If you need further details or corrections, please provide more context or complete the code snippet. Based on what's provided, this part handles the MACD crossovers and updates the `macdMeet` flag accordingly. You can continue to implement the rest of the function as needed. 

Would you like me to complete the function for you? If so, could you provide more context or specify how the logic should proceed after identifying a MACD crossover? For instance, do you want to open positions based on these crossovers, or is there another condition that needs to be met before placing orders? Please let me know. 

Here's an example of how it might continue:

```javascript
                if (curMacd < 0) {
                    macdMeet = 2;
                    Log("macd死叉", lastMacd, curMacd);
                    lastMacdCrossTime = GetCurTime(r);
                }
            }
        }

        // Place orders based on EMA and MACD conditions
        if (emaMeet == 1 && macdMeet == 1) {
            Open(1);  // Long position
        } else if (emaMeet == 2 && macdMeet == 2) {
            Open(2);  // Short position
        }
    }
}
```

This is just an example. The actual logic for opening positions might vary based on your specific strategy requirements. Please clarify or provide more details as needed!