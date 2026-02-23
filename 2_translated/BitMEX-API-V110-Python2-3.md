<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

BitMEX-Advanced API Features-V110-Futures Batch Order Editing Iceberg Orders One-Click Cancellation Timed Cancellation-Python2-3

> Author

FawkesPan

> Strategy Description

# BitMEX Advanced API Features (FMZ.com)

### Initialization
This library integrates some advanced BitMEX API features and needs to be initialized before use.
```
# Single Exchange
BitMEX = ext.BitMEXPlus(exchange)    # Create a new interface object
# Multiple Exchanges
BitMEX = ext.BitMEXPlus(exchanges[0]) # exchanges[depends on which slot your exchange was added to]
```

### Order Operations
#### Batch Orders
##### BulkAdd() Add new orders to the local order list
```
side price amount are required parameters
symbol defaults to the default trading pair if not provided
displayQty is used for iceberg order feature, sets the displayed portion size of the order, setting to 0 completely hides it
orderType execInst optional parameters, please see comments within source code
BitMEX.BulkAdd(side=string, price=float, amount=integer, symbol=string, displayQty=integer, ordType='Limit', clOrdID='', execInst='') 
```
##### BulkClear() Clear unsubmitted local orders
```
symbol specifies which trading pair orders to clear; if unspecified, clears all orders
notify whether to show logs, default is to show
BitMEX.BulkClear(symbol=string, notify=True)
```
##### BulkPost() Submit unsubmitted local orders
```
symbol if specified, only submits orders for the specified trading pair; if unspecified, submits all orders
BitMEX.BulkPost(symbol=string)
```
##### BulkOrders() View all unsubmitted local orders
```
BitMEX.BulkOrders()
```
#### Cancel Orders
##### CancelAllOrders() Cancel currently incomplete orders
```
symbol if specified, only cancels orders for the specified trading pair; if unspecified, cancels all orders
filter custom order filtering, only cancels orders meeting conditions e.g., filter={'side': 'Buy'} cancels all buy orders
BitMEX.CancelAllOrders(symbol=string, filter=dict)
```
##### CancelAllAfter() Cancel all incomplete orders after a certain time
Requesting again can reset the counter
```
timeout specifies how many milliseconds after which to cancel orders; filling 0 deletes the counter
BitMEX.CancelAllAfter(timeout=integer)
```
#### Edit Orders
##### Amend() Modify an order
```
symbol specifies the trading pair; if unspecified, uses the default trading pair
orderID clOrdID Order ID and user-defined order ID; at least one must be specified, if both are filled only orderID is used
price amount New price and new quantity for the order; at least one modification required, both can be modified simultaneously
BitMEX.Amend(symbol=string, orderID=string, clOrdID=string, price=float, amount=integer)
```
#### Batch Edit Orders
##### AmendAdd() Add an order needing modification to the local pending modification order list
```
symbol specifies the trading pair; if unspecified, uses the default trading pair
orderID clOrdID Order ID and user-defined order ID; at least one must be specified, if both are filled only orderID is used
price amount New price and new quantity for the order; at least one modification required, both can be modified simultaneously
BitMEX.AmendAdd(symbol=string, orderID=string, clOrdID=string, price=float, amount=integer)
```
##### AmendClear() Clear unsubmitted pending modification orders locally
```
symbol if specified, clears orders for the specified trading pair; if unspecified, clears all orders
notify whether to show logs, default is to show
BitMEX.AmendClear(symbol=string, notify=True)
```
##### AmendPost() Submit unsubmitted pending modification orders
```
symbol if specified, submits modification requests for the specified trading pair orders; if unspecified, submits modification requests for the default trading pair orders
BitMEX.AmendPost(symbol=string)
```
##### AmendOrders() View all unsubmitted orders
```
BitMEX.AmendOrders()
```

