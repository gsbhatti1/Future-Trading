```text
Name

MACD Drawing Example

Author

Inventor Quantification-Little Dream


Source (javascript)

```
``` javascript
/*backtest
start: 2019-05-13 00:00:00
end: 2019-06-12 00:00:00
Period: 1d
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD"}]
*/

var preTime = 0;
var ChartObj = null;
function main(){
LogReset(1);
ChartObj = Chart(null);
ChartObj.reset();
var records = null;
var MACD = null;
exchange.SetContractType("quarter");
// Log(exchange.GetUSDCNY());
// exchange.SetRate(exchange.GetUSDCNY());
exchange.SetRate(1);
ChartObj = $.GetCfg();

// Process indicator axis------------------------
ChartObj.yAxis = [{
    title: {text: 'K line'},//title
    style: {color: '#4572A7'},//Style
    opposite: false //Generate the right Y axis
},
{
    title:{text: "Indicator Axis"},
    opposite: true, //Generate the right Y axis ceshi
}
];
//Initialize indicator line
while(!records || records.length < 30){
    records = _C(exchange.GetRecords);
    LogStatus("records.length:", records.length);
    Sleep(1000);
}

$.PlotRecords(records, 'OK Futures');
$.PlotLine('dif', 0, records[records.length - 1].Time);
$.PlotLine('dea', 0, records[records.length - 1].Time);
var chart = $.PlotLine('macd', 0, records[records.length - 1].Time);
//Modify indicator line coordinate axis Y axis
for(var key in ChartObj.series){
    if(ChartObj.series[key].name == 'dif' || ChartObj.series[key].name == 'dea' || ChartObj.series[key].name == 'macd'){
        ChartObj.series[key].yAxis = 1;
    }
}
chart.update(ChartObj);
chart.reset();

while(true){
    records = _C(exchange.GetRecords);
    if(records.length > 50){
        $.PlotRecords(records, 'OK Futures');
        MACD = TA.MACD(records);
        var dif = MACD[0];
        var dea = MACD[1];
        var macd = MACD[2];
        if(preTime !== records[records.length - 1].Time){
            $.PlotLine('dif', dif[dif.length - 2], records[records.length - 2].Time);
            $.PlotLine('dea', dea[dea.length - 2], records[records.length - 2].Time);
            $.PlotLine('macd', macd[macd.length - 2], records[records.length - 2].Time);

            $.PlotLine('dif', dif[dif.length - 1], records[records.length - 1].Time);
            $.PlotLine('dea', dea[dea.length - 1], records[records.length - 1].Time);
            $.PlotLine('macd', macd[macd.length - 1], records[records.length - 1].Time);

            preTime = records[records.length - 1].Time;
        }else{
            $.PlotLine('dif', dif[dif.length - 1], records[records.length - 1].Time);
            $.PlotLine('dea', dea[dea.length - 1], records[records.length - 1].Time);
            $.PlotLine('macd', macd[macd.length - 1], records[records.length - 1].Time);
        }
    }
    LogStatus("records.length:", records.length, records[records.length - 1]);
    // Log(records[records.length - 1]);
    Sleep(1000);
}
}
```

Detail

https://www.fmz.com/strategy/151972

Last Modified

2020-02-27 14:09:37
```