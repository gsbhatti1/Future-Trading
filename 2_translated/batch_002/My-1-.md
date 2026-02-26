``` markdown
---
Name

My-1-Value-Averaging-Diet-Strategy

Author

Lizza

Strategy Description

Live Trading: https://www.fmz.com/m/robot/26018
This strategy is suitable for die-hard Bitcoin fans who are bullish on the long term. It uses a value averaging strategy to invest regularly, effectively mitigating market volatility. (For more details about Value Averaging, search online.)

The basic idea is to first decide how much money you want to invest each month (Strategy Variable: MoneyEveryMonth), and then determine how often to trade; it’s not recommended to have an interval shorter than 5 minutes (Strategy Parameter: InvestInternal).

Here's an example to illustrate the strategy logic and trading opportunities:
Assume you want to buy Bitcoin worth RMB 72,000 each month (for ease of calculation), trading once per hour, which means planning for 720 trades over a month. The planned investment amount per trade would be RMB 100 (Variable A).

| Hour | Price(C) | Invested Funds(D) | Bought BTC(E) | Current Value of BTC(F) | Money to Invest This Time(G) | Amount of BTC to Buy This Time(H) |
|---|---|---|---|---|---|---|
| 1 | 400 | 0 | 0 | C*E=0 | A*B-F=100 | G/C=0.25 |
| 2 | 200 | 100 | 0.25 | 200 * 0.25 = 50 | 100 * 2 - 50 = 150 | 0.75 |
| 3 | 1000 | 250 | 1 | 1000 | 100 * 3 - 1000 = -700 | -0.7 |
| 4 | 500 | -550 | 0.3 | 150 | 100 * 4 - 150 = 250 | 0.5 |

The final result is an investment of RMB 300, buying 0.8 BTC (worth 400 RMB), with an average price of 375 RMB per BTC.

Explanation: The program will check the difference in funds and Bitcoin between the account at startup and now to calculate the quantity that needs to be purchased each time; therefore, do not use a common account with other robots or manually perform buy/sell operations. If there are deposits or withdrawals on the exchange, fill them in the interaction section of the program, otherwise, the program's calculation will be incorrect.

Strategy Arguments

| Argument | Default | Description |
|---|---|---|
| ErrorInterval | 2000 | Retry interval for errors (milliseconds) |
| InvestInternal | 15 | Investment interval (in minutes) |
| MoneyEveryMonth | 5000 | Monthly investment amount |
| SlidePrice | 0.05 | Slippage at the time of purchase |

| Button | Default | Description |
|---|---|---|
| Pause | __button__ | Pause trading |
| Continue | __button__ | Resume trading |
| MoneyChange | false | Record fund deposits or withdrawals |
| StockChange | false | Record cryptocurrency deposits or withdrawals |

Source (javascript)

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
        Sleep/ErrorInterval;
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
        if(account.Stocks < Math.abs(stockToInvestThi
```

Note: The document translation is cut off at the end. The full code block should be completed with proper logic as per the original.