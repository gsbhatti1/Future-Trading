---
> Name

RecordsCollecter-Upgrade Provides Custom Data Source Functionality

> Author

InventorQuantum - XiaoXiaoMeng

> Strategy Description

Related Article: [https://www.fmz.com/bbs-topic/5569](https://www.fmz.com/bbs-topic/5569)

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|dropNames|[]|Delete table names|


> Source (python)

``` python
import _thread
import pymongo
import json
import math
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

def url2Dict(url):
    query = urlparse(url).query  
    params = parse_qs(query)  
    result = {key: params[key][0] for key in params}  
    return result

class Provider(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            dictParam = url2Dict(self.path)
            Log("Custom data source service received request, self.path:", self.path, "query parameters:", dictParam)
            
            # Currently, the backtesting system can only choose exchange names from a list. When adding a custom data source, set it to Binance.
            exName = exchange.GetName()                                     
            # Note: period is the underlying K-line interval
            tabName = "%s_%s" % ("records", int(int(dictParam["period"]) / 1000))  
            priceRatio = math.pow(10, int(dictParam["round"]))
            amountRatio = math.pow(10, int(dictParam["vround"]))
            fromTS = int(dictParam["from"]) * int(1000)
            toTS = int(dictParam["to"]) * int(1000)
            
            
            # Connect to database
            Log("Connecting to database service, fetching data, database: ", exName, "table: ", tabName)
            myDBClient = pymongo.MongoClient("mongodb://localhost:27017")
            ex_DB = myDBClient[exName]
            exRecords = ex_DB[tabName]
            
            
            # Requested response data
            data = {
                "schema" : ["time", "open", "high", "low", "close", "vol"],
                "data" : []
            }
            
            # Construct query conditions: greater than a certain value {'age': {'$gt': 20}} or less than a certain value {'age': {'$lt': 20}}
            dbQuery = {"$and":[{'Time': {'$gt': fromTS}}, {'Time': {'$lt': toTS}}]}
            Log("Query conditions: ", dbQuery, "Number of matching records: ", exRecords.find(dbQuery).count(), "Total number of database records: ", exRecords.find().count())
            
            for x in exRecords.find(dbQuery).sort("Time"):
                # Need to process data precision based on request parameters round and vround
                bar = [x["Time"], int(x["Open"] * priceRatio), int(x["High"] * priceRatio), int(x["Low"] * priceRatio), int(x["Close"] * priceRatio), int(x["Volume"] * amountRatio)]
                data["data"].append(bar)
            
            Log("Data: ", data, "Responding to backtesting system request.")
            # Write response data
            self.wfile.write(json.dumps(data).encode())
        except BaseException as e:
            Log("Provider do_GET error, e:", e)


def createServer(host):
    try:
        server = HTTPServer(host, Provider)
        Log("Starting server, listening at: %s:%s" % host)
        server.serve_forever()
    except BaseException as e:
        Log("createServer error, e:", e)
        raise Exception("stop")

def main():
    LogReset(1)
    exName = exchange.GetName()
    period = exchange.GetPeriod()
    Log("Collecting K-line data from", exName, "exchange, K-line interval: ", period, "seconds")
    
    # Connect to database service, service address mongodb://127.0.0.1:27017 as per the MongoDB setup on the server
    Log("Connecting to the database service running on the host device, mongodb://localhost:27017")
    myDBClient = pymongo.MongoClient("mongodb://localhost:27017")   
    # Create database
    ex_DB = myDBClient[exName]
    
    # Print current database tables
    collist = ex_DB.list_collection_names()
    Log("mongodb ", exName, " collist:", collist)
    
    # Check if any table should be deleted
    arrDropNames = json.loads(dropNames)
    if isinstance(arrDropNames, list):
        for i in range(len(arrDropNames)):
            dropName = arrDropNames[i]
            if isinstance(dropName, str):
                if not dropName in collist:
                    continue
                tab = ex_DB[dropName]
                Log("dropName:", dropName, "Deleting: ", dropName)
                ret = tab.drop()
                collist = ex_DB.list_collection_names()
                if dropName in collist:
                    Log(dropName, "Deletion failed")
                else :
                    Log(dropName, "Deleted successfully")
    
    # Start a thread to provide custom data source service
    try:
        _thread.start_new_thread(createServer, (("0.0.0.0", 9090), ))         # Testing on VPS server
        Log("Starting custom data source service thread", "#FF0000")
    except BaseException as e:
        Log("Failed to start custom data source service!")
        Log("Error information: ", e)
        raise Exception("stop")
    
    # Create "records" table
    ex_DB_Records = ex_DB["%s_%d" % ("records", period)]
    Log("Starting collection of K-line data from", exName, "interval: ", period, "Opening (creating) database table:", "%s_%d" % ("records", period), "#FF0000")
    preBarTime = 0
    index = 1
    while True:
        r = _C(exchange.GetRecords)
        if len(r) < 2:
            Sleep(1000)
            continue
        if preBarTime == 0:
            # Write all bar data for the first time
            for i in range(len(r) - 1):
                bar = r[i]
                # Write one by one, need to check whether the database table already has this record based on timestamp. If it does, skip; if not, write.
                retQuery = ex_DB_Records.find({"Time": bar["Time"]})
                if retQuery.count() > 0:
                    continue
                
                # Insert bar into database table
                ex_DB_Records.insert_one({"High": bar["High"], "Low": bar["Low"], "Open": bar["Open"], "Close": bar["Close"], "Time": bar["Time"], "Volume": bar["Volume"]})                
                index += 1
            preBarTime = r[-1]["Time"]
        elif preBarTime != r[-1]["Time"]:
            bar = r[-2]
            # Check before writing whether the data already exists based on timestamp
            retQuery = ex_DB_Records.find({"Time": bar["Time"]})
            if retQuery.count() > 0:
                continue
            
            ex_DB_Records.insert_one({"High": bar["High"], "Low": bar["Low"], "Open": bar["Open"], "Close": bar["Close"], "Time": bar["Time"], "Volume": bar["Volume"]})
            index += 1
            preBarTime = r[-1]["Time"]
```