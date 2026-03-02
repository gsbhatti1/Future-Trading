> Strategy Arguments


|Argument Name    |Default Value|Description|
|-----------------|-------------|-----------|
|`DEMA Length`     |21           |The length of the DEMA used for trend confirmation. A shorter value makes the strategy more sensitive to short-term trends.|
|`MACD Fast Len`   |12           |The fast period in the MACD calculation, which influences the sensitivity to recent price changes.|
|`MACD Slow Len`   |26           |The slow period in the MACD calculation, which affects the smoothing effect on older data. A longer value makes the strategy less sensitive to short-term fluctuations.|
|`MACD Signal Len` |9            |The signal line period, used for further confirmation of buy and sell signals. A shorter value results in more responsive signals but may also increase false positives.|
|`Use MACD Confirm`|True         |Whether to use the MACD histogram greater than 0 as an additional confirmation before issuing a buy signal based on DEMA cross.|
|`Stop Loss Value` |1             |The percentage of the entry price used for setting stop loss orders. A value less than 1 represents a lower risk profile, while higher values allow larger potential losses.|

---

> Strategy Parameters


```python
def init(self):
    self.set_parameters({
        'DEMA Length': 21,
        'MACD Fast Len': 12,
        'MACD Slow Len': 26,
        'MACD Signal Len': 9,
        'Use MACD Confirm': True,
        'Stop Loss Value': 1
    })
```

---

> Strategy Logic


```python
def on_bar(self, bar):
    # Calculate DEMA and MACD values
    dema = self.get_price('DEMA', period=21)
    macd_hist = self.get_indicator('MACD.HISTOGRAM')
    
    # Buy signal based on DEMA crossover and optional MACD confirmation
    if bar['Close'] > dema and (self.params.Use_MACD_Confirm or macd_hist > 0):
        self.buy()
        
    # Sell signal based directly on DEMA crossover
    elif bar['Close'] < dema:
        self.sell()
    
    # Set stop loss order
    if self.position.size > 0:
        self.stop_loss(order_type='STOCH', value=self.params.Stop_Loss_Value)
```

---

> Strategy Notes

This strategy uses a combination of DEMA and MACD indicators to generate buy/sell signals. The key idea is to use the DEMA for trend identification and the MACD for momentum confirmation, thereby improving signal reliability and reducing false positives.

The parameters can be adjusted based on market conditions to fine-tune the sensitivity and response time of the strategy.