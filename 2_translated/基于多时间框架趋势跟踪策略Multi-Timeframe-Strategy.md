``` pinescript
/*backtest
start: 2024-01-19 00:00:00
end: 2024-02-18 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("[RichG] Easy MTF Strategy v1.1", overlay=false)

TF_1_time = input("D", "Timeframe 1")
TF_2_time = input("10D", "Timeframe 2")
TF_3_time = input("15D", "Timeframe 3")
TF_4_time = input("30D", "Timeframe 4")
lengthKC = input(20, title="KC Length")
multKC = input(1.5, title="KC MultFactor")
lengthBB = input(20, title="BB Length")
transaction_size = input(1, "Contract/Share Amount")

src = close, len = 20


out = sma(src, len)
width = 5
upcolor = green
downcolor = red
neutralcolor = blue
linestyle = line


kc() =>
    ma = sma(close, lengthKC)
    range = tr
    rangema = sma(range, lengthKC)
    upperKC = ma + rangema * multKC
    lowerKC = ma - rangema * multKC
    [lowerKC, upperKC] 

 
bb() =>
    source = close 
    basis = sma(source, lengthBB)
    dev = multKC * stdev(source, lengthBB)
    upperBB = basis + dev
    lowerBB = basis - dev
    [upperBB, lowerBB]

TF_1 = request.security(syminfo.tickerid, TF_1_time, open) < request.security(syminfo.tickerid, TF_1_time, close) ? true : false
TF_1_color = TF_1 ? upcolor : downcolor

TF_2 = request.security(syminfo.tickerid, TF_2_time, open) < request.security(syminfo.tickerid, TF_2_time, close) ? true : false
TF_2_color = TF_2 ? upcolor : downcolor

TF_3 = request.security(syminfo.tickerid, TF_3_time, open) < request.security(syminfo.tickerid, TF_3_time, close) ? true : false
TF_3_color = TF_3 ? upcolor : downcolor

TF_4 = request.security(syminfo.tickerid, TF_4_time, open) < request.security(syminfo.tickerid, TF_4_time, close) ? true : false
TF_4_color = TF_4 ? upcolor : downcolor

TF_global = TF_1 and TF_2 and TF_3 and TF_4 
TF_global_bear = TF_1 == false and TF_2 == false and TF_3 == false and TF_4 == false
TF_global_color = TF_global ? green : TF_global_bear ? red : white
TF_trigger_width = TF_global ? 6 : width

plot(1, style=linestyle, linewidth=width, color=TF_1_color)
plot(5, style=linestyle, linewi
```