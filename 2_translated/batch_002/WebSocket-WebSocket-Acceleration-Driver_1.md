``` javascript
function main() {
    $.setupWebsocket()
    while (true) {
        exchanges.map(e=>{
            Log(e.GetName(), e.GetDepth())
            Log(e.GetName(), e.GetTrades())
            // support custom and auto subscribe Eg: e.GetDepth('ETH_USDT')
        })
        EventLoop(100) // trigger by websocket or use Sleep control delay
    }
}
```





> Source (javascript)

``` javascript
// @ts-check

$.setupWebsocket = function(main_exchanges) {
    let crc32 = function (r) {
        for (var a, o = [], c = 0; c < 256; c++) {
            a = c;
            for (var f = 0; f < 8; f++) a = 1 & a ? 3988292384 ^ a >>> 1 : a >>> 1;
            o[c] = a
        }
        for (var n = -1, t = 0; t < r.length; t++) n = n >>> 8 ^ o[255 & (n ^ r.charCodeAt(t))];
        return (-1 ^ n) >>> 0
    }

    let trace = function (...args: any[]) {
        args.unshift('#' + __threadId())
        Log.apply(this, args)
    }
    
    let MyDial = function(address) : IDial {
        let ws = Dial(address)
        if (ws) {
            let createTime = new Date().getTime()
            let oldClose = ws.close
            ws.close = function() {
                oldClose.apply(ws)
                trace(address, "closed after", (new Date().getTime() - createTime)/1e6, "seconds")
            }
        }
        trace("connect", address, ws ? "success" : "failed")
        return ws
    }

    interface ICtx {
        name: string
        symbols: string[]
        callback?: Function
    }
    let lastUpdateSymbolsTime = new Date().getTime()
    let updateSymbols = function(ctx: ICtx, callBack: Function) {
        let ts = new Date().getTime()
        if (ts - lastUpdateSymbolsTime < 5000) {
            return
        }
        lastUpdateSymbolsTime = ts
        let e = __threadPeekMessage(-1)
        if (e) {
            trace("subscribe", e, "#ff0000")
            callBack(e.symbol, e.method)
            if (e.method == "subscribe") {
                ctx.symbols.push(e.symbol)
            } else {
                ctx.symbols = ctx.symbols.filter(symbol=>symbol!=e.symbol)
            }
        }
    }

    let supports = {}
    supports["Binance"] = function (ctx:ICtx) {
        let processMsg = function (obj) {
            let event = {
                ts: obj.E,
                instId: obj.s,
                depth: null,
                trades: [],
            }

            if (obj.e == "depthUpdate") {
                let depth = {
                    asks: [],
                    bids: []
                }
                obj.b.forEach(function (item) {
                    depth.bids.push({
                        price: Number(item[0]),
                        qty: Number(item[1])
                    })
                })
                obj.a.forEach(function (item) {
                    depth.asks.push({
                        price: Number(item[0]),
                        qty: Number(item[2])
                    })
                })
                event.depth = depth
            } else if (obj.e == "trade") {
                let trade = {
                    ts: obj.T,
                    id: obj.t,
                    side: obj.S == 'sell' ? 'Sell' : 'Buy',
                    price: Number(obj.p),
                    size: Number(obj.q)
                }
                event.trades.push(trade)
            }

            ctx.callback && ctx.callback(event)
        }
    }
}
```