> Name

Dual-Thrust-MyLanguage-Version

> Author

Archimedes' Bathtub

> Strategy Description

[trans]
> Basic Principle

- At the close of the day, calculate two values: highest price minus closing price, and closing price minus lowest price. Take the larger of these two values, multiply it by the k-value, and the result is called the trigger value.
- At the opening of the next day, record the opening price. Immediately buy when the price exceeds (opening price + trigger value), or sell short immediately when the price falls below (opening price - trigger value).
- This system is a reversal system without a separate stop loss. That is, the reverse signal also serves as the position closing signal.

The Dual Thrust strategy includes complete chart display, dynamic chart updates, template references, and more. It can be used as a learning template.

Detailed introduction to the strategy: http://xueqiu.com/5256769224/32429363

- Main Chart:
  Upper Track: Formula: UPTRACK^^O+KS*RG;
  Lower Track: Formula: DOWNTRACK^^O-KX*RG;

- Sub Chart:
  None

||

- Fundamental:
  At the close of the day, two values are calculated: the highest price - the closing price, and the closing price - the lowest price. Then take the larger one and multiply it by the value of k. The result is called the trigger value.
  At the opening of the next day, record the opening price, then buy immediately when the price exceeds (opening price + trigger value), or sell short when the price is lower than (opening price - trigger value).
  This system is a reversal system with no separate stop loss. In other words, the reverse signal is also the closing signal.

  ![IMG](https://www.fmz.com/upload/asset/d2d373289db613f356811d9314775b83.jpg)  
  ![IMG](https://www.fmz.com/upload/asset/c6c5a6c53fa4f0c9c5971df9349e1dca.png)  
  ![IMG](https://www.fmz.com/upload/asset/65fd01ff1e7b844006ba18ad0ea3dedf.png) 

- Main chart:
  Upper track: formula: UPTRACK^^O+KS*RG;
  Lower track: formula: DOWNTRACK^^O-KX*RG;

- Secondary chart:
  none

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|N|4|Calculation Period|Period: calculate period|
|KS|0.5|Upper Track Coefficient|upper track coefficient|
|KX|0.5|Lower Track Coefficient|lower track coefficient|


> Source (MyLanguage)

``` pascal
(*backtest
start: 2018-01-01 00:00:00
end: 2018-02-28 00:00:00
period: 1d
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD"}]
args: [["ContractType","this_week",126961]]
*)

HH:=HV(H,N);
HC:=HV(C,N);
LL:=LV(L,N);
LC:=LV(C,N);

RG:=MAX(HH-LC,HC-LL);
UPTRACK^^O+KS*RG;
DOWNTRACK^^O-KX*RG;


C>UPTRACK,BPK;
C<DOWNTRACK,SPK;

```

> Detail

https://www.fmz.com/strategy/128884

> Last Modified

2019-08-20 10:47:50