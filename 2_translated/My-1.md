> Name

My-1-Averaging Value Investment Strategy

> Author

Lizza

> Strategy Description

Live Trading: https://www.fmz.com/m/robot/26018
This strategy is suitable for Bitcoin enthusiasts who are long-term bullish. It uses an averaging value investment approach to regularly invest, effectively mitigating market fluctuations (more about averaging value investment on Baidu).

The basic idea is to first decide how much money you want to invest every month (strategy variable: MoneyEveryMonth), then determine the interval between transactions, with a minimum trading interval not recommended less than 5 minutes (strategy parameter: InvestInternal).

Below is an example illustrating the strategy and buying/selling timing:
Assume you want to buy Bitcoin worth 72000 RMB each month for calculation purposes, trade once per hour, meaning planning 24 * 30 = 720 transactions monthly. Each planned investment amount would be 72000 / 720 = 100 RMB (Variable A).

Hour B, Current Price C, Invested Funds D, Number of Coins Purchased E, Value of Holding F, Amount to Invest G, Number of Coins Purchased This Time H
1      400     0            0           C*E=0         A*B-F=100         G/C=0.25                   
2      200     100          0.25        200 * 0.25 = 50   100*2-50 = 150      0.75
3     1000     250          1           1000          100*3-1000=-700    -0.7
4     500      -550         0.3         150           100*4-150=250       0.5

The final result is an investment of 300 RMB, purchasing 0.8 Bitcoin (worth 400 RMB), with an average price of 375 RMB.

Note: The program will check the difference between account funds and coins at startup to calculate the number of purchases needed each time. Therefore, do not use a shared account with other robots or manually perform buying/selling operations. If there are deposits/withdrawals on the exchange, enter them in the interactive part of the program; otherwise, the calculation will be incorrect.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|ErrorInterval|2000|Error retry interval (milliseconds)|
|InvestInternal|15|Trading interval (in minutes)|
|MoneyEveryMonth|5000|Monthly investment amount|
|SlidePrice|0.05|Slippage at the time of purchase|



|Button|Default|Description|
|----|----|----|
|Pause|__button__|Pause trading|
|Continue|__button__|Resume trading|
|MoneyChange|false|Record fund deposits/withdrawals|
|StockChange|false|Record cryptocurrency deposits/withdrawals|


> Source (javascript)

``` javascript
var initAccount;
var startTime; //unix timestamp
var pause = false; //pause execution of strategy or continue
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

function CaculateMoneyToInvest(currentPrice,investCount)
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
            Log('Stock not Enough.#ff0000@');
            return;
        }
    }

    var order = {
        'type': stockToInvestThisTime > 0 ? 'buy' : 'sell',
        'price': currentPrice,
        'amount': Math.abs(stockToInvestThisTime)
    };

    exchange.PlaceOrder(order);
}
```