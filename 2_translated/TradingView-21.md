``` javascript
// Signal structure
var Template = {
    Flag: "45M103Buy",     // Identifier, can be arbitrarily specified
    Exchange: 1,           // Specify the trading pair on the exchange
    Currency: "BTC_USDT",  // Trading pair
    ContractType: "swap",  // Contract type [swap, quarter, next_quarter, spot for spot market]
    Price: "{{close}}",    // Opening or closing price, -1 indicates market price
    Action: "buy",         // Trading action [ buy: Spot Buy , sell: Spot Sell , long: Futures Long , short: Futures Short , closesell: Futures Close Short , closebuy: Futures Close Long, bpk: Buy to Cover then Open Long , spk: Sell to Cover then Open Short ]
    Amount: "0",           // Trading volume
}

var BaseUrl = "https://www.fmz.com/api/v1"   // FMZ extension API interface address 
var RobotId = _G()                           // Current live trading ID
var Success = "#5cb85c"    // Success color
var Danger = "#ff0000"     // Danger color
var Warning = "#f0ad4e"    // Warning color
var buffSignal = []

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
        Log("The minimum exchange number is 1 and must be an integer", Danger)
        return
    }
    if (Signal.Amount <= 0 || typeof(Signal.Amount) != "number") {
        Log("Trading volume cannot be less than 0 and must be a numerical type", typeof(Signal.Amount), Danger)
        return
    }
    if (typeof(Signal.Price) != "number") {
        Log("Price must be a number", Danger)
        return
    }
    if (Signal.ContractType == "spot" && Signal.Action != "buy" && Signal.Action != "sell") {
        Log("Command for spot trading, Action error, Action:", Signal.Action, Danger)
        return 
    }
    if (Signal.ContractType != "spot" && Signal.Action != "long" && Signal.Action != "short" && Signal.Action != "closesell" && Signal.Action != "closebuy" &&
        Signal.Action != "bpk" && Signal.Action != "spk") {
        Log("Command for futures trading, Action error, Action:", Signal.Action, Danger)
        return 
    }
    return true
}

function commandRobot(url, accessKey, secretKey, robotId, cmd) {
    // https://www.fmz.com/api/v1?access_key=xxx&secret_key=xxx&method=CommandRobot&args=[xxx,+""]
    url = url + '?access_key=' + accessKey + '&secret_key=' + secretKey + '&method=CommandRobot&args=[' + robotId + ',+""]'
    var postData = {
        method:'POST', 
        data:cmd
    }
    var headers = "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36\nContent-Type: application/json"
    var ret = HttpQuery(url, postData, "", headers)
    Log("Simulating TradingView webhook request, sending a test POST request:", url, "body:", cmd, "response:", ret)
}

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
        
        Log("Creating task:", task)
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
    
    self.cover = function(task) {
        var e = exchanges[task.exchangeIdx]
        var action = task.Action
        var pos = e.GetPosition()
        if (pos === null) {
            task.error = "Position data abnormal"
            return false
        }
        
        _.each(pos, function(p) {  
            if (action == "bpk" && p.Type == PD_SHORT) {
                e.SetDirection("closesell")
                e.Buy(-1, p.Amount)
            } else if (action == "spk" && p.Type == PD_LONG) {
                e.SetDirection("closebuy")
                e.Sell(-1, p.Amount)
            }
        })

        return true 
    }

    self.pollTask = function(task) {
        var e = exchanges[task.exchangeIdx]
        var name = e.GetName()
        var isFutures = true
        e.SetCurrency(task.Currency)
        if (task.ContractType != "spot" && name.indexOf("Futures_") != -1) {
            // Non-spot, set the contract type
            e.SetContractType(task.ContractType)
        } else if (task.ContractType == "spot" && name.indexOf("Future") == -1) {
            isFutures = false
        }
        
        task.pricePrecision = self.getPrecision(task.Price)
        task.amountPrecision = self.getPrecision(task.Amount)
    }
}
```