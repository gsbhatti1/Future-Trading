``` markdown
---
Name

My-1-Value-Averaging-Investment-Strategy

Author

Lizza

Strategy Description

Live Trading: [https://www.fmz.com/m/robot/26018](https://www.fmz.com/m/robot/26018)
This strategy is suitable for long-term Bitcoin believers. It uses a value averaging approach to invest regularly, effectively mitigating market volatility (read about value averaging on Baidu).

The basic idea is to decide how much money you want to invest each month (Strategy Variable: MoneyEveryMonth), and then determine the frequency of transactions; it's not recommended to trade less than every 5 minutes (Strategy Parameter: InvestInternal).

Here’s an example to illustrate the strategy and trading opportunities:
Assume that you want to buy Bitcoin with a value of 72,000 RMB per month (for easy calculation), and plan to trade once every hour. This means you will trade approximately 24 * 30 = 720 times each month, with each planned investment amounting to 72000 / 720 = 100 RMB (Variable A).

|Hour B|Current Price C|Total Invested Funds D|Bitcoin Bought E|Value of Bitcoins F|Investment Funds This Time G|Bitcoin Bought This Time H|
|---|---|---|---|---|---|---|
|1|400|0|0|C*E=0|A*B-F=100|G/C=0.25|
|2|200|100|0.25|200 * 0.25 = 50|100 * 2 - 50 = 150|0.75|
|3|1000|250|1|1000|100 * 3 - 1000 = -700|-0.7|
|4|500|-550|0.3|150|100 * 4 - 150 = 250|0.5|

After this, your total investment is 300 RMB, and you have bought approximately 0.8 BTC (worth 400 RMB), with an average price of 375 RMB.

Note: The program checks the difference between the current account balance and Bitcoin holdings from when it was started to calculate how much needs to be purchased each time. Therefore, do not use the same account with other robots or perform manual buys/sells. If there are deposits/withdrawals on the exchange, they should be entered in the interactive section of the program; otherwise, the program will calculate incorrectly.

Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|ErrorInterval|2000|Error retry interval (milliseconds)|
|InvestInternal|15|Investment interval (in minutes)|
|MoneyEveryMonth|5000|Monthly investment amount|
|SlidePrice|0.05|Purchase slippage|

|Button|Default|Description|
|---|---|---|
|Pause|__button__|Pause trading|
|Continue|__button__|Resume trading|
|MoneyChange|false|Record fund deposits or withdrawals|
|StockChange|false|Record digital currency deposits or withdrawals|

Source (JavaScript)

``` javascript
var initAccount;
var startTime; // unix timestamp
var pause = false; // pause execution of strategy or continue
var moneyDeposit = 0; // positive means deposit, negative means withdraw
var stockDeposit = 0; // positive means deposit, negative means withdraw

function AdjustFloat(v) {
    return Math.floor(v * 1000)/1000;
}

function GetAccount() {
    var account = null;
    while (!(account = exchange.GetAccount())) {
        Log('Get Account Error');
        Sleep(ErrorInterval);
    }
    return account;
}

function GetCurrentPrice() {
    var ticker = null;
    while (!(ticker = exchange.GetTicker())) {
        Log('Get Ticker Error');
        Sleep(ErrorInterval);
    }
    return AdjustFloat(ticker.Last);
}

function GetOrders(){
    var orders = null;
    while (!(orders = exchange.GetOrders())) {
        Log('Get Orders Error');
        Sleep(ErrorInterval);
    }
    return orders;
}

function CancelPendingOrders() {
    while(true){
        var orders = GetOrders();
        if (orders.length === 0) {
            return;
        }

        for (var i = 0; i < orders.length; i++) {
            exchange.CancelOrder(orders[i].Id);
            if (i < (orders.length-1)) {
                Sleep(ErrorInterval);
            }
        }
    }
}

