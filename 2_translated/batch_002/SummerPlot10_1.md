<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

SummerPlot10

> Author

SummerPlot10

> Strategy Description

This strategy demonstrates how to draw various types of charts including line charts, bar charts, and pie charts using JavaScript in the FMZ platform. It fetches real-time market data such as buy and sell prices from an exchange and visualizes them dynamically on different chart panels.

> Source (javascript)

```javascript
//#region Version Updates
/*
------------  【1.0 Version】   ---------------------
----------- 2023.3.14 --------------
1. Initial version.
----------- 2023.3.16 --------------
1. Adjusted time range selector.
*/
//#endregion

var _Cfgs = [];
var _Chart = null;

function init() {
    _Chart = Chart([]);
    _Chart.reset();
    Log("SummerPlot init finished.");
}

function setChart(title, line, col, is_single, series_type, is_stock) {
    let char = _Cfgs.find(item => item?.title?.text === title);
    if (char) {
        char.extension.col = col;
        char.extension.layout = is_single ? 'single' : 'group';
        return char;
    } else {
        _Cfgs.push({
            __isStock: is_stock,
            tooltip: {
                xDateFormat: '%Y-%m-%d %H:%M:%S, %A'                // Tooltip date format
            },
            legend: {
                enabled: true,                                      // Curve user selectable
            },
            extension: {
                layout: is_single ? 'single' : 'group',
                col: col,
            },
            title: {
                text: title
            },
            xAxis: {
                type: 'datetime'
            },
            series: [{
                name: line,
                data: [],
                type: series_type,
            }],
            //#region Set optional time ranges
            rangeSelector: {
                buttons: [{
                    type: 'day',
                    count: 1,
                    text: '1d'
                }, {
                    type: 'day',
                    count: 7,
                    text: '7d'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1M'
                }, {
                    type: 'month',
                    count: 3,
                    text: '3M'
                }, {
                    type: 'month',
                    count: 6,
                    text: '6M'
                }, {
                    type: 'year',
                    count: 1,
                    text: '1Y'
                }, {
                    type: 'all',
                    text: 'All'
                }],
                selected: 2,
                inputEnabled: true
            },
            //#endregion
        });
    }
    return _Cfgs[_Cfgs.length - 1];
}

function getSeriesIndex(title, line, series_type) {
    let index = -1, cfg_index = -1, last_series_index = -1;
    for (let i = 0; i < _Cfgs.length; i++) {
        for (let j = 0; j < _Cfgs[i].series.length; j++) {
            index++;
            if (_Cfgs[i].title.text === title) {
                cfg_index = i;                              // Record corresponding chart index
                last_series_index = index;                  // Record last index of the chart
                if (_Cfgs[i].series[j].name === line && _Cfgs[i].series[j].type === series_type) {
                    // Found matching curve, directly return index
                    return index;
                }
            }
        }
    }
    // If no matching curve found
    _Cfgs[cfg_index].series.push({
        name: line,
        data: [],
        type: series_type,
    });
    return (last_series_index + 1);
}

$.PlotLineSummer = function(title, line, dot, date, col, is_single) {
    setChart(title, line, col, is_single, 'line', true);
    let index = getSeriesIndex(title, line, 'line');
    _Chart.add(index, [date, dot]);
    _Chart.update(_Cfgs);
}

$.PlotBarSummer = function(title, line, dot, date, col, is_single) {
    setChart(title, line, col, is_single, 'column', true);
    let index = getSeriesIndex(title, line, 'column');
    _Chart.add(index, [date, dot]);
    _Chart.update(_Cfgs);
}

$.PlotPieSummer = function(title, line, data, col, is_single) {
    let chart = setChart(title, line, col, is_single, 'pie', false);
    chart.series[0].data = data;
    _Chart.update(_Cfgs);
}

function main() {
    let count = 0;
    while (true) {
        Sleep(1000)
        let ticker = exchange.GetTicker()
        if (!ticker) {
            continue;
        }
        let diff = ticker.Sell - ticker.Buy;
        let time = new Date().getTime()
        $.PlotLineSummer('Bid/Ask Chart', 'Buy1', ticker.Buy, time, 12, true);
        $.PlotLineSummer('Bid/Ask Chart', 'Sell1', ticker.Sell, time, 12, true);
        $.PlotBarSummer('Spread Chart', 'Spread1', diff, time, 12, true);
        $.PlotBarSummer('Spread Chart', 'Spread2', diff * 2, time, 12, true);
        $.PlotLineSummer('Bid/Ask Chart2', 'Buy1', ticker.Buy, time, 8, true);
        $.PlotLineSummer('Bid/Ask Chart2', 'Sell1', ticker.Sell, time, 8, true);
        $.PlotLineSummer('Bid/Ask Chart3', 'Buy1', ticker.Buy, time, 4, true);
        $.PlotLineSummer('Bid/Ask Chart3', 'Sell1', ticker.Sell, time, 4, true);
        let data = [["A", 25 + (++count)],
                    ["B", 25 - count],
                    ["C", 25],
                    ["D", 25]];
        $.PlotPieSummer('Pie Chart1', 'Pie Chart1', data, 6, true);
        $.PlotPieSummer('Pie Chart2', 'Pie Chart2', data, 6, true);
    }
}
```

> Detail

https://www.fmz.com/strategy/404014

> Last Modified

2023-08-09 13:04:14