### Contact Me
Email i@fawkex.me
Telegram [FawkesPan](https://telegram.me/FawkesPan)

Custom strategy development accepted

### About This Library
[BitMEX API Documentation](https://www.bitmex.com/app/apiOverview)

[Using GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html)

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|LANG|ZH|Language / 语言|


> Source (python)

``` python


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
    'GREET' : '[BitMEX Interface Initialized] Contract: %s. %s',
    'INITF' : 'Incorrect exchange used, current exchange: %s',
    'PARAMERR' : '***Wrong parameter passed Check your code*** %s',
    'NEWORDER' : '[Add Order] Contract: %s Side: %s Price: %.8f Quantity: %d Contracts. %s',
    'MODORDER' : '[Modify Order] orderID/clOrdID: %s New Price: %.8f New Quantity: %d. %s',
    'MODORDERP' : '[Modify Order] orderID/clOrdID: %s New Price: %.8f. %s',
    'MODORDERA' : '[Modify Order] orderID/clOrdID: %s New Quantity: %d. %s',
    'ORDCOUNT' : '[Batch Orders Sent] Total: %d entries. %s',
    'THISBATCH' : '[Info] Processing Contract: %s Count: %d. %s',
    'CLEARALL' : '[Info] Cleared all local orders. %s',
    'CLEAR' : '[Info] Cleared all %s local orders. %s',
    'CA' : '[Order Scheduled Cancellation] All orders will be canceled after %d milliseconds. %s'
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
            Log(QUOTES[LANG]['INITF'] % (name))
            
    def Log(self, *args):
        if self.silent:
            return 
        Log(*args)

    def BulkAdd(self, side=None, price=None, amount=None, symbol=None, ordType='Limit', displayQty=None, clOrdID=None, execInst=None):
        if type is None or price is None or amount is None:
            Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
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
        # MarketWithLeftOverAsLimit: A market order that, after eating through the order book as far as permitted by available margin, will become a limit order. The difference between this type and Market only affects the behavior in thin books. Upon reaching the deepest possible price, if there is quantity left over, a Market order will cancel the remaining quantity. MarketWithLeftOverAsLimit will keep the remaining quantity in the books as a Limit.
        # Stop: A Stop Market order. Specify an orderQty and stopPx. When the stopPx is reached, the order will be entered into the book.
        ## On sell orders, the order will trigger if the triggering price is lower than the stopPx. On buys, higher.
        ## Note: Stop orders do not consume margin until triggered. Be sure that the required margin is available in your account so that it may trigger fully.
        ## Close Stops don't require an orderQty. See Execution Instructions below.
        # StopLimit: Like a Stop Market, but enters a Limit order instead of a Market order. Specify an orderQty, stopPx, and price.
        # MarketIfTouched: Similar to a Stop, but triggers are done in the opposite direction. Useful for Take Profit orders.
        # LimitIfTouched: As above; use for Take Profit Limit orders.
        order['ordType'] = ordType
        # If you want to keep track of order IDs yourself, set a unique clOrdID per order. This clOrdID will come back as a property on the order and any related executions (including on the WebSocket), and can be used to get or cancel the order. Max length is 36 characters.
        if clOrdID is not None:
            order['clOrdID'] = clOrdID
        # The following execInsts are supported. If using multiple, separate with a comma (e.g. LastPrice,Close).
        # ParticipateDoNotInitiate, MarkPrice, LastPrice, IndexPrice, ReduceOnly, Close
        # ParticipateDoNotInitiate: Also known as a Post-Only order. If this order would have executed on placement, it will cancel instead.
        # MarkPrice, LastPrice, IndexPrice: Used by stop and if-touched orders to determine the triggering price. Use only one. By default, 'MarkPrice' is used. Also used for Pegged orders to define the value of 'LastPeg'.
        # ReduceOnly: A 'ReduceOnly' order can only reduce your position, not increase it. If you have a 'ReduceOnly' limit order that rests in the order book while the position is reduced by other orders, then its order quantity will be amended down or canceled. If there are multiple 'ReduceOnly' orders the least aggressive will be amended first.
        # Close: 'Close' implies 'ReduceOnly'. A 'Close' order will cancel other active limit orders with the same side and symbol if the open quantity exceeds the current position. This is useful for stops: by canceling these orders, a 'Close' Stop is ensured to have the margin required to execute, and can only execute up to the full size of your position. If orderQty is not specified, a 'Close' order has an orderQty equal to your current position's size.
        ## Note that a Close order without an orderQty requires a side, so that BitMEX knows if it should trigger above or below the stopPx.
        if execInst is not None:
            order['execInst'] = execInst
            if 'Close' in execInst:
                del order['orderQty']
        # Optional quantity to display in the book. Use 0 for a fully hidden order. (Iceberg Order)
        if displayQty is not None:
            order['displayQty'] = displayQty

        self.bulks.append(order)

        self.Log(QUOTES[LANG]['NEWORDER'] % (symbol.upper(),side.upper(),price,amount,cl))

        return True

    def BulkClear(self, symbol=None, notify=True):
        ret = []
        if symbol is None:
            ret = self.bulks
            self.bulks = []
            if notify:
                self.Log(QUOTES[LANG]['CLEARALL'] % (COLORS['RED']))
        else:
            new = []
            for i in self.bulks:
                if i['symbol'] != symbol:
                    new.append(i)
                else:
                    ret.append(i)
            self.bulks = new
            self.Log(QUOTES[LANG]['CLEAR'] % (symbol.encode().upper(), COLORS['RED']))

        return ret

    def BulkPost(self, symbol=None):
        orders = []
        if symbol is None:
            orders = self.BulkClear(notify=False)
        else:
            orders = self.BulkClear(symbol=symbol, notify=False)
            
        if len(orders) == 0:
            return True

        ret = self.IO("api", "POST", "/api/v1/order/bulk", 'orders=%s' % json.dumps(orders))

        self.Log(QUOTES[LANG]['ORDCOUNT'] % (len(orders),COLORS['LAPIS']))
        return ret

    def BulkOrders(self):
        return self.bulks

    def Amend(self, symbol=None, orderID=None, clOrdID=None, price=None, amount=None):
        if symbol is None:
            symbol = self.symbol

        order = {}
        order['symbol'] = symbol
        if orderID is None:
            if clOrdID is None:
                Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
                return False
            else:
                order['clOrdID'] = clOrdID
        else:
            order['orderID'] = orderID

        if price is not None:
            order['price'] = price
        if amount is not None:
            order['orderQty'] = amount

        if price is None and amount is None:
            Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
            return False

        ret = self.IO("api", "PUT", "/api/v1/order/bulk", 'orders=%s' % json.dumps([order]))
        if ret == False:
            return False

        try:
            id = order['orderID']
        except:
            id = order['clOrdID']

        if price is None:
            self.Log(QUOTES[LANG]['MODORDERA'] % (id, amount, COLORS['LAPIS']))
            return ret
        elif amount is None:
            self.Log(QUOTES[LANG]['MODORDERP'] % (id, price, COLORS['LAPIS']))
            return ret
        else:
            self.Log(QUOTES[LANG]['MODORDER'] % (id, price, amount, COLORS['LAPIS']))
            return ret

    def AmendAdd(self, symbol=None, orderID=None, clOrdID=None, price=None, amount=None):
        if symbol is None:
            symbol = self.symbol

        order = {}
        order['symbol'] = symbol
        if orderID is None:
            if clOrdID is None:
                Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
                return False
            else:
                order['clOrdID'] = clOrdID
        else:
            order['orderID'] = orderID

        if price is not None:
            order['price'] = price
        if amount is not None:
            order['orderQty'] = amount

        if price is None and amount is None:
            Log(QUOTES[LANG]['PARAMERR'] % (COLORS['RED']))
            return False

        self.amends.append(order)

        try:
            id = order['orderID']
        except:
            id = order['clOrdID']

        if price is None:
            self.Log(QUOTES[LANG]['MODORDERA'] % (id, amount, COLORS['LAPIS']))
            return True
        elif amount is None:
            self.Log(QUOTES[LANG]['MODORDERP'] % (id, price, COLORS['LAPIS']))
            return True
        else:
            self.Log(QUOTES[LANG]['MODORDER'] % (id, price, amount, COLORS['LAPIS']))
            return True

    def AmendClear(self, symbol=None, notify=True):
        ret = []
        if symbol is None:
            ret = self.amends
            self.amends = []
            if notify:
                self.Log(QUOTES[LANG]['CLEARALL'] % (COLORS['RED']))
        else:
            new = []
            for i in self.amends:
                if i['symbol'] != symbol:
                    new.append(i)
                else:
                    ret.append(i)
            self.self.amends = new
            self.Log(QUOTES[LANG]['CLEAR'] % (symbol.encode().upper(), COLORS['RED']))

        return ret

    def AmendPost(self, symbol=None):
        if symbol is None:
            symbol = self.symbol
        orders = self.AmendClear(symbol=symbol, notify=False)
        if len(orders) == 0:
            return True
        param = "orders=" + json.dumps(orders)
        self.Log(QUOTES[LANG]['ORDCOUNT'] % (len(orders),COLORS['LAPIS']))
        return self.IO("api", "PUT", "/api/v1/order/bulk", param)

    def AmendOrders(self):
        return self.amends

    def CancelAllOrders(self, symbol=None, filters=None):
        param = ''
        if symbol is not None:
            param = param + 'symbol=' + symbol
        if filters is not None:
            param = param + 'filters=' + json.dumps(filters)
        return self.IO("api","DELETE","/api/v1/order/all", param)

    def CancelAllAfter(self, timeout=0, notify=True):
        param = 'timeout=' + str(timeout)
        if notify:
            self.Log(QUOTES[LANG]['CA'] % (timeout,COLORS['LAPIS']))
        return self.IO("api","POST","/api/v1/order/cancelAllAfter", param)

    def GetInstrument(self, symbol='XBTUSD'):
        try:
            import requests
        except ModuleNotFoundError:
            Log('Install requests via pip to use GetInstrument() function.')
            return {}
        return requests.get('https://www.bitmex.com/api/v1/instrument?symbol=%s&count=1&reverse=false' % symbol).json()[0]

ext.BitMEXPlus = BitMEX # Export BitMEX Class, main strategy can call via BitMEXPlus = ext.BitMEXPlus(exchange)
ext.toNearest = toNearest

# Module functionality test
def main():
    LogReset()
    Log(exchange.GetAccount())
    BitMEXPlus = ext.BitMEXPlus(exchange)
    exchange.SetContractType(exchange.GetCurrency())
    base_price = exchange.GetTicker()['Last']
    _toNearest = ext.toNearest
    BitMEXPlus.BulkAdd('sell', _toNearest(base_price*1.4, 0.5), 30)
    BitMEXPlus.BulkAdd('buy', _toNearest(base_price*0.7, 0.5), 30)
    Log(BitMEXPlus.BulkOrders())
    Log(BitMEXPlus.BulkPost())
    Log(exchange.GetOrders())
    Log(BitMEXPlus.CancelAllAfter(5000))
    Sleep(8000)
    Log(exchange.GetOrders())
    Log(BitMEXPlus.BulkOrders())

```

> Detail

https://www.fmz.com/strategy/114148

> Last Modified

2020-05-19 22:57:04