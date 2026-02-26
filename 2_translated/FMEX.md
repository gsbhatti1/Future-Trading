``` javascript
exchange.SetBase(Url)
if(exchange.GetName() != 'Futures_FMex') {
    throw 'This strategy only supports FMEX Futures'
}

var account = null
var records = null 
var pos = {direction: 'empty', price: 0, amount: 0, unrealised_profit: 0}


var total_efficiency = 0 // Total efficiency
var my_efficiency = 0

var ordersInfo = {buyId: 0, buyPrice: 0, sellId: 0, sellPrice: 0}
var coverInfo = {buyId: 0, buyPrice: 0, sellId: 0, sellPrice: 0}
var depthInfo = {asks: [], bids: []}
var lastProfitTime = 0 // Control profit print time
var lastRestTime = Date.now()   // Timer reset strategy
var lastLogStatusTime = 0
var lastPeriod = 0
var today = _D().slice(8,11)

updateAccount()

var total_back = 0
if(_G('total_back')) {
    total_back = _G('total_back')
} else {
    _G('total_back', total_back)
}
var init_value = 0
if(_G('init_value')) {
    init_value = _G('init_value')
} else {
    init_value = _N(account.Info.data.BTC[0] + account.Info.data.BTC[1] + account.Info.data.BTC[2], 6)
    Log('First start of the strategy, initial total value: ', init_value)
    _G('init_value', init_value)
}

function updateRecords() {
    var data = exchange.GetRecords(60)
    if(data) {
        records = data
    } else {
        Log('Error fetching market data')
    }
}

function updateAccount() {
    var data = exchange.GetAccount()
    if(data) {
        account = data
    } else {
        Log('Error fetching account data')
    }
}

function updatePosition() {
    var data = exchange.GetPosition()
    if(data) {
        if(data.length > 0) {
            if(data[0].Info.direction != pos.direction || data[0].Info.quantity != pos.amount) {
                Log('Position changed: ', pos.direction + ' ' + pos.amount + ' -> ' + data[0].Info.direction + ' ' + data[0].Info.quantity)
            }
            pos = {direction: data[0].Info.direction, price: data[0].Info.entry_price, amount: data[0].Info.quantity, unrealised_profit: data[0].Info.unrealized_pnl}
        } else {
            if(pos.amount) {
                Log('Position changed: ', pos.direction + ' ' + pos.amount + ' -> ' + 'empty')
            }
            pos = {direction: 'empty', price: 0, amount: 0, unrealised_profit: 0}
        }
    } else {
        Log('Error fetching position data')
    }
}

function calcEfficiency() {
    total_efficiency = 0
    for(var i = 0; i < records.length; i++) {
        total_efficiency += 1000000 * (Amount / (records[i].Volume + Amount)) * 0.3 * 0.5 / 2880
    }
    if(_D().slice(17) > 57) {
        my_efficiency = 1000000 * (Amount / (records[records.length - 1].Volume + Amount)) * 0.3 * 0.5 / 2880
    }
}

function logStatus() {
    if(Date.now() - lastLogStatusTime < 4000) {
        return
    }
    lastLogStatusTime = Date.now()
    var leverage = pos.amount / (account.Info.data.BTC[0] * (depth.Asks[0].Price + depth.Bids[0].Price) / 2)
    var table1 = {type: 'table', title: 'Account Information',
             cols: ['Available Margin', 'Frozen Margin', 'Position Margin', 'Direction', 'Quantity', 'Entry Price', 'Unrealized Profit', 'Used Leverage', 'Initial Capital', 'Profit/Loss', 'Buy Price', 'Sell Price', 'Average Efficiency', 'My Efficiency'],
             rows: [[_N(account.Info.data.BTC[0], 6), _N(account.Info.data.BTC[1], 6), _N(account.Info.data.BTC[2], 6),
                     pos.direction, pos.amount, _N(pos.price, 2), _N(pos.unrealised_profit, 5), _N(leverage, 2),
                     _N(init_value, 6), _N(account.Info.data.BTC[0] - init_value, 6), ordersInfo.buyPrice, ordersInfo.sellPrice,
                     _N(total_efficiency / records.length, 2), _N(my_efficiency, 2)
                    ]]
                 }
    var table2 = {type: 'table', title: 'Order Information', cols: ['Position', 'Buy Price', 'Buy Amount', 'Efficiency', 'Sell Price', 'Sell Amount', 'Efficiency'], rows: []}
    for(var i = 0; i < 15; i++) {
        // Log(i+1, depthInfo.bids[i][1], depthInfo.bids[i][2], depthInfo.bids[i][3], depthInfo.asks[i][1], depthInfo.asks[i][2], depthInfo.asks[i][3])
        table2.rows.push([i + 1, depthInfo.bids[i][1], depthInfo.bids[i][2], depthInfo.bids[i][3], depthInfo.asks[i][1], depthInfo.asks[i][2], depthInfo.asks[i][3]])
    }
    if(_D().slice(8,11) != today) {
        today = _D().slice(8,11)
        Log('Total unlocked amount millionth of yesterday: ', total_back). Log('Today reset statistics')
        total_back = 0
    }
    var logString = 'Current mining period: '+_D().slice(11,14) + nowPeriod*5 + ' - ' + _D().slice(11,14) + (nowPeriod*5+5) + ' ' + 'Sorted mining obtained the millionth of today's unlocked total amount of ' + _N(total_back, 4) + '\n'
    LogStatus(logString + '`' + JSON.stringify(table1) + '`\n' + '`' + JSON.stringify(table2) + '`')
    if(Date.now() - lastProfitTime > ProfitTime * 1000) {
        updateAccount()
        lastProfitTime = Date.now()
        LogProfit(_N(account.Info.data.BTC[0] + account.Info.data.BTC[1] + account.Info.data.BTC[2], 6))
    }
}

function cancelAll() { // Reset strategy to prevent some orders from being stuck, which may affect other running strategies
    var orders = exchange.GetOrders()
    if(orders) {
        for(var i = 0; i < orders.length; i++) {
            exchange.CancelOrder(orders[i].Id)
        }
        ordersInfo = {buyId: 0, buyPrice: 0, sellId: 0, sellPrice: 0}
    }
}

function coverPosition() {
    if(pos.amount > 0) {
        if(pos.direction == 'long') { // Cover long position by taking a market order, which will incur trading fees. This can be changed to limit orders, but it increases the risk of holding positions.
            var sellPrice = _N(pos.price, 0) + _N(CoverCost, 0)
            if(sellPrice != coverInfo.sellPrice) {
                if(coverInfo.sellId) {
                    exchange.CancelOrder(coverInfo.sellId)
                    coverInfo.sellId = 0
                }
                exchange.SetDirection('sell')
                var sellId = exchange.Sell(sellPrice, pos.amount, 'Cover long position')
                coverInfo.sellPrice = sellPrice
                if(sellId) {
                     coverInfo.sellId = sellId
                } else {
                    coverInfo.sellId = 0
                }
            }
        } else {
            var buyPrice = _N(pos.price, 0) - _N(CoverCost, 0)
            if(buyPrice != coverInfo.buyPrice) {
                if(coverInfo.buyId) {
                    exchange.CancelOrder(coverInfo.buyId)
                    coverInfo.buyId = 0
                }
                exchange.SetDirection('buy')
                var buyId = exchange.Buy(buyPrice, pos.amount, 'Cover short position')
                coverInfo.buyPrice = buyPrice
                if(buyId) {
                     coverInfo.buyId = buyId
                } else {
                    coverInfo.buyId = 0
                }
            }
        }
    }
}
```