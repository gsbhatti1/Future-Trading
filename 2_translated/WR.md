```python
'''
backtest
start: 2021-03-19 05:00:00
end: 2021-03-21 00:00:00
period: 15m
basePeriod: 15m
exchanges: [{"eid":"Futures_HuobiDM","currency":"BTC_USD"},{"eid":"Futures_HuobiDM","currency":"ETH_USD","stocks":300},{"eid":"Futures_HuobiDM","currency":"EOS_USD","stocks":5000}]
args: [["openConMode",null]]
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
import talib
import math
import urllib.request

ChartCfg = {
    '__isStock': True,
    'title': {
        'text': 'WR'
    },
    'yAxis': [{
        'title': {'text': 'WR'},
        'style': {'color': '#4572A7'},
        'opposite': False #右边轴
    }],
    'series': [{
        'type': 'line',
        'id': 'wr',
        'name': 'wr',
        'data': []
    }]
}

def MyLog(str1, ktime, price=''):
    if _G('str') != str1 or _G('ktime') != ktime and not (_G('str2') == str1 and _G('ktime2') == ktime):
        _G('str2', _G('str'))
        _G('ktime2', _G('ktime'))

        _G('str', str1)
        _G('ktime', ktime)
        Log(str1 + str(price)) 


def moveStocks(_moveStocks):
    global todayProfit
    if exchanges[0].GetName().find('Binance') >= 0: # Futures_Binance 只有币本位有交割且共用资金 2-U本位向现货   4-币本位向现货 返回tranId
        if exchanges[0].GetCurrency().find('USDT') >= 0:
            movecurrency = 'USDT'
            mtype = 2
        else: # 币本位
            movecurrency = 'BTC'
            mtype = 4
        timestamp = int(time.time() * 1000)
        params = "type=" + str(mtype) + "&asset=" + movecurrency + "&amount=" + str(_moveStocks) + "&timestamp=" + str(timestamp)
        exchanges[0].SetBase('https://api.binance.com')
        moveid = exchange.IO("api", "POST", "/sapi/v1/futures/transfer", params)
        exchanges[0].SetBase('https://fapi.binance.com')
        if moveid is not None:
            Log('资金转出成功', moveid)
            _G('moveStocks', _G('moveStocks') + _moveStocks)
            todayProfit["initStocks"] = todayProfit["initStocks"] - _moveStocks
            _G('todayProfit', todayProfit)
        else:
            Log('资金转出失败')
    else:
        Log('暂不支持该交易所转移')

def cancelOD(i):
    orders = _C(exchanges[i].GetOrders)
    for order in orders:
        exchanges[i].CancelOrder(order.Id)
        time.sleep(0.1)

def coverAll(i):
    position = _C(exchanges[i].GetPosition)
    cancelOD(i)
    time.sleep(0.3)
    for j in range(len(position)):
        pamount = position[j]["Amount"] #-position[0]["FrozenAmount"]
        if position[j]["Type"] == 0:     # 持多单
            Deal(-1, pamount, "closebuy", exchanges[i].GetCurrency() + '手动市价清仓', i)
        elif position[j]["Type"] == 1:     # 持空单
            Deal(-1, pamount, "closesell", exchanges[i].GetCurrency() + '手动市价清仓', i)

def getOpenPrice(position):
    if hasattr(position[0], 'Info') and hasattr(position[0].Info, 'cost_open'):  # huobi
        return position[0].Info.cost_open
    elif hasattr(position[0], 'Info') and hasattr(position[0].Info, 'avg_cost'):  # ok
        return position[0].Info.avg_cost
    elif hasattr(position[0], 'Info') and hasattr(position[0].Info, 'entryPrice'):  # binance
        return position[0].Info.entryPrice
    else:
        return position[0]["Price"] 

def UpdateAccout():
    accout = _C(exchanges[0].GetAccount)
    acc1 = accout.FrozenBalance    # 其它币的冻结余额 是否共用?
    acc2 = accout.Balance
    
    _G("ableAccount", acc2)  # 当前可用U
    _G("allAccount", acc1 + acc2 + GetMargin())  # 没计算浮盈
    if acc2 < 1:
        Log("账户保证金余额不足")
        time.sleep(8)

def GetMargin():
    allMargin = 0
    for i in range(len(exchanges)):
        allMargin += _G("margin")[i]
    return round(allMargin, 2)


def GetHighest(records, i, period):
    high = 0
    for j in range(i - period + 1, i + 1):
        if records[j].High > high:
            high = records[j].High
    return high

def GetLowest(records, i, period):
    low = 1000000
    for j in range(i - period + 1, i + 1):
        if records[j].Low < low:
            low = records[j].Low
    return low
    
def SetType(type):
    if type == 0:
        _G("contractType", "swap")
    elif type == 1:
        _G("contractType", "this_week")
    elif type == 2:
        _G("contractType", "next_week")
    elif type == 3:
        _G("contractType", "quarter")
    elif type == 4:
        _G("contractType", "next_quarter")
        
def Deal(price, num, btype, beizhu='', i=0):
    time.sleep(0.05)
    #if beizhu != '':
    #    Log(beizhu)
    exchanges[i].SetDirection(btype)
    if btype == "closebuy" or btype == "sell":
        exchanges[i].Sell(price, num, beizhu)
        #Log('开空', price)
    else:
        exchanges[i].Buy(price, num, beizhu)
        #Log('开多', price)


def myProfit():
    LogProfit(_G("allAccount") - _G("initStocks"))
```

Note: I maintained the code blocks and formatting as provided, translated only the human-readable text.