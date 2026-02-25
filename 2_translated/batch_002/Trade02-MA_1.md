> Name

Trade02-Aron Indicator MA Strategy

> Author

TradeMan

> Strategy Description

In order to give back to the FMZ platform and community, share strategies & codes & ideas & templates

Introduction:
Volume price factor combination

✱Contact information (welcome to communicate and discuss, learn and progress together)
WECHAT: haiyanyydss
TEL: https://t.me/JadeRabbitcm
✱Fully automatic CTA & HFT trading system @2018 - 2023

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|N|240|N|
|percent|5|percent|


> Source (MyLanguage)

``` pascal
(*backtest
start: 2018-01-01 09:00:00
end: 2021-07-30 15:00:00
Period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD","stocks":10,"fee":[0.05,0.05]}]
args: [["N",120],["SlideTick",0,126961],["ContractType","quarter",126961]]
*)



//LOTS:=MAX(1,INTPART(percent/100*MONEYTOT/(C*MARGIN*UNIT)));//Golden book
LOTS:= MAX(1,INTPART(percent/100*MONEYTOT*C/(MARGIN*UNIT)));//Coin book

MALONG:EMA(REF(C,1),N); //Calculate long-term moving average
HH_N:MIN(BARSLAST(HHV(H,N)>HHV(REF(H,1),N))+1,N);//Calculate the number of days after the highest price during the lookback time
LL_N:MIN(BARSLAST(LLV(L,N)<LLV(REF(L,1),N))+1,N);//Calculate the number of days after the lowest price during the lookback time

// N: Time window of lookback HH_N: Number of days after the highest price within the lookback period LL_N: Number of days after the lowest price within the lookback period

AROON_UP:=(N-HH_N)/N * 100;//Calculate the high price AROON indicator
AROON_DN:=(N-LL_N)/N * 100;//Calculate the low-price AROON indicator
AROON:=AROON_UP-AROON_DN;//Calculate the AROON indicator difference

//*How to use
//(1) When AROON_UP crosses 70 and AROON>0, it means that an upward trend is formed and a buy signal is generated;
//(2) When AROON_DOWN crosses 70 and AROON<0, it indicates that a downward trend has formed and a sell signal is generated;
//(3) When AROON_UP falls below 30 and AROON<0, it means that the upward trend has weakened and may reverse downward, generating a sell signal;
//(4) When AROON_DOWN crosses 30 and AROON>0, it means that the downward trend has weakened and may reverse upward, generating a buy signal.*/

DCOND1:=CROSSUP(AROON_UP,70) AND AROON>0;//Calculate long position opening condition 1
DCOND2:=CROSSDOWN(AROON_DN,30) AND AROON>0;//Calculate long position opening condition 2
KCOND1:=CROSSUP(AROON_DN,70) AND AROON<0;//Calculate short position opening one
KCOND2:=CROSSDOWN(AROON_UP,30) AND AROON<0;//Calculate short position opening two

PDCOND1:=AROON>0 AND CROSSDOWN(AROON_UP,50);//Calculate the long position closing conditions, when AROON is greater than 0 and AROON_UP crosses 50, the long position will be closed;
PKCOND1:=AROON<0 AND CROSSDOWN(AROON_DN,50);//Calculate the short position closing conditions. When AROON is less than 0 and AROON_DN crosses 50, the short position will be closed;

(DCOND1 OR DCOND2) AND BKVOL<=0 AND C>MALONG, BPK(LOTS);//The conditions for opening a long position 1 or 2 are met, and there are no long positions at the same time, and the price is greater than the long-term moving average, open a long position;
(KCOND1 OR KCOND2) AND SKVOL<=0 AND C<MALONG, SPK(LOTS);// Short position opening condition 1 or 2 is met, and there is no short position, and the price is lower than the long-term moving average, open a short position;

PDCOND1,SP(BKVOL);//Platform condition
PKCOND1,BP(SKVOL);//Short closing conditions
```

> Detail

https://www.fmz.com/strategy/425796

> Last Modified

2023-09-04 22:33:13