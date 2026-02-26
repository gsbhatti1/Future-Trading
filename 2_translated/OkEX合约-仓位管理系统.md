> Name

OkEX Contract - Position Management System

> Author

FawkesPan



> Source (python)

``` python
import time
import math
import threading
import decimal
from uuid import uuid4 as _uuid

def genUUID():
    return str(_uuid())

class PositionManager:

    def __init__(self, exchange, symbol, contract, getDepth, tickSize=0.01):
        self.okex = exchange
        self.symbol = symbol
        self.contract = contract
        self.tickSize = tickSize
        self.isFMZ = False
        if 'Asks' in getDepth().keys():
            self.isFMZ = True
        self.okexGetDepth = getDepth
        self.orderLock = threading.Lock()
        self.orderLocks = {}
        self.orders = {}
        self.cancels = []
        self.completeds = []
        self.init()

    def init(self):
        self.okex.IO("currency", self.symbol.upper())
        self.okex.SetContractType(self.contract)
        self.order_logs = {
            'buySent': 0,
            'buyCanceled': 0,
            'sellSent': 0,
            'sellCanceled': 0
        }

    def toNearest(self, num):
        tickDec = decimal.Decimal(str(self.tickSize))
        return float((decimal.Decimal(round(num / self.tickSize, 0)) * tickDec))

    def getDepth(self):
        depth = self.okexGetDepth()
        if self.isFMZ:
            depth['asks'] = [[x['Price'], x['Amount']] for x in depth['Asks']]
            depth['bids'] = [[x['Price'], x['Amount']] for x in depth['Bids']]
        return depth

    def getOrderLogs(self):
        return self.order_logs

    def getBestPrices(self):
        bestPrices = {}
        depth = self.getDepth()
        ask, bid = depth['asks'][0][0], depth['bids'][0][0]
        spread = ask - bid
        if spread <= self.tickSize*2:
            bestPrices['ask'] = ask
            bestPrices['bid'] = bid
        elif spread <= self.tickSize*6:
            bestPrices['ask'] = ask-self.tickSize
            bestPrices['bid'] = bid+self.tickSize
        elif spread >= self.tickSize*20:
            bestPrices['ask'] = ask-self.tickSize*5
            bestPrices['bid'] = bid+self.tickSize*5
        else:
            midPrice = self.toNearest((ask+bid)/2)
            bestPrices['ask'] = midPrice+self.tickSize*2
            bestPrices['bid'] = midPrice-self.tickSize*2
        return {
            'ask': self.toNearest(bestPrices['ask']),
            'bid': self.toNearest(bestPrices['bid'])
        }

    def getPositions(self, noRetry=False, maxRetries=10):
        if noRetry:
            return self.okex.GetPosition()
        attempts = 0
        while True:
            time.sleep(0.4)
            positions = self.okex.GetPosition()
            attempts+=1
            if len(positions) != 0:
                return positions
            if attempts == maxRetries:
                return False

    def havePosition(self, type=None, noRetry=True, maxRetries=10):
        positions = self.getPositions(noRetry=True)
        if not positions:
            positions = []
        if type == None:
            pass
        elif type == 'buy':
            key = 'buy_amount'
        elif type == 'sell':
            key = 'sell_amount'
        for position in positions:
            if type is not None:
                if position['Info'][key] != 0:
                    return positions
            else:
                return positions
        if noRetry:
            return False
        attempts = 0
        while True:
            time.sleep(0.4)
            positions = self.getPositions(noRetry=True)
            if not positions:
                positions = []
            attempts+=1
            for position in positions:
                if type is not None:
                    if position['Info'][key] != 0:
                        return positions
                else:
                    return positions
            if attempts == maxRetries:
                return False

    def orderDone(self, orderID):
        orders = self.okex.GetOrders()
        for order in orders:
            if order['Info']['order_id'] == orderID:
                return order['Info']['price'], order['Info']['amount']-order['Info']['deal_amount']
        return True

    def getOrder(self, uuid):
        try:
            self.orders[uuid]
        except KeyError:
            Log('不存在订单 %s' % uuid)
            return 0
        return self.orders[uuid]

    def getOrderInfo(self, uuid):
        return self.okex.GetOrder(self.getOrder(uuid))

    def awaitOrder(self, uuid, timeout=None):
        start = time.time()
        try:
            self.orderLocks[uuid]
        except KeyError:
            return False
        while True:
            if self.orderLocks[uuid].acquire(False):
                del self.orderLocks[uuid]
                return self.getOrder(uuid)
            else:
                if timeout is not None:
                    if time.time()-timeout>start:
                        Log('等待订单成交已超时.')
                        return
            time.sleep(0.001)

    def isDone(self, uuid):
        if uuid in self.completeds:
            return True
        return False

    def cancel(self, uuid):
        self.cancels.append(uuid)
        _cancel = self.okex.CancelOrder(self.getOrder(uuid))
        self.orderLocks[uuid].acquire()
        self.orderLocks[uuid].release()
        if _cancel:
            Log('%s %s 已取消.' % (uuid, str(self.getOrder(uuid))))
            return True
        Log('%s %s 取消失败.' % (uuid, str(self.getOrder(uuid))), str(self.okex.GetRawJSON()))
        return False

    def trade(self, type, price, amount, matchPrice=False, noRetry=False, uuid=None):
        if type == 'buy' or type == 'closesell':
            _trader = self.okex.Buy
            _side = 'buy'
            __side = 'bid'
        else:
            _trader = self.okex.Sell
            _side = 'sell'
            __side = 'ask'
        def trader(price, amount):
            self.orderLock.acquire()
            self.o
```