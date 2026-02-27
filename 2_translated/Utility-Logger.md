```javascript
//var COLOR_ERROR = "#FF0000"
//var COLOR_WARN = "#FF0000"
//var COLOR_INFO = "#0000FF"
//var COLOR_DEBUG = "#000000"
var LEVEL_PATTERN = {
    DEBUG: 0,
    INFO: 1,
    WARNING: 2,
    ERROR: 3
}

$.changeLoggerLevel = function (val) {
    level = val
}

//var loggerLevel = [LEVEL_PATTERN.DEBUG, LEVEL_PATTERN.INFO, LEVEL_PATTERN.WARNING, LEVEL_PATTERN.ERROR][level]
$.Error = function (msg, obj, route = 'route') {
    if (level == 0 || "route" + routeFilter == route) {
        Log('[ERR] ', "[" + route.toUpperCase() + "]", msg, obj, '#0000FF')
    }

}

$.Warn = function (msg, obj, route = 'route') {
    if (routeFilter == 0 || "route" + routeFilter == route) {
        if (level <= LEVEL_PATTERN.WARNING) {
            Log('[WAR] ', "[" + route.toUpperCase() + "]", msg, obj, '#0000FF')
        }
    }
}

$.Info = function (msg, obj, route = 'route') {
    if (routeFilter == 0 || "route" + routeFilter == route) {
        if (level <= LEVEL_PATTERN.INFO) {
            Log('[INF] ', "[" + route.toUpperCase() + "]", msg, obj, '#0000FF')
        }
    }

}

$.Debug = function (msg, obj, route = 'route') {
    if (routeFilter == 0 || "route" + routeFilter == route) {
        if (level <= LEVEL_PATTERN.DEBUG) {
            Log('[DBG] ', "[" + route.toUpperCase() + "]", msg, obj, '#0000FF')
        }
    }
}

var executedBlocksCross = []
var executedBlocksCrossIds = []
var takerExecutionSummary = []
var executedTrades = []
var blocksLatency = []
var blocksLatencyV2 = []
var executedTradesTriangular = []
var positionHistory = []
var volumeHistory = []
var currentStatus = []
var blocksTimestamps = []

var tradesTable = {
    type: 'table',
    title: 'Executed Trades',
    cols: ['Timestamp', 'Label-Id', 'Contract', 'Exch-Id', 'Exchange', 'Side', 'Px', 'Amt', 'Fees'],
    rows: executedTrades
}

var timestampsTable = {
    type: 'table',
    title: 'Timestamps',
    cols: ['Label-Id', 'Exch-Mkr', 'Start', 'End', 'Mkr-Live', 'Cancel-Mkr', 'Cancel-Exec', 'Creating-Tkr', 'Tkr-Live', 'Complete'],
    rows: blocksTimestamps
}

var latencyTable = {
    type: 'table',
    title: 'Latency',
    cols: ['Label-Id', 'Exch-Mkr', 'Start', 'End', 'Book-T', 'Book-M', 'Mkr-Live', 'Cancel-Mkr', 'Cancel-Exec', 'Creating-Tkr', 'Tkr-Live', 'Complete'],
    rows: blocksLatencyV2
}

var posTable = {
    type: 'table',
    title: 'Position History',
    cols: ['Timestamp', 'Exch1', 'Exch2', 'Exch1-Pos', 'Exch2-Pos', 'Exposure'],
    rows: positionHistory
}

var volumeTable = {
    type: 'table',
    title: 'Volume Traded',
    cols: ['Date', 'Exch1', 'Exch2', 'Exch1-Trade Amt', 'Exch2-Trade Amt', 'Exch1-Total Volume', 'Exch2-Total Volume'],
    rows: volumeHistory
}

var blocksTableIds = {
    type: 'table',
    title: 'Executed Blocks - Ids',
    cols: ['Date', 'Label-Id', 'Exch-B', 'Exch-S', 'MkrId', 'TkrId', 'Route'],
    rows: executedBlocksCrossIds
}

var blocksTable = {
    type: 'table',
    title: 'Executed Blocks',
    cols: ['Date', 'Label-Id', 'Exch-B', 'Sprd-%', 'Slip-%', 'Sprd-$', 'Val', 'B-Px', 'S-Px', 'B-Amt', 'S-Amt', 'Lc', 'Lat', 'Tries'],
    rows: executedBlocksCross
}

var blocksTakerSummary = {
    type: 'table',
    title: 'Taker Exec',
    cols: ['Label-Id', 'Exch-B', 'Slip-%', 'Book-T', 'Book-M', 'Taker-Liq', 'Taker-Px-Init', 'Taker-Px-Sent'],
    rows: takerExecutionSummary
}

var tradesTable_triangular = {
    type: 'table',
    title: 'Executed Blocks',
    cols: ['Timestamp', 'Label-Id', 'Exc Sprd', 'Buy-Px', 'Sell-Px', 'Con-Px', 'Buy-Amt', 'Sell-Amt', 'Con-Amt', 'Mkr-Id', 'Tkr-Id', 'Con-Id', 'Loc', 'Lat-Exch', 'Lat-React'],
    rows: executedTradesTriangular
}

var currentStatusTable = {
    type: 'table',
    title: 'Current Status',
    cols: ['Timestamp', 'Variable Name', 'Route 1', 'Route 2', 'Route 3', 'Route 4'],
    rows: currentStatus
}

/*
    Logs the current status of the bot per route. Variables that it tracks:
    - Bot State
    - Taker Book
    - Maker Book

*/

$.logBotStatus = function () {
    currentStatus.push(
        [
            new Date().toLocaleString("da-DK"), // Timestamp
            "botState",
            _G("botStateroute1"),
            _G("botStateroute2"),
            _G("botStateroute3"),
            _G("botStateroute4")

        ]
    )
    LogStatus('`' + JSON.stringify([blocksTable, blocksTableIds, tradesTable, posTable, volumeTable, latencyTable, timestampsTable, currentStatusTable, blocksTakerSummary]) + '`')

}

/* LOC, represents the part of the code that triggered the liquidation.
    0- Order creation -> order executed as taker.
    1- Order Status -> normal check via websocket.
    2- Order Cancellation -> order was executed while the bot was trying to cancel it.
    3- REST Update -> bot had to check status via rest.
*/
```