function ProcessCommand() {
    var command = GetCommand();

    if (command !== null) {
        Log('command:', command);
        if (command === 'pause') {
            pause = true;
        }
        if (command === 'Continue') {
            pause = false;
        }
        if(command.indexOf('MoneyChange:') === 0){
            moneyDeposit += parseFloat(command.replace("MoneyChange:", ""));
            Log('Deposit Money:', moneyDeposit);
        }
        if(command.indexOf('StockChange:') === 0){
            stockDeposit += parseFloat(command.replace("StockChange:", ""));
            Log('Deposit Stock:',stockDeposit);
        }
    }
}

function CaculateMoneyToInvest(currentPrice, investCount)
{
    var moneyEveryInvest = MoneyEveryMonth * InvestInternal / (30 * 24 * 60);
    var totalStockInvested = 0.0;
    var totalMoneyInvested = 0.0;
    var totalValueInvested = 0.0;
    var moneyToInvestThisTime = 0.0;

    CancelPendingOrders();
    var accountNow = GetAccount();
    totalMoneyInvested = initAccount.Balance + initAccount.FrozenBalance + moneyDeposit - accountNow.Balance - accountNow.FrozenBalance;
    totalStockInvested = accountNow.Stocks + accountNow.FrozenStocks - initAccount.Stocks - initAccount.FrozenStocks - stockDeposit;

    Log('Total Money Invested:',totalMoneyInvested);
    Log('Total Stock Invested:',totalStockInvested);

    totalValueInvested = AdjustFloat(totalStockInvested * currentPrice);
    Log('Total Value Invested:',totalValueInvested);

    var averagePrice = 0;
    if(totalStockInvested !== 0){
        averagePrice = AdjustFloat(totalMoneyInvested / totalStockInvested);
    }

    moneyToInvestThisTime = AdjustFloat(moneyEveryInvest * investCount - totalValueInvested);
    Log('Money to Invest This Time:', moneyToInvestThisTime);

    var profit = totalValueInvested - totalMoneyInvested;
    var totalValueNow = (accountNow.Stocks + accountNow.FrozenStocks) * currentPrice + accountNow.Balance + accountNow.FrozenBalance;
    LogStatus('Account Value Now:' + totalValueNow + '\n' + 'Count:',investCount,'  Money:', totalMoneyInvested, 'Stock:', totalStockInvested, 'Average:', averagePrice,'Profit:',profit);
    LogProfit(profit);

    return moneyToInvestThisTime;
}

function onTick(investCount) {
    var currentPrice = GetCurrentPrice();
    Log('Current Price', currentPrice);

    var moneyToInvestThisTime = CaculateMoneyToInvest(currentPrice,investCount);
    var stockToInvestThisTime = 0;
    if(moneyToInvestThisTime > 0){ //Buy
        stockToInvestThisTime = AdjustFloat(moneyToInvestThisTime / (currentPrice + SlidePrice));
    }else{ //Sell
        stockToInvestThisTime = AdjustFloat(moneyToInvestThisTime / (currentPrice - SlidePrice));
    }

    var minPrice = exchange.GetMinPrice();
    if(Math.abs(moneyToInvestThisTime) < minPrice){
        Log('Invest Less Than MinPrice:', minPrice);
        return;
    }

    var minStock = exchange.GetMinStock();
    if(Math.abs(stockToInvestThisTime) < minStock){
        Log('Invest Less Than MinStock:',minStock);
        return;
    }

    var account = GetAccount();
    if(stockToInvestThisTime > 0){ //Buy
        if(account.Balance < moneyToInvestThisTime){
            Log('Money not Enough.#ff0000@');
            return;
        }
    }else{ //Sell
        if(account.Stocks < Math.abs(stockToInvestThisTime)){
            Log('Insufficient Stocks to Sell.#ff0000@');
            return;
        }
    }

    var order = {
        type: (stockToInvestThisTime > 0) ? 'buy' : 'sell',
        price: currentPrice,
        amount: Math.abs(stockToInvestThisTime)
    };

    exchange.PlaceOrder(order);
}
```
```