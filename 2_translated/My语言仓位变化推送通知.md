Name

My language position change push notification

Author

inventor quantification


Source (MyLanguage)

```pascal
C>HV(H, 10),SPK;
C<LV(L, 15),BPK;
AUTOFILTER;

%%
// The following code is attached to any My language strategy and finally the position changes can be pushed to the mobile App and WeChat
if (typeof(scope._tmp) !== 'number') {
scope._tmp = 0;
}
var pos = scope.get_locals('BKVOL') - scope.get_locals('SKVOL');
if (pos != scope._tmp) {
scope._tmp = pos;
Log('Notification of position changes:', scope.symbol, pos, '@');
}
%%
```

Detail

https://www.fmz.com/strategy/305745

Last Modified

2021-08-09 14:01:30