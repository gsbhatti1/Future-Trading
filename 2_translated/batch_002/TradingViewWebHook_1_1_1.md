```javascript
/*
- Interactive command string format
  action:amount
  action: buy , sell , long , short , cover_long , cover_short, spk , bpk
- Exchange type
  eType variable values: 0 spot , 1 futures

- TV documentation link
  https://www.tradingview.com/pine-script-docs/en/v4/Quickstart_guide.html
  https://cn.tradingview.com/chart/8xfTuX7F/

- TV webhook sending request
  https://www.fmz.com/api/v1?access_key=xxx&secret_key=yyyy&method=CommandRobot&args=[186515,"action:amount"]

- Reference library
  Reference digital currency trading library
*/

// Parameters
// var IsMarketOrder = false 
// var QuotePrecision = 2
// var BasePrecision = 2

// Futures parameters
// var Ct = ""


// Global variables
var BUY = "buy"
var SELL = "sell"
var LONG = "long"
var SHORT = "short"
var COVER_LONG = "cover_long"
var COVER_SHORT = "cover_short"
var SPK = "spk"
var BPK = "bpk"


function main() {
    // Clear logs, if not needed, can be deleted
    LogReset(1)

	// Set precision
    exchange.SetPrecision(QuotePrecision, BasePrecision)

    // Identify futures or spot
    var eType = 0
    var eName = exchange.GetName()
    var patt = /Futures_/
    if (patt.test(eName)) {
        Log("Added exchange is a futures exchange：", eName, "#FF0000")
        eType = 1
        if (Ct == "") {
            throw "Ct contract setting is empty"
        } else {
        	Log(exchange.SetContractType(Ct), "Set contract：", Ct, "#FF0000")
        }
    } else {
    	Log("Added exchange is a spot exchange：", eName, "#32CD32")
    }
    
    var lastMsg = ""
    var acc = _C(exchange.GetAccount)
    while(true) {
        var cmd = GetCommand()
        if (cmd) {
            // Detect interactive commands
            lastMsg = "Command:" + cmd + "Time:" + _D()
            var arr = cmd.split(":")
            if (arr.length != 2) {
                Log("cmd information is incorrect：", cmd, "#FF0000")
                continue
            }

            var action = arr[0]
            var amount = parseFloat(arr[1])

            if (eType == 0) {
                if (action == BUY) {               
                    var buyInfo = IsMarketOrder ? exchange.Buy(-1, amount) : $.Buy(amount)
                    Log("buyInfo:", buyInfo)
                } else if (action == SELL) {        
                    var sellInfo = IsMarketOrder ? exchange.Sell(-1, amount) : $.Sell(amount)
                    Log("sellInfo:", sellInfo)
                } else {
                	Log("Spot exchange not supported!", "#FF0000")
                }
            } else if (eType == 1) {
            	var tradeInfo = null
            	var ticker = _C(exchange.GetTicker)
                if (action == LONG) {
                	exchange.SetDirection("buy")
                    tradeInfo = IsMarketOrder ? exchange.Buy(-1, amount) : exchange.Buy(ticker.Sell, amount)
                } else if (action == SHORT) {        
                    exchange.SetDirection("sell")
                    tradeInfo = IsMarketOrder ? exchange.Sell(-1, amount) : exchange.Sell(ticker.Buy, amount)
                } else if (action == COVER_LONG) {        
                    exchange.SetDirection("closebuy")
                    tradeInfo = IsMarketOrder ? exchange.Sell(-1, amount) : exchange.Sell(ticker.Buy, amount)
                } else if (action == COVER_SHORT) {        
                	exchange.SetDirection("closesell")
                	tradeInfo = IsMarketOrder ? exchange.Buy(-1, amount) : exchange.Buy(ticker.Sell, amount)
                } else if (action == SPK) {   // Sell to close long position, sell to open short position
                    exchange.SetDirection("closebuy")
                    var tradeInfo1 = IsMarketOrder ? exchange.Sell(-1, amount) : exchange.Sell(ticker.Buy, amount)
                    exchange.SetDirection("sell")
                    var tradeInfo2 = IsMarketOrder ? exchange.Sell(-1, amount) : exchange.Sell(ticker.Buy, amount)
                    tradeInfo = [tradeInfo1, tradeInfo2]
                } else if (action == BPK) {   // Buy to close short position, buy to open long position
                    exchange.SetDirection("closesell")
                    var tradeInfo1 = IsMarketOrder ? exchange.Buy(-1, amount) : exchange.Buy(ticker.Sell, amount)
                    exchange.SetDirection("buy")
                    var tradeInfo2 = IsMarketOrder ? exchange.Buy(-1, amount) : exchange.Buy(ticker.Sell, amount)
                    tradeInfo = [tradeInfo1, tradeInfo2]
                } else {
                	Log("Futures exchange not supported!", "#FF0000")
                }
                if (tradeInfo) {
                    Log("tradeInfo:", tradeInfo)
                }
            } else {
            	throw "eType error, eType:" + eType
            }
            acc = _C(exchange.GetAccount)
        }
        var tbl = {
        	type : "table", 
        	title : "Status Information", 
        	cols : ["Data"], 
        	rows : []
        }
        tbl.rows.push([JSON.stringify(acc)])
        LogStatus(_D(), eName, "Last received command：", lastMsg, "\n", "`" + JSON.stringify(tbl) + "`")
    	Sleep(1000)
    }
}

```