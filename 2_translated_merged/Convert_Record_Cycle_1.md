```markdown
---
Name

Convert_Record_Cycle

Author

jxc6698

Strategy Description

# Get candlestick data for a specified period

If there are any bugs or issues, please feel free to leave a comment.

Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|UI_NewCycleForMS|1000*60*60*2|Synthetic cycle in milliseconds|

Source (javascript)

``` javascript
/**
*   author: jcx
*   date:   3/10/2017
*/
/**
*   Modified from XiaoXiaoMeng's "Convert Any K-Line Cycle" template, supporting setting any period size and input ticker.
*   The time setting must be an integer multiple of the current provided records[] cycle (no check is performed in the program).
*
*   Considering that the last data returned by getrecords() may change:
*   1. A loop can be used from 0 to <length-1 in the main function.
*   2. Or, as the current method allows for updating of the value at the end of the period in AddKLine(), implying records should be added in chronological order.
*
*/

// K-line cycle synthesis - extended to synthesize based on base K-line cycles into any desired periods.

var cloneObj = function(obj) {                             // Deep copy object function
    var str, newobj = obj.constructor === Array ? [] : {};
    if (typeof obj !== 'object') {
        return;
    } else if (JSON) {
        str = JSON.stringify(obj);                         // Serialize the object
            newobj = JSON.parse(str);                      // Parse to create a copy
    } else {
        for (var i in obj) {
            newobj[i] = typeof obj[i] === 'object' ?
                cloneObj(obj[i]) : obj[i];
        }
    }
    return newobj;
};

/**
*   NeWCycleForMS: New cycle
*   n            : Number of candle records to be returned each time
*/
var DefaultN = 10
function AssembleRecords(NewCycleForMS, n) {
    var self = {}
    self.NewCycleForMS = NewCycleForMS;
    self.curBars = []       // Used to store the most recent n candle objects
    n = parseInt(n)         // Store the number of candles returned each time
    if (n*1 === n)
        self.n = n
    else
        self.n = DefaultN
    // Temporary variables
    self.tmp = {lasttime: 0}

    self.timeAf = function (time1, time2) {
        return time1 < time2
    }
    self.timeAfOrEq = function (time1, time2) {
        return time1 <= time2
    }
    self.inSameKLine = function (time1, time2) {
        if (parseInt(time1/self.NewCycleForMS) === 
            parseInt(time2/self.NewCycleForMS)) {
            return true
        }
        return false;
    }
    self.getKlineStartTime = function (time) {
        return time - time%self.NewCycleForMS
    }
    self.newBarObj = function (time, v) {
        var value = 0;
        value = v
        return {                         // Define a candlestick structure
            Time: time,
            Open: value,
            High: value,
            Low: value,
            Close: value,
            Volume: 0
        }
    }
    self.updateNewBar = function(time, defaultvalue) {
        var barobj;
        if (self.curBars.length == 0) {
            barobj = self.newBarObj(self.getKlineStartTime(time), 
                defaultvalue)
            self.curBars.push(barobj)
        } else if(!self.inSameKLine(self.curBars[self.curBars.length-1].Time,
            time) ) {
            barobj = self.newBarObj(self.getKlineStartTime(time),
                defaultvalue)
            self.curBars.push(barobj)
        }
            
        if (self.curBars.length > n+2) {
            self.curBars.shift()
        }
        return self.curBars[self.curBars.length-1];
    }
    self.AddTicker = function (ticker) {
        var barobj;
//      ticker should be passed in time order
        barobj = self.updateNewBar(ticker.Time, ticker.Last);

        if (!self.timeAfOrEq(self.barobj[self.barobj.length-1].Time, 
            ticker.Time)) {
            return;
        }        
        if (barobj.High < ticker.High)
            barobj.High = ticker.High
        if (barobj.Low > ticker.Low)
            barobj.Low = ticker.Low
        barobj.Close = ticker.Last
//        barobj.Volume += ticker.Volume
    }
    self.AddKLine = function (klinerecord) {
        var barobj;        

        // Must use <=, when stepping into new record, last record may change
        if (!self.timeAfOrEq(self.tmp.lasttime, 
            klinerecord.Time)) {
            return
        }
        barobj = self.updateNewBar(klinerecord.Time, klinerecord.Open)
        self.tmp.lasttime = klinerecord.Time

        if (barobj.High < klinerecord.High) {
            barobj.High = klinerecord.High
        }
        if (barobj.Low > klinerecord.Low)
            barobj.Low = klinerecord.Low
        barobj.Close = klinerecord.Close
        barobj.Volume += klinerecord.Volumn
    }
    self.GetKline = function () {
        var len = self.curBars.length;
        return self.curBars.slice(len-self.n);
    }

    return self;
}

//  Test code
function main() {
    var records = exchange.GetRecords();
    while (!records || records.length < 24) {
        records = exchange.GetRecords();
    }
    
    // Handle UI parameters, can be referenced if implemented in your own strategy
    
    var Num_UI_NewCycleForMS = 1;
    var arrayNum = UI_NewCycleForMS.split("*");
    for(var indexNum = 0 ; indexNum < arrayNum.length ; indexNum++){
        Num_UI_NewCycleForMS = Num_UI_NewCycleForMS * Number(arrayNum[indexNum]);
    }
    Log("Custom cycle in milliseconds: ", Num_UI_NewCycleForMS);
    
    // First parameter is the base K-line, second parameter is the millisecond value of the desired period, e.g., 1000 * 60 * 20 for 20 minutes
    obj = AssembleRecords(Num_UI_NewCycleForMS, 5);      



    while(true){
        records = _C(exchange.GetRecords);
        
        for (var i=0;i<records.length;i++) {
            obj.AddKLine(records[i])
        }

        newrecords = obj.GetKline()
        $.PlotRecords(newrecords, 'BTC');

        // throw "stop"; // test
        Sleep(1000);
    }
}
```

Detail

https://www.fmz.com/strategy/37678

Last Modified

2017-03-13 16:41:10
```