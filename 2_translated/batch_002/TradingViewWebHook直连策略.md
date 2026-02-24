<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

TradingViewWebHook Direct Connection Strategy

> Author

FMZ Quant - Xiao Xiao Meng

> Strategy Description

Related article: https://www.fmz.com/bbs-topic/5969

Due to some issues with HTTPServer itself, consider using ThreadingHTTPServer instead.
Reference: https://docs.python.org/3.7/library/http.server.html
Requires Python 3.7 version.

Resources on HTTPServer issues:
https://www.zybuluo.com/JunQiu/note/1350528

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|AccessKey|$$$__enc__$$$|AccessKey secret|
|SecretKey|$$$__enc__$$$|SecretKey secret|
|ContractType||Contract ID|
|Port|80|Listening port number of the service|
|UseMarketOrderForCTP|true|Use market order for commodity futures|
|isDealBodyMsg|false|Whether to process Body message|
|amount|0.0001|Order amount|
|ct|swap|Contract code|


> Source (python)

``` python
'''
Request format: http://x.x.x.x:xxxx/data?access_key=xxx&secret_key=yyy&type=buy&amount=0.001
Strategy bot parameters:
- Type: encrypted string, AccessKey, SecretKey. You can use FMZ platform's low-permission API KEY, or generate your own KEY.
- Type: string, contract ID, ContractType
- Type: numeric, port number, Port
'''

import re
import _thread
import json
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

def url2Dict(url):
    query = urlparse(url).query  
    params = parse_qs(query)  
    result = {key: params[key][0] for key in params}  
    return result

class Executor(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            dictParam = url2Dict(self.path)
            Log("Test", dictParam)
        except Exception as e:
            Log("Provider do_GET error, e:", e)
    def do_POST(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dictParam = url2Dict(self.path)
            
            # Test POST request Body information            
            data = self.rfile.read(200)   # Specified read length
            Log("data:", data)            # Print POST request data, can let the bot execute corresponding operations based on data in the request
            
            # Validation
            if len(dictParam) == 4 and dictParam["access_key"] == AccessKey and dictParam["secret_key"] == SecretKey:
                del dictParam["access_key"]
                del dictParam["secret_key"]
                Log("Received request", "Parameters:", dictParam, "#FF0000")
                '''
                map[access_key:xxx amount:0.001 secret_key:yyy type:buy]
                '''
                isSpot = True
                if exchange.GetName().find("Futures") != -1:
                    if ContractType != "":
                        exchange.SetContractType(ContractType)
                        isSpot = False 
                    else :
                        raise "Futures contract not set"
                                
                q = None
                if exchange.GetName() == "Futures_CTP" and UseMarketOrderForCTP == False:
                    q = ext.NewTaskQueue()
                
                if isSpot and dictParam["type"] == "buy":
                    exchange.Buy(-1, float(dictParam["amount"]))
                    Log(exchange.GetAccount())
                elif isSpot and dictParam["type"] == "sell":
                    exchange.Sell(-1, float(dictParam["amount"]))
                    Log(exchange.GetAccount())
                elif not isSpot and dictParam["type"] == "long":
                    exchange.SetDirection("buy")
                    if not q:
                        exchange.Buy(-1, float(dictParam["amount"]))
                    else :
                        q.pushTask(exchange, ContractType, "buy", float(dictParam["amount"]), lambda task, ret: Log(task["desc"], ret, "#FF0000"))
                    Log("Positions:", exchange.GetPosition())
                elif not isSpot and dictParam["type"] == "short":
                    exchange.SetDirection("sell")
                    if not q:
                        exchange.Sell(-1, float(dictParam["amount"]))
                    else :
                        q.pushTask(exchange, ContractType, "sell", float(dictParam["amount"]), lambda task, ret: Log(task["desc"], ret, "#FF0000"))
                    Log("Positions:", exchange.GetPosition())
                elif not isSpot and dictParam["type"] == "cover_long":
                    exchange.SetDirection("closebuy")
                    if not q:
                        exchange.Sell(-1, float(dictParam["amount"]))
                    else :
                        q.pushTask(exchange, ContractType, "closebuy", float(dictParam["amount"]), lambda task, ret: Log(task["desc"], ret, "#FF0000"))
                    Log("Positions:", exchange.GetPosition())
                elif not isSpot and dictParam["type"] == "cover_short":
                    exchange.SetDirection("closesell")
                    if not q:
                        exchange.Buy(-1, float(dictParam["amount"]))
                    else :
                        q.pushTask(exchange, ContractType, "closesell", float(dictParam["amount"]), lambda task, ret: Log(task["desc"], ret, "#FF0000"))
                    Log("Positions:", exchange.GetPosition())
                
                if q is not None:
                    while q.size() > 0:
                        q.poll()
                        Sleep(500)
            
            # Process body data
            if isDealBodyMsg:
                if exchange.GetName().find("Futures") != -1:
                    Log("data:", data.decode('utf-8'))  # Test
                    if re.search(r'buy', data.decode('utf-8')):
                        Log("Trigger buy")
                        exchange.SetContractType(ct)
                        exchange.SetDirection("buy")
                        exchange.Buy(-1, amount)
                    elif re.search(r'sell', data.decode('utf-8')):
                        Log("Trigger sell")
                        exchange.SetContractType(ct)
                        exchange.SetDirection("sell")
                        exchange.Sell(-1, amount)
            
            # Write response data
            self.wfile.write(json.dumps({"state": "ok"}).encode())
        except Exception as e:
            Log("Provider do_POST error, e:", e)


def createServer(host):
    try:
        server = ThreadingHTTPServer(host, Executor)
        Log("Starting server, listen at: %s:%s" % host)
        server.serve_forever()
    except Exception as e:
        Log("createServer error, e:", e)
        raise Exception("stop")

def main():
    # Start a thread
    try:
        _thread.start_new_thread(createServer, (("0.0.0.0", Port), ))         # Test on VPS server           
    except Exception as e:        
        Log("Error message:", e)
        raise Exception("stop")    
    if exchange.GetName().find("Futures") != -1:
        exchange.SetContractType(ContractType)
    Log("Account asset information:", _C(exchange.GetAccount))
    while True:
        if exchange.GetName() == "Futures_CTP":
            if exchange.IO("status"):
                LogStatus(_D(), "CTP Connected")
            else:
                LogStatus(_D(), "CTP Not Connected")
        else:
            LogStatus(_D())
        Sleep(2000)
```

> Detail

https://www.fmz.com/strategy/221850

> Last Modified

2021-03-31 11:33:30