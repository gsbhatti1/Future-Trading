<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Convert_Record_Cycle

> Author

jxc6698

> Strategy Description

# Obtain candlestick line data of specified cycle

If there are BUGs or issues, feel free to leave a comment

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|UI_NewCycleForMS|1000*60*60*2|Synthesized cycle milliseconds|


> Source (javascript)

``` javascript
/**
*   author: jcx
*   date:   3/10/2017
*/
/**
*   Modified from Xiaoxiaomeng's template "Convert any K-line period", supports setting arbitrary period sizes, supports input ticker
*   Time settings must be an integer multiple of the current provided records[] period to make sense (not checked in the program)
*   
*
* Considering that the last data returned by getrecords() may change.
*   1. You can loop in the main function from 0 to < length-1  
*   2. Or using the current processing method, in the AddKLine method, use timeAfOrEq(), allowing the value of the last time period to be updated
*       (implicitly requires adding kline records in chronological order)
*
*/



// K-line period synthesis extended to synthesize from basic K-lines to arbitrary periods.
var cloneObj = function(obj) {                             // Deep copy object function
    var str, newobj = obj.constructor === Array ? [] : {};
    if (typeof obj !== 'object') {
        return;
    } else if (JSON) {
        str = JSON.stringify(obj);                         // Serialize object
            newobj = JSON.parse(str);                      // Restore
    } else {
        for (var i in obj) {
            newobj[i] = typeof obj[i] === 'object' ?
                cloneObj(obj[i]) : obj[i];
        }
    }
    return newobj;
};

/**
*   NeWCycleForMS: New period
*   n            : Size of candle records array returned each time
*/
var DefaultN = 10
function AssembleRecords(NewCycleForMS, n) {
    var self = {}
    self.NewCycleForMS = NewCycleForMS;
    self.curBars = []       // Used to store recent n candle objects
    n = parseInt(n)         // Store number of candles returned each time
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
        return {                         // Define a K-line bar structure
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
//      ticker should passed as time order
        barobj = self.updateNewBar(ticker.Time, ticker.Last);

        if (!self.timeAfOrEq(self.barobj[self.barobj.length-1].Time, 
            cker.Time)) {
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

        // must use <=, when stepping into new record, last record may change
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
    
    // Process interface parameters, you can refer to this when writing your own strategy
    
    var Num_UI_NewCycleForMS = 1;
    var arrayNum = UI_NewCycleForMS.split("*");
    for(var indexNum = 0 ; indexNum < arrayNum.length ; indexNum++){
        Num_UI_NewCycleForMS = Num_UI_NewCycleForMS * Number(arrayNum[indexNum]);
    }
    Log("Custom period millisecond time is:", Num_UI_NewCycleForMS);
    
    // The first parameter is the base K-line, the second parameter is the millisecond number of the period to be converted, 1000 * 60 * 20 is to convert to 20 minutes
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

> Detail

https://www.fmz.com/strategy/37678

> Last Modified

2017-03-13 16:41:10