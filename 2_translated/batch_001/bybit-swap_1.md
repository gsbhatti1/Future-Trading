> Name

bybit-swap Perpetual Rolling Strategy

> Author

gulishiduan_高频排序

> Strategy Description

//Recently, some friends have reported a small bug. For now, the test network is being used. Parameters can be adjusted according to your needs. The essence of the strategy is to track the offset price of k-lines to judge long/short positions; in simple terms, it detects signals through the turning points of moving averages.
//If you're new to our service, please register using this link: https://www.bybit.com/en/register/?affiliate_id=7586&language=en&group_id=0&group_type=2
//This link provides access to multiple strategies./
//Basic principle: if k-lines continue to rise, continuously increase the position until the maximum leverage is reached.

//If long: unsuitable for short positions, but not increasing long positions during a decline.
//If short: unsuitable for long positions, but not increasing short positions during an uptrend.

//Note that both long and short positions can be opened in different accounts.

//For other strategy purchases, please consult via WeChat: ying5737
//You need to connect with the exchange yourself./Please test on a simulation account first. Be cautious of risks at your own discretion.


// At daily or weekly level, we will use daily as an example,
// detecting MA5 and MA10, if k-line closing price is above both MA5 and MA10, and MA5 is rising (judged by the previous day's closing price being greater than 5 days ago), then place a buy order or directly buy 500u every opening, continuously increasing as long as prices continue to rise.
// Increase position: if two consecutive down k-lines appear during an uptrend, add 500u on the third day. Each set of two consecutive down k-lines is counted separately.

// Sell: reduce by 1000u after three consecutive up k-lines (or 2000u after four consecutive up k-lines). The strategy runs for 13 days or 21 days, and automatically stops to close positions and orders.

The above images:

https://wx1.sinaimg.cn/mw1024/c5775633ly1gbsjvtrgnhj20m80dmmxy.jpg
https://wx1.sinaimg.cn/mw1024/c5775633ly1gbsjvty48uj20lr0u077o.jpg
https://wx2.sinaimg.cn/mw1024/c5775633ly1gbsjvu4iipj20lr0h775f.jpg

---

