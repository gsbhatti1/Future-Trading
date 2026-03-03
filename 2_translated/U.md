> Name

U-based grid amplitude filtering

> Author

ChaoZhang

> Strategy Description

Find the currency with the largest average amplitude for grid trading

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|Day|30|Number of days to consider for calculating the average amplitude|


> Source (javascript)

``` javascript
/* jshint esversion: 6 */
// var Day = 30; // Counting days
var Quote = "USDT"; // Quotation currency, BUSD or USDT
function GetAmplitude(klineList) {
    let ret = {
        ampl: 0,
        change: 0,
        maxAmpl: 0,
        maxAmplTime: 0,
        minAmpl: 100,
        minAmplTime: 0,
        maxChange: 0,
        minChange: 0,
        avgAmpl: 0,
        avgChange: 0,
        day: 0,
    };
    for (let i = 0; i < klineList.length; i++) {
        const item = klineList[i];
        amp = (parseFloat(item.High - item.Low) / parseFloat(item.Open)) * 100.0; // Amplitude
        change = (parseFloat(item.Close - item.Open) / parseFloat(item.Open)) * 100.0; // Increase
        if (amp > ret.maxAmpl) {
            ret.maxAmpl = amp;
            ret.maxAmplTime = item.Time;
        }
        if (amp < ret.minAmpl) {
            ret.minAmpl = amp;
            ret.minAmplTime = item.Time;
        }
        if (change > ret.maxChange) {
            ret.maxChange = change;
        }
        if (change < ret.minChange) {
            ret.minChange = change;
        }
        ret.ampl += amp;
        ret.change += change;
        ret.day = i + 1;
    }
    ret.avgAmpl = ret.ampl / klineList.length;
    ret.avgChange = ret.change / klineList.length;
    return ret;
}

function main() {
    exchange.SetContractType("swap");
    exchange.SetMaxBarLen(1000);
    let table = {
        type: "table",
        title: "Amplitude Information",
        cols: ["currency", "number of days", "average amplitude %", "maximum amplitude %", "maximum amplitude time", "minimum amplitude", "minimum amplitude time", "total amplitude %", "average increase or decrease %", "maximum increase %", "maximum decrease %", "increase or decrease %"],
        rows: [],
    };
    let info = exchange.IO("api", "GET", "/fapi/v1/exchangeInfo");
    for (let i = 0; i < info.symbols.length; i++) {
        const ele = info.symbols[i];
        if (ele.contractType == "PERPETUAL" && ele.status == "TRADING" && ele.quoteAsset == Quote) {
            let symbol = ele.baseAsset + "_" + Quote;
            exchange.SetCurrency(symbol);
            let records = exchange.GetRecords(PERIOD_D1);
            if (records.length < Day) {
                Log(ele.baseAsset + Quote+".P", records.length);
                continue; // Only count currencies with enough days
            }
            let ampls = GetAmplitude(records.splice(-1 * (Day + 1), Day));
            //
            table.rows.push([
                ele.baseAsset + Quote+".P", // Currency
                ampls.day, // Number of days
                _N(ampls.avgAmpl, 2), // Average amplitude
                _N(ampls.maxAmpl, 2), // Maximum amplitude
                _D(ampls.maxAmplTime), // Maximum amplitude time
                _N(ampls.minAmpl, 2), // Minimum amplitude
                _D(ampls.minAmplTime), // Minimum amplitude time
                _N(ampls.ampl, 2), // Total amplitude
                _N(ampls.avgChange, 2), // Average increase or decrease
                _N(ampls.maxChange, 2), // Maximum increase
                _N(ampls.minChange, 2), // Minimum increase
                _N(ampls.change, 2), // Total increase
            ]);
        }
    }
    LogStatus("`" + JSON.stringify(table) + "`\n");
}
```

> Detail

https://www.fmz.com/strategy/364968

> Last Modified

2024-03-10 18:23:10