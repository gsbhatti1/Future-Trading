``` javascript
/**
 * desc: $.GetRecordsByLength is an interface function of this template library, used to get K-line data with a specified length.
 * @param {Object} e - Exchange object
 * @param {Int} period - K-line interval in seconds
 * @param {Int} length - The specified length of the K-line data to be retrieved. This is specific to the exchange API limits.
 * @returns {Array<Object>} - K-line data
 */
$.GetRecordsByLength = function(e, period, length) {
    if (!Number.isInteger(period) || !Number.isInteger(length)) {
        throw "params error!"
    }

    var exchangeName = e.GetName()
    if (exchangeName == "Futures_Binance") {
        return getRecordsForFuturesBinance(e, period, length)
    } else {
        throw "not support!"
    }
}

/**
 * desc: getRecordsForFuturesBinance is the specific implementation of the function to retrieve K-line data from Binance Futures exchange.
 * @param {Object} e - Exchange object
 * @param {Int} period - K-line interval in seconds
 * @param {Int} length - The specified length of the K-line data to be retrieved. This is specific to the exchange API limits.
 * @returns {Array<Object>} - K-line data
 */
function getRecordsForFuturesBinance(e, period, length) {
    var contractType = e.GetContractType()
    var currency = e.GetCurrency()
    var strPeriod = String(period)

    var symbols = currency.split("_")
    var baseCurrency = ""
    var quoteCurrency = ""
    if (symbols.length == 2) {
        baseCurrency = symbols[0]
        quoteCurrency = symbols[1]
    } else {
        throw "currency error!"
    }

    var realCt = e.SetContractType(contractType)["instrument"]
    if (!realCt) {
        throw "realCt error"
    }
    
    // m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    var periodMap = {}
    periodMap[(60).toString()] = "1m"
    periodMap[(60 * 3).toString()] = "3m"
    periodMap[(60 * 5).toString()] = "5m"
    periodMap[(60 * 15).toString()] = "15m"
    periodMap[(60 * 30).toString()] = "30m"
    periodMap[(60 * 60).toString()] = "1h"
    periodMap[(60 * 60 * 2).toString()] = "2h"
    periodMap[(60 * 60 * 4).toString()] = "4h"
    periodMap[(60 * 60 * 6).toString()] = "6h"
    periodMap[(60 * 60 * 8).toString()] = "8h"
    periodMap[(60 * 60 * 12).toString()] = "12h"
    periodMap[(60 * 60 * 24).toString()] = "1d"
    periodMap[(60 * 60 * 24 * 3).toString()] = "3d"
    periodMap[(60 * 60 * 24 * 7).toString()] = "1w"
    periodMap[(60 * 60 * 24 * 30).toString()] = "1M"
    
    var records = []
    var url = ""
    if (quoteCurrency == "USDT") {
        // GET https://fapi.binance.com /fapi/v1/klines symbol , interval , startTime , endTime , limit 
        // limit max value: 1500

        url = "https://fapi.binance.com/fapi/v1/klines"
    } else if (quoteCurrency == "USD") {
        // GET https://dapi.binance.com /dapi/v1/klines symbol , interval , startTime , endTime , limit
        // startTime and endTime can be at most 200 days apart
        // limit max value: 1500

        url = "https://dapi.binance.com/dapi/v1/klines"
    } else {
        throw "not support!"
    }

    var maxLimit = 1500
    var interval = periodMap[strPeriod]
    if (typeof(interval) !== "string") {
        throw "period error!"
    }

    var symbol = realCt
    var currentTS = new Date().getTime()

    while (true) {
        // Calculate limit
        var limit = Math.min(maxLimit, length - records.length)
        var barPeriodMillis = period * 1000
        var rangeMillis = barPeriodMillis * limit
        var twoHundredDaysMillis = 200 * 60 * 60 * 24 * 1000
        
        if (rangeMillis > twoHundredDaysMillis) {
            limit = Math.floor(twoHundredDaysMillis / barPeriodMillis)
            rangeMillis = barPeriodMillis * limit
        }

        var query = `symbol=${symbol}&interval=${interval}&endTime=${currentTS}&limit=${limit}`
        var retHttpQuery = HttpQuery(url + "?" + query)
        
        var ret = null 
        try {
            ret = JSON.parse(retHttpQuery)
        } catch(e) {
            Log(e)
        }
        
        if (!ret || !Array.isArray(ret)) {
            return null
        }
        
        // If outside the exchange's query range or no data found
        if (ret.length == 0 || currentTS <= 0) {
            break
        }

        for (var i = ret.length - 1; i >= 0; i--) {
            var ele = ret[i]
            var bar = {
                Time : parseInt(ele[0]),
                Open : parseFloat(ele[1]),
                High : parseFloat(ele[2]),
                Low : parseFloat(ele[3]), 
                Close : parseFloat(ele[4]),
                Volume : parseFloat(ele[5])
            }

            records.unshift(bar)
        }

        if (records.length >= length) {
            break
        }

        currentTS -= rangeMillis
        Sleep(1000)
    }

    return records
}

/**
 * desc: $.UpdataRecords is an interface function of this template library, used to update K-line data.
 * @param {Object} e - Exchange object
 * @param {Array<Object>} records - The source of the updated K-line data
 * @param {Int} period - K-line interval. Needs to be consistent with the K-line data cycle in the records parameter.
 * @returns {Bool}  - Whether the update was successful
 */
$.UpdataRecords = function(e, records, period) {
    var r = e.GetRecords(period)
    if (!r) {
        return false 
    }

    for (var i = 0; i < r.length; i++) {
        if (r[i].Time > records[records.length - 1].Time) {
            // Add new Bar
            records.push(r[i])
            // Update the previous Bar
            if (records.length - 2 >= 0 && i - 1 >= 0 && records[records.length - 2].Time == r[i - 1].Time) {
                records[records.length - 2] = r[i - 1]
            }            
        } else if (r[i].Time == records[records.length - 1].Time) {
            // Update Bar
            records[records.length - 1] = r[i]
        }
    }
    return true
}

// Template test function
function main() {
    Log("The current test exchange:", exchange.GetName())

    // If it is a futures, set the contract type
    exchange.SetContractType("swap")

    // Use $.GetRecordsByLength to retrieve K-line data with a specified length. The period is 60 seconds, i.e., one-minute K-lines, and the length is 8000 bars.
    var r = $.GetRecordsByLength(exchange, 60, 8000)
    Log(r)

    // Check the data
    var diffTime = r[1].Time - r[0].Time 
    Log("diffTime:", diffTime, " ms")
    for (var i = 0; i < r.length; i++) {
        for (var j = 0; j < r.length; j++) {
            // 
```

Note: The last code block was cut off. Please continue or complete the intended logic as needed.