# Mid-frequency One-sided Trend Strategy
## Monitoring Variables
1. Fast MA
2. Slow MA
3. Closing Price
## Configuration Parameters
1. Single Order Volume Amount
2. Single Liquidation Volume CloseAmount
3. Maximum Position MaxPosition
## Long
### Necessary Conditions
1. K-line closing price is greater than fast MA and slow MA
2. And the fast MA is rising (judged by yesterday's closing price being greater than 5 days ago)
### Placing Orders
1. Reduce by CloseAmount after three consecutive up k-lines.
2. Add Amount during two consecutive down k-lines, which means placing an order for 2*Amount.
3. Normal situation, place a single order of Amount.
### Limits
1. Do not place orders if the maximum position exceeds MaxPosition.
### Exit
1. Exit after N bars have run.

## Short
### Necessary Conditions
1. K-line closing price is less than fast MA and slow MA
2. And the fast MA is falling (judged by yesterday's closing price being less than 5 days ago)
### Placing Orders
1. Reduce by CloseAmount after three consecutive down k-lines.
2. Add Amount during two consecutive up k-lines, which means placing an order for 2*Amount.
3. Normal situation, place a single order of Amount.
### Limits
1. Do not place orders if the maximum position exceeds MaxPosition.
### Exit
1. Exit after N bars have run.
## Notes
1. The program will acquire account information each time to determine the current position size.
2. Please bind your WeChat with FMZ for important notifications.

---

## Parameters
1. Fast MA Period
2. Slow MA Period	
3. Interval (ms)	
4. Long/Short Selection
5. Leverage Level: 0 represents full margin mode
6. Contract Type: Currently, only SWAP is supported on Fmex. Set to 'swap' in the interface for backtesting; can be set as this_week, next_month during backtesting.
7. Single Liquidation Volume. The amount to liquidate when a liquidation condition is met.
8. Maximum Position (u).
9. API Base URL. Can be set to https://api.fmex.com or testnet at https://api.testnet.fmex.com
10. Number of Bars for Strategy Exit. After how many bars will the strategy exit normally.
11. Whether to Liquidate Positions When Exiting. If a manual operation is required, it will wait for your intervention; otherwise, it exits directly.
12. Whether to Place Market Orders or Limit Orders: check this box to place market orders; uncheck to place limit orders with buy at the top of the order book and sell at the bottom.
13. Number of consecutive up k-lines (for long positions). A signal for reducing position, e.g., reduce if a series of up k-lines appear during long positions.
14. Number of consecutive down k-lines (for long positions). The number of consecutive down k-lines to trigger reductions in long positions.
15. Whether it is a volatile market: check this box for a volatile trading environment.

## Interaction
**Interaction is only valid when `Whether to Interact` is checked.**
**Interaction occurs during the normal exit of the strategy.**
1. Continue. This restarts the strategy with the same parameters.
2. Stop. The strategy exits.
3. Continue after switching market conditions: switch between volatile and trending markets, extending 1.

```javascript
////////////////// params ////////////////////////
var makeLong = direction == '做多' ? true : false;
var startTime = null;
var holdAmount = 0;
var lastBar = null;
var yinxianCnt = 0; // Down k-line count
var yangxianCnt = 0; // Up k-line count
var lastClose = 0;
var last5thClose = 0;
var fastMa = [];
var slowMa = [];
var barCnt = 0;
var localIsShock = false;

////////////////// variable ////////////////////////
var PreBarTime = 0;
var isFirst = true;

function PlotMA_Kline(records) {
    $.PlotRecords(records, 'K');
    if (fastMa.length == 0) {
        fastMa = TA.MA(records, fastMaPeriod);
    }
    if (slowMa.length == 0) {
        slowMa = TA.MA(records, slowMaPeriod);
    }
    if (isFirst) {
        $.PlotFlag(records[records.length - 1].Time, 'Start', 'STR');
        for (var i = records.length - 1; i >= 0; i--) {
            if (fastMa[i] !== null) {
                $.PlotLine('ma' + fastMaPeriod, fastMa[i], records[i].Time);
            }
            if (slowMa[i] !== null) {
                $.PlotLine('ma' + slowMaPeriod, slowMa[i], records[i].Time);
            }
        }
        PreBarTime = records[records.length - 1].Time;
        isFirst = false;
    } else {
        if (PreBarTime !== records[records.length - 1].Time) {
            $.PlotLine('ma' + fastMaPeriod, fastMa[fastMa.length - 2], records[fastMa.length - 2].Time);
            $.PlotLine('ma' + slowMaPeriod, slowMa[slowMa.length - 2], records[slowMa.length - 2].Time);
            PreBarTime = records[records.length - 1].Time;
        }
    }
}
```
```javascript
// Additional logic for trading and monitoring
function onBarUpdate(newRecords) {
    if (startTime === null) startTime = newRecords[newRecords.length - 1].Time;

    lastBar = newRecords[newRecords.length - 1];

    // Update moving averages
    fastMa.push(TA.MA(lastBar.Close, fastMaPeriod));
    slowMa.push(TA.MA(lastBar.Close, slowMaPeriod));

    // Check for long or short conditions and adjust positions accordingly.
    if (makeLong) {
        if (lastClose > last5thClose && fastMa[fastMa.length - 1] > slowMa[slowMa.length - 1]) {
            // Place buy order
            holdAmount += Amount;
            log('Buying at ' + lastBar.Time);
        } else if (yinxianCnt === 2) {
            // Reduce position after two consecutive down k-lines during an uptrend.
            holdAmount -= CloseAmount;
            yinxianCnt = 0;
            log('Reducing position at ' + lastBar.Time);
        }
    } else {
        if (lastClose < last5thClose && fastMa[fastMa.length - 1] < slowMa[slowMa.length - 1]) {
            // Place sell order
            holdAmount -= CloseAmount;
            log('Selling at ' + lastBar.Time);
        } else if (yangxianCnt === 2) {
            // Increase position after two consecutive up k-lines during a downtrend.
            holdAmount += Amount;
            yangxianCnt = 0;
            log('Increasing position at ' + lastBar.Time);
        }
    }

    lastClose = lastBar.Close;
    last5thClose = TA.Candle(lastRecords, 5).Close; // Assuming there's a function to get the closing price of the 5th bar.
}
```

This script provides a basic framework for implementing and monitoring your strategy. Ensure that you test thoroughly in a simulated environment before deploying it with real funds. Adjustments may be necessary based on specific market conditions and requirements.