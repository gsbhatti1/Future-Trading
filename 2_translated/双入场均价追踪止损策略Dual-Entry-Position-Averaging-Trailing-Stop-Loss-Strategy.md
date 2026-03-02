> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|1.15|Total Stop Loss|
|v_input_2|1.05|Enter Second trade @ what higher 5%?|
|v_input_3|0.95|First Trade Profit % Target|
|v_input_4|0.9|Second Trade Profit % Target|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-23 00:00:00
end: 2023-11-28 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//              @version=4
strategy("Dual Entry Position Averaging Trailing Stop Loss Strategy", "DEPALS", initial_capital=0)


//              DUAL ENTRIES
//              ADDS ON MORE SHARES IF THE PILOT TRADE DOES NOT REACH PROFIT TARGET
//              RED     LINE        == STOP LOSS LINE
//              GREEN   LINE        == PROFIT TARGET FOR THE 1ST TRADE
//              YELLOW  LINE        == ADD ON SHARES TO THE TRADE
//              WHITE   LINE        == PROFIT TARGET FOR THE 1ST & SECOND TRADE COMBINED


StopLossPerc        = input(1.15, "Total Stop Loss", step=0.01)


T2EntTrgPerc        = input(1.05, "Enter Second trade @ what higher 5%?", step=0.01)    //  BUY STOP LIMIT ONLY WHEN ONE TRADE IS ALREADY OPEN & AIMS TO BUY DOUBLE THE OWNED SHARES AT A HIGHER ENTRY PRICE // YELLOW LINE

T1ProfTrgPerc       = input(0.95, "First Trade Profit % Target", step=0.01)
T2ProfTrgPerc       = input(0.90, "Second Trade Profit % Target", step=0.01)            //  ADD ON PROFIT TARGET AFTER ENTERING THE SECOND TRADE // WHITE LINE
```

This Pine Script code defines the strategy with appropriate comments and inputs for stop loss percentage, second trade entry target, first and second trade profit targets.