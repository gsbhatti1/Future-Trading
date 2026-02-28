Name

Dynamic balancing strategy-python-version

Author

teddy



Source(python)

```python
# !usr/bin/python3
# *_* coding:utf-8 *_*
# The first dynamic balancing strategy written after learning python
# QQ: 5325049 Any deficiencies are welcome to be corrected.

import time

# Define the function to obtain market information and account information
def nowinfo():
    global NowTicker, NowAsset, NowCoinValue, AssetDiff
    NowTicker = exchange.GetTicker()  # Get market information
    NowAsset = exchange.GetAccount()  # Get account information
    NowCoinValue = NowTicker.Last * NowAsset.Stocks  # Calculate the net asset value of the currency
    AssetDiff = NowCoinValue - NowAsset.Balance  # Calculate the difference between currency assets and cash

# Define transaction execution function
def trade():
    if AssetDiff > NowAsset.Balance * 0.05:  # Determine whether the currency value exceeds 5% of the fund
        Log("The transaction will be executed with ", NowTicker.Buy, "Sell", AssetDiff / 2 / NowTicker.Buy,
            "Coin")
        exchange.SetPrecision(5, 5)  # Set pricing precision
        exchange.Sell(NowTicker.Buy, AssetDiff / 2 / NowTicker.Buy)  # Execute currency selling transaction
    elif AssetDiff < NowAsset.Balance * (-0.05):  # Determine whether the currency value is lower than 5% of the fund
        Log("The transaction will be executed with ", NowTicker.Sell, "Buy", AssetDiff / -2 / NowTicker.Sell,
            "Coin")
        exchange.SetPrecision(5, 5)  # Set pricing precision
        exchange.Buy(NowTicker.Sell, AssetDiff / -2 / NowTicker.Sell)  # Execute currency purchase transaction
    else:
        Log("Trading condition not triggered")

# Entry function, as long as it is defined, the system will automatically execute the function, no need to call it
def main():
    i = 0
    while i < 1000:  # Set the total number of executions
        nowinfo()  # Call the function to obtain market assets
        Log(NowTicker)  # Print market information
        Log(NowAsset)  # Print account information
        Log("Current currency balance:", NowAsset.Stocks)
        Log("Current fund balance:", NowAsset.Balance)
        Log("Current currency market value:", NowCoinValue)
        Log("Difference between currency market value and funds:", AssetDiff)
        trade()  # Call the transaction execution function
        i += 1  # conditional iteration
        Log("th", i, "end of cycle")
        time.sleep(60)  # Wait 60 seconds

```

Detail

https://www.fmz.com/strategy/152830

Last Modified

2019-06-22 18:35:30