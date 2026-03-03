``` python
import time

class Error_noSupport(BaseException):
    def __init__(self):
        Log("Only supports OKCoin futures! #FF0000")

class Error_AtBeginHasPosition(BaseException):
    def __init__(self):
        Log("There is a futures position at the start! #FF0000")

ChartCfg = {
    '__isStock': True,
    'title': {
        'text': 'Dual Thrust Upper and Lower Band Chart'
    },
    'yAxis': {
        'plotLines': [{
            'value': 0,
            'color': 'red',
            'width': 2,
            'label': {
                'text': 'Upper Band',
                'align': 'center'
            },
        }, {
            'value': 0,
            'color': 'green',
            'width': 2,
            'label': {
                'text': 'Lower Band',
                'align': 'center'
            },
        }]
    },
    'series': [{
        'type': 'candlestick',
        'name': 'Current Period',
        'id': 'primary',
        'data': []
    }, {
        'type': 'flags',
        'onSeries': 'primary',
        'data': []
    }]
}

STATE_IDLE = 0
STATE_LONG = 1
STATE_SHORT = 2
State = STATE_IDLE

LastBarTime = 0
UpTrack = 0
BottomTrack = 0
chart = None
InitAccount = None
LastAccount = None
Counter = {
    'w': 0,
    'l': 0
}

def GetPosition(posType):  # if the positions has no this posType ,will return [] ,Another case is return a dict of object
    positions = exchange.GetPosition()
    return [{'Price': position['Price'], 'Amount': position['Amount']} for position in positions if position['Type'] == posType]

def CancelPendingOrders():
    while True:
        orders = exchange.GetOrders()
        [exchange.CancelOrder(order['Id']) for order in orders if not Sleep(500)]
        if len(orders) == 0:
            break 

def Trade(currentState, nextState):
    global InitAccount, LastAccount, OpenPrice, ClosePrice
    ticker = _C(exchange.GetTicker)
    slidePrice = 1
    pfn = exchange.Buy if nextState == STATE_LONG else exchange.Sell 
    if currentState != STATE_IDLE:
        Log(_C(exchange.GetPosition)) # ceshi 
        exchange.SetDirection("closebuy" if currentState == STATE_LONG else "closesell")
        while True:
            ID = pfn( (ticker['Last'] - slidePrice) if currentState == STATE_LONG else (ticker['Last'] + slidePrice), AmountOP) # xiugai 限价单
            # ID = pfn(-1, AmountOP) # xiugai 市价单
            # ID = pfn(AmountOP) # xiugai 市价单
            Sleep(Interval)
            Log(exchange.GetOrder(ID)) # xiugai
            ClosePrice = (exchange.GetOrder(ID))['AvgPrice'] # 
            CancelPendingOrders()
            if len(GetPosition(PD_LONG if currentState == STATE_LONG else PD_SHORT)) == 0:
                break 
        account = exchange.GetAccount()
        if account['Stocks'] > LastAccount['Stocks']:
            Counter['w'] += 1
        else:
            Counter['l'] += 1
        # Log("ceshi account:",account,InitAccount) #ceshi
        Log(account) # xiugai
        LogProfit((account['Stocks'] - InitAccount['Stocks']),"Return Rate:", ((account['Stocks'] - InitAccount['Stocks']) * 100 / InitAccount['Stocks']),'%')
        Cal(OpenPrice,ClosePrice)
        LastAccount = account 
    
    exchange.SetDirection("buy" if nextState == STATE_LONG else "sell") 
    Log(_C(exchange.GetAccount))
    while True:
        ID = pfn( (ticker['Last'] + slidePrice) if nextState == STATE_LONG else (ticker['Last'] - slidePrice), AmountOP) # 限价单
        # ID = pfn(-1, AmountOP) # 市价单
        # ID = pfn(AmountOP) # 市价单
        Sleep(Interval)
        Log(exchange.GetOrder(ID)) # xiugai
        CancelPendingOrders()
        pos = GetPosition(PD_LONG if nextState == STATE_LONG else PD_SHORT)
        if len(pos) != 0:
            Log("Average Price of Position",pos[0]['Price'],"Quantity:",pos[0]['Amount'])
            OpenPrice = (exchange.GetOrder(ID))['AvgPrice'] # pos[0]['Price']
            Log("Current Account:",exchange.GetAccount())
            break 

def onTick(exchange):
    global LastBarTime, chart, State, UpTrack, DownTrack, LastAccount
    records = exchange.GetRecords()
    if not records or len(records) <= NPeriod:
        return 
    Bar = records[-1]
    if LastBarTime != Bar['Time']:
        HH = TA.Highest(records, NPeriod, 'High')
        HC = TA.Highest(records, NPeriod, 'Close')
        LL = TA.Lowest(records, NPeriod, 'Low')
        LC = TA.Lowest(records, NPeriod, 'Close')
        
        Range = max(HH - LC, HC - LL)
        UpTrack = _N(Bar['Open'] + (Ks * Range))
        DownTrack = _N(Bar['Open'] - (Kx * Range))
        if LastBarTime > 0:
            PreBar = records[-2]
            chart.add(0, [PreBar['Time'], PreBar['Open'], PreBar['High'], PreBar['Low'], PreBar['Close']], -1)
        else:
            for i in range(len(records) - min(len(records), NPeriod * 3), len(records)):
                b = records[i]
                chart.add(0,[b['Time'], b['Open'], b['High'], b['Low'], b['Close']])
                
        chart.add(0,[Bar['Time'], Bar['Open'], Bar['High'], Bar['Low'], Bar['Close']])
        ChartCfg['yAxis']['plotLines'][0]['value'] = UpTrack 
        ChartCfg['yAxis']['plotLines'][1]['value'] = DownTrack 
        ChartCfg['subtitle'] = {
            'text': 'Upper Band' + str(UpTrack) + 'Lower Band' + str(DownTrack)
        }
        chart.update(ChartCfg)
        chart.reset(PeriodShow)
        
        LastBarTime = Bar['Time']
    else:
        chart.add(0,[Bar['Time'], Bar['Open'], Bar['High'], Bar['Low'], Bar['Close']], -1)
        
    LogStatus("Price:", Bar["Close"], "up:", UpTrack, "down:", DownTrack, "wins:", Counter['w'], "losses:", Counter['l'])
```