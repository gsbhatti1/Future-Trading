> Name

R-Breaker Trading Strategy

> Author

Tai Ji

> Strategy Description

R-Breaker Trading Strategy


> Source (python)

``` python
#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#R-Breaker Trading Strategy
#Strategy Provider @FJK   QQ:171938416
#Improved by @Tai Ji  QQ:7650371

def my_buy(): # Opening Position
    try:
        global buy_price, buy_qty
        initAccount = ext.GetAccount()  # Trading template export function to get account status and save the initial account state before strategy run
        opAmount = 1
        PositionRatio = 1
        # Check if there are coins first; if not, perform a purchase
        if int(initAccount.Stocks) > 0:
            if buy_price < 1:
                buy_price = _C(exchange.GetTicker).Last
                buy_qty = initAccount.Stocks
            # Log('Opening position info 1: Still have %s coins, clearing first.' % (initAccount.Stocks), '--Opening Position Details:', initAccount)
            return 1
        if int(initAccount.Stocks) < 1:
            if int(str(initAccount.Stocks).replace('0.', '')) >= 3:
                if buy_price < 1:
                    buy_price = _C(exchange.GetTicker).Last
                    buy_qty = initAccount.Stocks
                # Log('Opening position info 2: Still have %s coins, clearing first.' % (initAccount.Stocks), '--Opening Position Details:', initAccount)
                return 1

        opAmount = _N(initAccount.Balance * PositionRatio, 3)  # Calculate the amount to buy
        Log("Opening position without coins, proceed with opening purchase of %s RMB" % str(opAmount))  # Generate log information

        Dict = ext.Buy(opAmount)  # Execute the buy order
        if Dict:  # Confirm that the position was opened successfully
            buy_price = Dict['price']  # Buy price   #{'price': 4046.446, 'amount': 1.5}
            buy_qty = Dict['amount']  # Buy quantity
            # LogProfit(_N(gains,4),'Opening position info: Initial balance:',initAccount.Balance,'--Coins:',initAccount.Stocks,'--Opening Position Details:',Dict)
            print_log(1, initAccount)
            return 1
        return 0

    except Exception as ex:
        Log('except Exception my_buy:', ex)
        return 0


import time
import datetime
def Caltime(date1, date2):   # Calculate running days
    try:
        date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
        date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
        return date2 - date1
    except Exception as ex:
        Log('except Exception Caltime:', ex)
        return "except Exception"

start_timexx = time.localtime(time.time())  # time.clock()
start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_timexx)
buy_price = 0  # Buy price
buy_qty = 0  # Buy quantity
gains = 0  # Profit

beng_Account = ext.GetAccount()  # Initialize information
beng_ticker = _C(exchange.GetTicker).Last  # Ticker  Market Price   Last Trade Price
beng_Balance = (beng_Account.Stocks * beng_ticker) + beng_Account.Balance  # Initial account balance

def print_log(k_p, data=""):  # Output function
    try:
        name = ""
        if k_p:
            name = "Opening Position"
        else:
            name = "Closing Position"
        global beng_Account, beng_ticker, beng_Balance
        global gains
        end_Account = ext.GetAccount()  # Current account information
        end_ticker = _C(exchange.GetTicker).Last  # Ticker  Market Price   Last Trade Price
        #################################################
        date1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg_data0 = ("This run started at: %s, Running for: %s\r\n" % (start_time, Caltime(start_time, date1)))
        #################################################
        msg_data1 = ("Initial status: %s \nCurrent status: %s \r\n" % (beng_Account, end_Account))
        #################################################
        end_Balance = (end_Account.Stocks * end_ticker) + end_Account.Balance  # Current balance on the account
        msg_data2 = ("Initial balance: %s, Now balance: %s, Profit/Loss: %s \r\n" % (str(beng_Balance), str(end_Balance), str(end_Balance - beng_Balance)))
        #################################################
        total = end_Account.Balance + end_Account.Stocks * _C(exchange.GetTicker).Last  # Total account value
        roi = ((total / beng_Balance) - 1) * 100
        msg_data3 = ("Current status: %s--Balance: %s--Coins: %s--Total value approx.: %.2f \r\n" % (str(name), str(end_Account.Balance), str(end_Account.Stocks), roi))
        #################################################
        income = total - beng_Account['Balance'] - beng_Account['Stocks'] * beng_ticker  # Total profit/loss
        msg_data4 = ("This run's profit/loss: %s (RMB)\tTotal Profit/Loss: %.2f (RMB) \r\n" % (str(gains), income, roi))
        #################################################
        # Calculation of profits and losses
        # Floating profit: Calculated as (current coins - initial coins) x current price + (current balance - initial balance)
        diff_stocks = end_Account.Stocks - beng_Account.Stocks  # Difference in coins
        diff_balance = end_Account.Balance - beng_Account.Balance  # Difference in balance
        new_end_balance = diff_stocks * end_ticker + diff_balance  # Realized profit/loss   # Current profit
        # Calculation of profits and losses on the books: (current coins x current price + current balance) - (initial coins x initial price + initial balance)
        new_end_balance2 = (end_Account.Stocks * end_ticker + end_Account.Balance) - (beng_Account.Stocks * beng_ticker + beng_Account.Balance)
        msg_data5 = ("Floating profit: %s (RMB)\nAccount Profit/Loss: %s (RMB)\n" % (_N(new_end_balance, 3), _N(new_end_balance2, 3)))
        #################################################
        LogStatus("Initial investment 2016/9/24 Invested 0.2 coins = 800 RMB equivalent\n",
                  msg_data0 + msg_data1 + msg_data2 + msg_data3 + msg_data4 + msg_data5,
                  "Updated at: %s" % (date1),
                  "%s" % (data)
                  )
        #################################################
        #################################################
        #################################################
    except Exception as ex:
        Log('except Exception print_log:', ex)

def my_sell(): # Closing Position
    try:
        global buy_price, buy_qty, gains, ExitPeriod
        ExitPeriod = 0
        nowAccount = ext.GetAccount()  # Trading template export function to get account information
        if nowAccount.Stocks <= 0.002:  # Ensure that the trade volume is met
            # Log('Does not meet minimum trading volume:',nowAccount.Stocks)
            return 1

        # history_Last = _N(Volume_averages(Ticker_list), 2)    # Historical average price
        # cur_last = _N(_C(exchange.GetTicker).Last, 2)

        # if _N(_C(exchange.GetTicker).Last, 2) > buy_price + ExitPeriod :   # Current price must be greater than the opening price
        if True:
            #if _N(_C(exchange.GetTicker).Last, 2) > buy_price + ExitPeriod and history_Last - cur_last > 0 and history_Last - cur_last < 2:   # Current price must be greater than the opening price
            # Log('Historical difference:',history_Last - cur_last)
```