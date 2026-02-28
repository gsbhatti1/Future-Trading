```markdown
Name

MACDMA indicator combination strategy that you don’t know MACDMA-Indicator-Combination-Strategy

Author

Zero

Strategy Description

This issue shares the MACD+MA indicator combination strategy. In technical analysis, the combination of indicators is very common. Different indicators combined have different operating points and analysis methods. The combination of indicators can enhance the accuracy of signals. This strategy is to judge the state of the market by comparing the relationship between price and MA, and then using the MACD indicator to measure the acceleration of price movement, and build a simple timing trading strategy.

The MA (Moving Average) indicator is short for "Moving average" in English and is called the moving average indicator. The moving average (MA) has a trending characteristic, which is relatively stable, unlike the daily K-line that will rise and fall. The longer the moving average, the more stable its performance; it is less prone to fluctuations, requiring you to wait for the true clarity of the stock price trend.

In this issue, we share the MACD+MA index combination strategy. In technical analysis, the combination of indicators is very common. Different indicators have different operation points and analysis methods. The combination of indicators can enhance the accuracy of the signal. The strategy is to compare the relationship between price and MA, and then measure the price movement acceleration using the MACD indicator to judge the state of the market and construct a simple timing trading strategy.

Source (MyLanguage)

```pascal
(*backtest
start: 2018-11-01 00:00:00
end: 2018-11-22 00:00:00
Period: 1h
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD"}]
*)

// MACD calculation
FASTLENGTH:=12;
SLOWLENGTH:=26;
MACDLENGTH:=9;

// Length of MA
L1:=50;
L2:=120;

// Stop loss 5%
STOPLOSS:=5;

// MACD
MACDVALUE:=EMA(CLOSE,FASTLENGTH)-EMA(CLOSE,SLOWLENGTH);
AVGMACD:=EMA(MACDVALUE,MACDLENGTH);
MACDDIFF:=MACDVALUE-AVGMACD;

// MA1, MA2
DMA1:=MA(C,L1);
DMA2:=MA(C,L2);
BUYCONDITION:=MACDVALUE>0 && DMA1>DMA2 && MACDDIFF>0 && C>DMA1 && REF(C,1)>REF(DMA1,1);
SELLCONDITION:=MACDVALUE<0 && DMA1<DMA2 && MACDDIFF<0 && C<DMA1 && REF(C,1)<REF(DMA1,1);

// Open position conditions
BKVOL=0 AND BUYCONDITION,BK;
SETSIGPRICETYPE(BK,NEW_ORDER);
SKVOL=0 AND SELLCONDITION,SK;
SETSIGPRICETYPE(SK,NEW_ORDER);

// Exit condition
BKVOL>0 AND (REF(MACDVALUE,1)<0 OR REF(DMA1,1)<REF(DMA2,1)),SP;
SKVOL>0 AND (REF(MACDVALUE,1)>0 OR REF(DMA1,1)>REF(DMA2,1)),BP;

// Start stop loss
SKVOL>0 AND HIGH>=SKPRICE*(1+STOPLOSS*0.01),BP;
BKVOL>0 AND LOW<=BKPRICE*(1-STOPLOSS*0.01),SP;
AUTOFILTER;
```

Detail

https://www.fmz.com/strategy/127101

Last Modified

2018-12-14 10:25:27
```