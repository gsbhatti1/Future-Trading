> Name

TradingView Signal Execution Strategy with Built-in HTTP Service Version

> Author

Innovator Quant - Xiao Xiaomeng

> Strategy Description

Related Articles:

> https://www.fmz.com/digest-topic/10556

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|port|Port number used by the built-in HTTP service.|Port Number|
|ipWhiteList|IP address whitelist, leave blank to disable validation.|IP Address Whitelist|
|passPhrase|Leave blank to disable validation.|Authentication Phrase|
|serverIP|Server IP address.|Server IP|
|SleepInterval|Main loop polling interval.|Polling Interval|
|maxBuffSignalRowDisplay|Maximum number of signals displayed in the buffer.|Maximum Number of Signals Displayed|
|initCode|Initialization code to be executed, for example used to test simulation disk: `exchange.SetBase("https://testnet.binancefuture.com")`; switch OKX simulation disk: `exchange.IO("simulate", true)`|Initialization Code|
|isResetLog|Reset log|Reset Log|




|Button|Default|Description|
|----|----|----|
|TestSignal|Signal Test.|Signal Test|


> Source (javascript)

``` javascript
// Signal structure
var Template = {
    Flag: "45M103Buy",     // Identifier, can be arbitrarily specified
    Exchange: 1,           // Specify the exchange trading pair
    Currency: "BTC_USDT",  // Trading pair
    ContractType: "spot",  // Contract type, `swap`, `quarter`, `next_quarter`, fill `spot` for spot market
    Price: "{{close}}",    // Opening or closing price, -1 for market price
    Action: "buy",         // Trade type [ buy: Spot Buy , sell: Spot Sell , long: Futures Long , short: Futures Short , closesell: Futures Buy to Close Short , closebuy: Futures Sell to Close Long ]
    Amount: "1",           // Trading volume
}

var Success = "#5cb85c"    // Successful color
var Danger = "#ff0000"     // Error color
var Warning = "#f0ad4e"    // Warning color
var buffSignal = []

// HTTP service
function serverFunc(ctx, ipWhiteList, passPhrase) {
    var path = ctx.path()
    if (path == "/CommandRobot") {
        // Validate IP address
        var fromIP = ctx.remoteAddr().split(":")[0]        
        if (ipWhiteList && ipWhiteList.length > 0) {
            var ipList = ipWhiteList.split(",")
            if (!ipList.includes(fromIP)) {
                ctx.setStatus(500)
                ctx.write("IP address not in white list")
                Log("500 Error: IP address not in white list", "#FF0000")
                return 
            }
        }

        // Validate authentication phrase
        var pass = ctx.rawQuery().length > 0 ? ctx.query("passPhrase") : ""
        if (passPhrase && passPhrase.length > 0) {
            if (pass != passPhrase) {
                ctx.setStatus(500)
                ctx.write("Authentication failed")
                Log("500 Error: Authentication failed", "#FF0000")
                return 
            }
        }

        var body = JSON.parse(ctx.body())
        threading.mainThread().postMessage(JSON.stringify(body))
        ctx.write("OK")
        // 200
    } else {
        ctx.setStatus(404)
    }
}

// Validate signal message format
function DiffObject(object1, object2) {
    const keys1 = Object.keys(object1)
    const keys2 = Object.keys(object2)
    if (keys1.length !== keys2.length) {
        return false
    }
    for (let i = 0; i < keys1.length; i++) {
        if (keys1[i] !== keys2[i]) {
            return false
        }
    }
    return true
}

function CheckSignal(Signal) {
    Signal.Price = parseFloat(Signal.Price)
    Signal.Amount = parseFloat(Signal.Amount)
    if (Signal.Exchange <= 0 || !Number.isInteger(Signal.Exchange)) {
        Log("Exchange minimum number is 1 and must be an integer", Danger)
        return
    }
    if (Signal.Amount <= 0 || typeof(Signal.Amount) != "number") {
        Log("Trade volume cannot be less than 0 and must be a numerical type", typeof(Signal.Amount), Danger)
        return
    }
    if (typeof(Signal.Price) != "number") {
        Log("Price must be a number", Danger)
        return
    }
    if (Signal.ContractType == "spot" && Signal.Action != "buy" && Signal.Action != "sell") {
        Log("Command for spot operation, Action error, Action:", Signal.Action, Danger)
        return 
    }
    if (Signal.ContractType != "spot" && Signal.Action != "long" && Signal.Action != "short" && Signal.Action != "closesell" && Signal.Action != "closebuy") {
        Log("Command for futures operation, Action error, Action:", Signal.Action, Danger)
        return 
    }
    return true
}

// Signal processing object
function createManager() {
    var self = {}
    self.tasks = []
    
    self.process = function() {
        var processed = 0
        if (self.tasks.length > 0) {
            _.each(self.tasks, function(task) {
                if (!task.finished) {
                    processed++
                    self.pollTask(task)
                }
            })
            if (processed == 0) {
                self.tasks = []
            }
        }
    }
    
    self.newTask = function(signal) {
        // {"Flag":"45M103Buy","Exchange":1,"Currency":"BTC_USDT","ContractType":"swap","Price":"10000","Action":"buy","Amount":"0"}
        var task = {}
        task.Flag = signal["Flag"]
        task.Exchange = signal["Exchange"]
        task.Currency = signal["Currency"]
        task.ContractType = signal["ContractType"]
        task.Price = signal["Price"]
        task.Action = signal["Action"]
        task.Amount = signal["Amount"]
        task.exchangeIdx = signal["Exchange"] - 1
        task.pricePrecision = null 
        task.amountPrecision = null 
        task.error = null 
        task.exchangeLabel = exchanges[task.exchangeIdx].GetLabel()
        task.finished = false 
        
        Log("Create task:", task)
        self.tasks.push(task)
    }
    
    self.getPrecision = function(n) {
        var precision = null 
        var arr = n.toString().split(".")
        if (arr.length == 1) {
            precision = 0
        } else if (arr.length == 2) {
            precision = arr[1].length
        } 
        return precision
    }
    
    self.pollTask = function(task) {
        var e = exchanges[task.exchangeIdx]
        var name = e.GetName()
        var isFutures = true
        e.SetCurrency(task.Currency)
        if (task.ContractType != "spot" && name.indexOf("Futures_") != -1) {
            // Non-spot, set contract type
            e.SetContractType(task.ContractType)
        } else if (task.ContractType == "spot" && name.indexOf("Futures_") == -1) {
            isFutures = false 
        } else {
            task.error = "The ContractType in the command does not match the configured exchange object type"
            return 
        }
        
        var depth = e.GetDepth()
        if (!depth || !depth.Bids || !depth.Asks) {
            task.error = "Order book data is abnormal"
            return 
        }
```