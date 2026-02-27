> Name

TradingView Strategy Signal Trading Robot - OKEx Version

> Author

High-Frequency Quantitative Analysis



> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|IsMarketOrder|false|Whether to use a market order|
|QuotePrecision|3|Price precision for orders|
|BasePrecision|3|Quantity precision for orders|
|Ct||Futures contract code|



|Button|Default|Description|
|----|----|----|
|buy|0.01|Test buy|
|sell|0.01|Test sell|
|long|0.01|Test long position|
|short|0.01|Test short position|
|cover_long|0.01|Test close long position|
|cover_short|0.01|Test close short position|


> Source (javascript)

``` javascript
/*
- Command string format for interaction:
  action:amount
  action: buy , sell , long , short , cover_long , cover_short, spk , bpk
- Exchange type
  eType variable value: 0 spot , 1 futures

- TradingView documentation link:
  https://www.tradingview.com/pine-script-docs/en/v4/Quickstart_guide.html
  https://cn.tradingview.com/chart/8xfTuX7F/

- TV webhook request sending:
  https://www.fmz.com/api/v1?access_key=xxx&secret_key=yyyy&method=CommandRobot&args=[186515,"action:amount"]

- Library references
  Reference digital currency trading library.
*/

// Parameters
// var IsMarketOrder = true 
var QuotePrecision = 3
var BasePrecision = 3

// Futures parameters
var Ct = "swap"
//exchange.SetContractType("swap")        // Set to perpetual contract
//exchange.SetCurrency("BTC_USDT")

// Global variables
var BUY = "buy"
var SELL = "sell"
var LONG = "long"
var SHORT = "short"
var COVER_LONG = "cover_long"
var COVER_SHORT = "cover_short"
var SPK = "spk"
var BPK = "bpk"


//------------------- Added
const accountInformation = { //Account information
    type: 'table',
    title: 'Account Information',
    cols: ['Initial Balance', 'Wallet Balance ', 'Margin Balance', 'Available Margin', 'Used Margin', 'Total Revenue', 'Yield'], // Column headers
    rows: null // Data array   
};

const binanceFundingRate = { //Position table
    type: 'table',
    title: 'OKEx UStablecoin Position Table',
    cols: ['Trading Pair', 'Trade Direction ', 'Opening Volume', 'Opening Price', 'Holding Value', 'Leverage', 'Used Margin', 'Profit'], // Column headers
    rows: null // Data array
};

initialPrincipalUsdt = null // Initial principal in USDT
revenueUsdt = 0 // Revenue


//--------------------------------------
// Account Information
//--------------------------------------
function accountInformationFunction() {
    exchange.SetContractType("swap"); // Set to perpetual contract swap / quarter/
    var Currency = exchange.GetCurrency()
    exchange.SetCurrency(Currency) // Switch product to access the UStablecoin account information
    var account = _C(exchange.GetAccount)

    _CDelay(2000 * 60)
    if (!account) {
        Log("Failed to retrieve assets")
        return
    }
    
    if (initialPrincipalUsdt == null ) {
        initialPrincipalUsdt = account.Info.data[0].totalEq // Get the initial balance when loading
        _G("initialPrincipalUsdt", initialPrincipalUsdt) // Retrieve and save data
        if (initialPrincipalUsdt == 0) {
            Log("No assets in USDT futures")
            return
        }
    }

    InitialBalance = Number(initialPrincipalUsdt)
    WalletBalance = account.Info.data[0].totalEq
    marginBalance = account.Info.data[0].isoEq
    FreeMargin = account.Info.data[0].isoEq
    UsedMargin = account.Info.data[0].isoEq
   
    TotalRevenue = Number(WalletBalance) - Number(InitialBalance)
    Yield1 = TotalRevenue / InitialBalance
    yield1 = Number(Yield1)
    Yield = (yield1 * 100).toFixed(2) + "%"
    
    // Wrap in an array
    revenueUsdt = Number(TotalRevenue)

    accountInformation.rows = [] // Clear the array
                                 //'Initial Balance', 'Wallet Balance ', 'Margin Balance', 'Free Margin', 'Used Margin', 'Total Revenue', 'Yield'
    accountInformation.rows[0] = [InitialBalance, WalletBalance, marginBalance, FreeMargin, UsedMargin, TotalRevenue, Yield]

}

//--------------------------------------
// Position Table
//--------------------------------------
function binanceFundingRateFunction() { // Position table
    binanceFundingRate.rows = []
    exchange.SetContractType("swap"); // Set to perpetual contract, note that both UStablecoin and native positions exist with perpetual contracts
    var y = 0 // To determine if the product has not been modified

    for (var i = 0; i < exchanges.length; i++) {
        exchange.SetCurrency(exchanges[i].GetCurrency()) // Switch product
        //-------------------------------------------------------
        var position = _C(exchange.GetPosition) // Get account position status
       // Log("position", position)
        _CDelay(1000 * 2 * 60)
        // Separate cross-period contracts for native positions. Perpetuals are different.
        if (position) {
            for (var iii = 0; iii < position.length; iii++) {
                if (exchange.GetContractType() == position[iii].ContractType) { // Why is the check needed? Because all cross-period positions are placed together
                    // ['Trading Pair', 'Trade Direction ', 'Opening Volume', 'Opening Price', 'Holding Value', 'Leverage', 'Used Margin', 'Profit'], // Column headers
                    binanceFundingRate.rows[y] = [position[iii].Info.instId, position[iii].Type == 0 ? "BUY" : "SELL", position[iii].Amount,
                                                  position[iii].Price, position[iii].Amount * position[iii].Price,
                                                  position[iii].MarginLevel, position[iii].Margin, position[iii].Profit
                                                  ]
                    y++
                }
            }
        }

    }

}


//--------------------------------------
// Main function
//--------------------------------------

function main() {
    // Clear logs, if not needed, delete it.
    // LogReset(1)

    // Set precision
    exchange.SetPrecision(QuotePrecision, BasePrecision)

    // Identify futures or spot trading
    var eType = 0
    var eName = exchange.GetName() // Name of the exchange, e.g.: Futures_Binance
    var patt = /Futures_/
    if (patt.test(eName)) { // Check if it contains Futures_
        Log("The added exchange is a futures exchange:", eName, "#FF0000")
        eType = 1
        if (Ct == "") {
            throw "Ct contract set to empty"
        } else {
            Log(exchange.SetContractType(Ct), "Set contract type: ", Ct, "#FF0000")
        }
    } else {
        Log("The added exchange is a spot exchange:", eName, "#32CD32")
    }

    // Test position function
    var position = exchange.GetPosition()
    if (position.length == 0) {
        Log("Robot first startup, performing comprehensive checks on the exchange", "#33CD33")
        Log(exchange.GetLabel(), "Account information initialization completed: No positions in the account, all is well", "#0000FF")
        Log("Machine"
```