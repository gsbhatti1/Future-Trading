```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding: utf-8
#
# BitMEX Advanced API Interface for FMZ.com.
#
# Copyright 2018 FawkesPan
# Contact : i@fawkex.me / Telegram@FawkesPan
#
# GNU General Public License v3.0
#

import json
import math
import decimal

def toNearest(num, tickSize):
    tickDec = decimal.Decimal(str(tickSize))
    return float((decimal.Decimal(round(num / tickSize, 0)) * tickDec))

QUOTES = {}
QUOTES['ZH'] = {
    'GREET' : '[BitMEX 接口已初始化]  合约: %s. %s',
    'INITF' : '使用的交易所不正确，当前交易所: %s',
    'PARAMERR' : '***传的参数不对 检查你的代码*** %s',
    'NEWORDER' : '[添加订单]  合约: %s 方向: %s 价格: %.8f 数量: %d 张. %s',
    'MODORDER' : '[修改订单]  orderID/clOrdID: %s 新价格: %.8f 新数量: %d. %s',
    'MODORDERP' : '[修改订单]  orderID/clOrdID: %s 新价格: %.8f. %s',
    'MODORDERA' : '[修改订单]  orderID/clOrdID: %s 新数量: %d. %s',
    'ORDCOUNT' : '[本次批量发送订单]  总计: %d 条. %s',
    'THISBATCH' : '[信息]  正在处理 合约: %s 条数: %d. %s',
    'CLEARALL' : '[信息]  已清除所有本地订单. %s',
    'CLEAR' : '[信息]  已清除所有 %s 本地订单. %s',
    'CA' : '[订单计划取消]  所有订单都将在 %d 毫秒 后取消. %s'
}

COLORS = {
    'DEEPBLUE' : '#1F618D',
    'BLUE' : '#0000FF',
    'LIGHTBLUE' : '#5DADE2',
    'DEEPGREEN' : '#27AE60',
    'GREEN' : '#00FF00',
    'LIGHTGREEN' : '#58D68D',
    'LAPIS' : '#26619C',
    'DEEPRED' : '#CB4335',
    'RED' : '#FF0000',
    'LIGHTRED' : '#EC7063'
}


class BitMEX:

    def __init__(self, exchange, silent=False):
        self.silent = silent
        exchange.GetCurrency()
        if isinstance(exchange.GetCurrency(), bytes):
            self.symbol = str(exchange.GetCurrency(), "utf-8").lower()
            name = str(exchange.GetName(), "utf-8")
        else:
            self.symbol = exchange.GetCurrency()
            name = exchange.GetName()
        self.IO = exchange.IO
        self.bulks = []
        self.amends = []
        if 'BitMEX' in str(name):
            self.Log(QUOTES[LANG]['GREET'] % (self.symbol.upper(),COLORS['LAPIS']))
        else:
            self.Log(QUOTES[LANG]['INITF'] % (name))
            
    def Log(self, *args):
        if self.silent:
            return 
        self.IO.Log(*args)

    def BulkAdd(self, side=None, price=None, amount=None, symbol=None, ordType='Limit', displayQty=None, clOrdID=None, execInst=None):
        if side is None or price is None or amount is None:
            self.Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
            return False
        side = side.lower()
        if 'sell' in side:
            side = 'Sell'
            cl = COLORS['DEEPRED']
        else:
            side = 'Buy'
            cl = COLORS['DEEPGREEN']
        if symbol is None:
            symbol = self.symbol

        # Order structure
        order = {}
        order['symbol'] = symbol.upper()            # Symbol
        order['price'] = price                      # Price
        order['side'] = side                        # Buy/Sell
        order['orderQty'] = int(amount)             # Amount

        # Valid order types
        # Market, Limit, Stop, StopLimit, MarketIfTouched, LimitIfTouched, MarketWithLeftOverAsLimit, Pegged
        # Limit: The default order type. Specify an orderQty and price.
        # Market: A traditional Market order. A Market order will execute until filled or your bankruptcy price is reached, at which point it will cancel.
        # MarketWithLeftOverAsLimit: A market order that, after eating through the order book as far as permitted by available margin, will become a limit order. The
```