```javascript

/*
-- The strategy should call $.Test() to invoke this method after referencing the template.
-- The main function is not triggered in the strategy; it's only used as an entry point for template debugging.
*/

/* eslint no-unused-vars : "off" */
/* eslint no-constant-condition : "off" */
/* global _N $ Log GetAccount GetTicker GetRecords PD_LONG PD_SHORT */

var DEFAULT_MINAMOUNT = 1;
var DEFAULT_AMOUNTPRECISION = 2;
var DEFAULT_PRICEPRECISION = 4;

function findItem(array, keyName, value) {
    var result = null;
    value = value.toLowerCase().trim();

    for (var i = 0; i < array.length; i++) {
        if (array[i][keyName].toLowerCase().trim() == value) {
            result = array[i];
            break;
        }
    }

    if (!result && (value.includes('usd') && !value.includes('usdt'))) {
        value = value + 't';    // usd 在 币对里面肯定放在最后
        for (i = 0; i < array.length; i++) {
            if (array[i][keyName].toLowerCase().trim() == value) {
                result = array[i];
                break;
            }
        }
    }

    return result;
}

//1.0000 0.1.,..
function getPrecision(number) {
    // Log("test precision " + number);
    var str = String(number.toFixed(12)), result = 0;
    if (str[1] == '.')
        for (var i = 0; i < str.length; i++) {
            if (str[i] == '1') {
                if (i == 0)
                    result = 0;
                else
                    result = i - 1;
            }
        }

    // Log("test " + result);
    return result;
}

$.HasMinTotal = function(jiaoyisuo) {
    return (jiaoyisuo.toLowerCase().includes('binance'));
}

$.GetMinAmount = function (jiaoyisuo, bidui) {
    var item;
    var unknown = true, isHuobi, isOk, isBinance;
    if (jiaoyisuo.toLowerCase().includes('huobi')) {
        isHuobi = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('ok')) {
        isOk = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('binance')) {
        isBinance = true;
        unknown = false;
    }

    if (isHuobi || unknown)
        item = findItem(huobiMinAmounts, "symbol", bidui);
    if (isBinance || (unknown && !item))
        item = findItem(binanceRegulation, "symbol", bidui);
    if (isOk || (unknown && !item))
        item = findItem(okexRegulation, "symbol", bidui);

    if (item)
        return item.minamount;

    return DEFAULT_MINAMOUNT;
}

$.GetAmountPrecision = function (jiaoyisuo, bidui) {
    var item;
    var unknown = true, isHuobi, isOk, isBinance;
    if (jiaoyisuo.toLowerCase().includes('huobi')) {
        isHuobi = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('ok')) {
        isOk = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('binance')) {
        isBinance = true;
        unknown = false;
    }

    if (isHuobi || unknown) {
        item = findItem(huobiPrecisions, "symbol", bidui);
        if (item)
            return item.amountprecision;
    }

    if (isBinance || (unknown && !item)) {
        item = findItem(binanceRegulation, "symbol", bidui);
        if (item)
            return getPrecision(item.minamount);    // Binance uses the minimum amount as the amount precision
    }

    if (isOk || (unknown && !item)) {
        item = findItem(okexRegulation, "symbol", bidui);
        if (item)
            return getPrecision(item.amountprecision);
    }

    return DEFAULT_AMOUNTPRECISION;
}

$.GetPricePrecision = function (jiaoyisuo, bidui) {
    var item;
    var unknown = true, isHuobi, isOk, isBinance;
    if (jiaoyisuo.toLowerCase().includes('huobi')) {
        isHuobi = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('ok')) {
        isOk = true;
        unknown = false;
    }
    else if (jiaoyisuo.toLowerCase().includes('binance')) {
        isBinance = true;
        unknown = false;
    }

    if (isHuobi || unknown) {
        item = findItem(huobiPrecisions, "symbol", bidui);
        if (item)
            return item.priceprecision;
    }

    if (isBinance || (unknown && !item)) {
        item = findItem(binanceRegulation, "symbol", bidui);
        // Log("test Binance PricePrecision=" + item.priceprecision + " item=" + JSON.stringify(item));
        if (item) {
            // Binance data is incorrect; eth has 6 digits, btc has 7 digits, but the list shows 8 digits
            var binanceP = getPrecision(item.priceprecision);
            if (binanceP > 6) binanceP = 6; // Force to use 6 digits

            return binanceP;
        }
    }

    if (isOk || (unknown && !item)) {
        item = findItem(okexRegulation, "symbol", bidui);
        if (item)
            return getPrecision(item.priceprecision);
    }

    return DEFAULT_PRICEPRECISION;
}

$.GetMinTotal = function (jiaoyisuo, bidui) {
    var item;
    var unknown = true, isBinance;

    if (jiaoyisuo.toLowerCase().includes('binance')) {
        isBinance = true;
        unknown = false;
    }

    if (isBinance || unknown) {
        item = findItem(binanceRegulation, "symbol", bidui);
        if (item)
            return item.minstock;
    }

    return 0;
}

var huobiMinAmounts = [
{"symbol":"AST_BTC", "minamount":1},
{"symbol":"ACT_BTC", "minamount":0.1},
{"symbol":"ADX_BTC", "minamount":0.01},
{"symbol":"ABT_BTC", "minamount":0.1},
{"symbol":"APPC_BTC", "minamount":0.01},
{"symbol":"AIDOC_BTC", "minamount":1},
{"symbol":"BAT_BTC", "minamount":1},
{"symbol":"BCH_BTC", "minamount":0.001},
{"symbol":"BCX_BTC", "minamount":1},
{"symbol":"BTG_BTC", "minamount":0.001},
{"symbol":"BCD_BTC", "minamount":0.001},
{"symbol":"BTM_BTC", "minamount":1},
{"symbol":"BIFI_BTC", "minamount":0.01},
{"symbol":"BLZ_BTC", "minamount":0.1},
{"symbol":"CMT_BTC", "minamount":0.1},
{"symbol":"CVC_BTC", "minamount":0.1},
{"symbol":"CHAT_BTC", "minamount":0.01}
];
```

Please note that the translation of human-readable text has been preserved while maintaining the original code blocks and formatting as specified.