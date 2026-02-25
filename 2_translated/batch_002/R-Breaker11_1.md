> Name

R-Breaker11 Trading Strategy

> Author

Taiji

> Strategy Description

R-Breaker Trading Strategy


> Source (python)

```python
#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
# Remove reversal stop loss
import math
import talib
def adjustFloat(v):
    v =math.floor(v*1000)
    return v/1000

def GetAccount():
    account = _C(exchange.GetAccount)
    while account == None:
        account = _C(exchange.GetAccount)
        Sleep(1000)
    return account

def GetTicker():
    ticker = exchange.GetTicker()
    while ticker == None:
        ticker = exchange.GetTicker()
        Sleep(1000)
    return ticker
# def updateProfit(accountInit, accountNow, ticker):
#     netNow = accountNow.Balance + accountNow.FrozenBalance + ((accountNow.Stocks + accountNow.FrozenStocks) * ticker.Buy)
#     netInit = accountInit.Balance + accountInit.FrozenBalance + ((accountInit.Stocks + accountInit.FrozenStocks) * ticker.Buy)
#     LogProfit(adjustFloat(netNow - netInit), accountNow)

# Get current account total
def GetNowamount():
    account = GetAccount()
    ticker = exchange.GetTicker()
    return account.Balance + account.FrozenBalance + ((account.Stocks + account.FrozenStocks) * ticker.Buy)
# Get current market value of stocks
def GetStockcap():
    account=GetAccount()
    ticker = GetTicker()
    return (account.Stocks + account.FrozenStocks) * ticker.Buy

# type 0: total holding ratio, 1: percentage of tradable coins
def my_buy(ratio,type):
    try:
        global InitAccount
        account = GetAccount()
        ticker=_C(exchange.GetTicker)
        # Calculate purchase quantity
        if type == 0:
            unit =(GetNowamount()/ticker.Buy)*ratio - account.Stocks - account.FrozenStocks
        else:
            unit =((GetNowamount()/ticker.Buy) - account.Stocks - account.FrozenStocks)*ratio
        
        # Insufficient minimum trading, exit purchase operation
        if unit < exchange.GetMinStock():
            return 0
        Dict = ext.Buy(unit)
        if(Dict):# Confirm successful opening position
            # buy_price=Dict['price'] # Purchase price   #{'price': 4046.446, 'amount': 1.5}
            # buy_qty=Dict['amount']  # Purchase quantity
            # LogProfit(_N(gains,4),'Opening information: Money:',initAccount.Balance,'--Coins:',initAccount.Stocks,'--Opening details:',Dict)
            # updateProfit(InitAccount, GetAccount(), GetTicker())
            Balance_log() # Profit calculation
            print_log(1,InitAccount)
            return 1
        return 0
    except Exception as ex:
        Log('except Exception my_buy:',ex)
        return 0

def my_sell(ratio,type):
    try:
        global InitAccount
        account = GetAccount()
        if type == 0:
            unit = 1
        else:
            unit =(account.Stocks + account.FrozenStocks)*ratio

        if unit<exchange.GetMinStock():
            return 0

        Dict = ext.Sell(unit)
        if(Dict):
            # updateProfit(InitAccount, GetAccount(), GetTicker())
            Balance_log() # Profit calculation
            print_log(0,GetAccount())
            return 1
    except Exception as ex:
        Log('except Exception my_sell:',ex)
        return 0

########################################################
import datetime
def Caltime(date1,date2):
    try:
        date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
        date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        return date2-date1
    except Exception as ex:
        Log('except Exception Caltime:',ex)
        return "except Exception"

import time
start_timexx =time.localtime(time.time()) #time.clock()
start_time=time.strftime("%Y-%m-%d %H:%M:%S",start_timexx)
buy_price=0 # Purchase price
buy_qty=0  # Purchase quantity
gains=0  # Profit

beng_Account = ext.GetAccount()  # Initial information
beng_ticker = _C(exchange.GetTicker).Last# Ticker 	Market condition   Last trade price
beng_Balance=(beng_Account.Stocks*beng_ticker)+beng_Account.Balance # Initial account money

def Balance_log(): # Profit calculation
    try:
        end_Account = ext.GetAccount()  # Current account information
        end_ticker = _C(exchange.GetTicker).Last# Ticker 	Market condition   Last trade price
        end_Balance=(end_Account.Stocks*end_ticker)+end_Account.Balance # Current money on the balance sheet
        LogProfit(end_Balance-beng_Balance) 	# Record profit value
    except Exception as ex:
        Log('except Exception Balance_log:',ex)

def print_log(k_p,data=""):  # Output
    try:
        name=""
        if k_p:
            name="Opening"
        else:
            name="Closing"
        global beng_Account,beng_ticker,beng_Balance
        global R1,R2,R3,S1,S2,S3
        global gains
        end_Account = ext.GetAccount()  # Current account information
        end_ticker = _C(exchange.GetTicker).Last# Ticker 	Market condition   Last trade price
        #################################################
        date1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        msg_data0=("This operation started at %s and has been running for %s\r\n"%(start_time,Caltime(start_time,date1)))
        #################################################
        msg_data1=("Initial status: %s\nCurrent status: %s\n"%(beng_Account,end_Account))
        #################################################
        end_Balance=(end_Account.Stocks*end_ticker)+end_Account.Balance # Current money on the balance sheet
        msg_data2=("Initial money: %s Current money: %s Profit/Loss: %s\r\n"%(str(beng_Balance),str(end_Balance),str(end_Balance-beng_Balance)))
        #################################################
        total = end_Account.Balance+end_Account.Stocks*_C(exchange.GetTicker).Last # Total account value
        roi = ((total/beng_Balance) -1)*100
        msg_data3=("Current status: %s--Money: %s--Coins: %s--Approximate total value: %.2f\r\n"%(str(name),str(end_Account.Balance),str(end_Account.Stocks),roi))
        #################################################
        income = total - beng_Account['Balance'] - beng_Account['Stocks']*beng_ticker # Total profit/loss
        msg_data4=("This operation's profit: %s(RMB)\tTotal profit: %.2f(RMB) %.2f\r\n"%(str(gains),income,roi))
        #################################################
```

Note that the comments and some function names have been kept in Chinese as they seem to be part of a local development environment or were originally written that way.