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
            
            # Currently, the backtesting system can only select exchange names from a list. When adding a custom data source, set it to Binance.
            exName = exchange.GetName()                                     
            # Note: period is the underlying K-line interval.
            tabName = "%s_%s" % ("records", int(int(dictParam["period"]) / 1000))  
            priceRatio = math.pow(10, int(dictParam["round"]))
            amountRatio = math.pow(10, int(dictParam["vround"]))
            fromTS = int(dictParam["from"]) * int(1000)
            toTS = int(dictParam["to"]) * int(1000)
            
            
            # Connect to the database
            Log("Connecting to database service to fetch data, database:", exName, "table:", tabName)
            myDBClient = pymongo.MongoClient("mongodb://localhost:27017")
            ex_DB = myDBClient[exName]
            exRecords = ex_DB[tabName]
            
            # Required response data
            data = {
                "schema" : ["time", "open", "high", "low", "close", "vol"],
                "data" : []
            }
            
            # Construct query conditions: greater than a value {'age': {'$gt': 20}} less than a value {'age': {'$lt': 20}}
            dbQuery = {"$and":[{'Time': {'$gt': fromTS}}, {'Time': {'$lt': toTS}}]}
            Log("Query conditions:", dbQuery, "Number of queried records:", exRecords.find(dbQuery).count(), "Total number of records in the database:", exRecords.find().count())
            
            for x in exRecords.find(dbQuery).sort("Time"):
                # Need to process data precision according to request parameters round and vround
                bar = [x["Time"], int(x["Open"] * priceRatio), int(x["High"] * priceRatio), int(x["Low"] * priceRatio), int(x["Close"] * priceRatio), int(x["Volume"] * amountRatio)]
                data["data"].append(bar)
            
            Log("Data:", data, "Responding to backtesting system request.")
            # Write the data response
            self.wfile.write(json.dumps(data).encode())
        except BaseException as e:
            Log("Provider do_GET error, e:", e)


def createServer(host):
    try:
        server = HTTPServer(host, Provider)
        Log("Starting server, listen at: %s:%s" % host)
        server.serve_forever()
    except BaseException as e:
        Log("createServer error, e:", e)
        raise Exception("stop")

def main():
    LogReset(1)
    exName = exchange.GetName()
    period = exchange.GetPeriod()
    Log("Collecting K-line data from", exName, "exchange, K-line interval:", period, "seconds")
    
    # Connect to the database service, server address: mongodb://127.0.0.1:27017 (specific settings depend on the MongoDB installed on the server)
    Log("Connecting to the MongoDB service hosted on the device, mongodb://localhost:27017")
    myDBClient = pymongo.MongoClient("mongodb://localhost:27017")   
    # Create a database
    ex_DB = myDBClient[exName]
    
    # Print current database tables
    collist = ex_DB.list_collection_names()
    Log("MongoDB", exName, "collist:", collist)
    
    # Check if dropping tables
    arrDropNames = json.loads(dropNames)
    if isinstance(arrDropNames, list):
        for i in range(len(arrDropNames)):
            dropName = arrDropNames[i]
            if isinstance(dropName, str):
                if not dropName in collist:
                    continue
                tab = ex_DB[dropName]
                Log("dropName:", dropName, "Dropping: ", dropName)
                ret = tab.drop()
                collist = ex_DB.list_collection_names()
                if dropName in collist:
                    Log(dropName, "Drop failed")
                else :
                    Log(dropName, "Drop successful")
    
    # Start a thread to provide custom data source service
    try:
        _thread.start_new_thread(createServer, (("0.0.0.0", 9090), ))         # Testing on VPS server
        Log("Starting custom data source service thread", "#FF0000")
    except BaseException as e:
        Log("Failed to start custom data source service!")
        Log("Error message:", e)
        raise Exception("stop")
    
    # Create the records table
    ex_DB_Records = ex_DB["%s_%d" % ("records", period)]
    Log("Starting to collect K-line data from", exName, "interval: ", period, "Opening (creating) database table:", "%s_%d" % ("records", period), "#FF0000")
    preBarTime = 0
    index = 1
    while True:
        r = _C(exchange.GetRecords)
        if len(r) < 2:
            Sleep(1000)
            continue
        if preBarTime == 0:
            # Writing all BAR data for the first time
            for i in range(len(r) - 1):
                bar = r[i]
                # Writing one by one, need to check whether the current database table already has this record based on timestamp. If it does, skip; if not, write.
                retQuery = ex_DB_Records.find({"Time": bar["Time"]})
                if retQuery.count() > 0:
                    continue
                
                # Insert bar into the database table
                ex_DB_Records.insert_one({"High": bar["High"], "Low": bar["Low"], "Open": bar["Open"], "Close": bar["Close"], "Time": bar["Time"], "Volume": bar["Volume"]})                
                index += 1
            preBarTime = r[-1]["Time"]
        elif preBarTime != r[-1]["Time"]:
            bar = r[-2]
            # Check before writing whether the data already exists based on timestamp.
            retQuery = ex_DB_Records.find({"Time": bar["Time"]})
            if retQuery.count() > 0:
                continue
            
            ex_DB_Records.insert_one({"High": bar["High"], "Low": bar["Low"], "Open": bar["Open"], "Close": bar["Close"], "Time": bar["Time"], "Volume": bar["Volume"]})
            index += 1
            preBarTime = r[-1]["Time"]
```