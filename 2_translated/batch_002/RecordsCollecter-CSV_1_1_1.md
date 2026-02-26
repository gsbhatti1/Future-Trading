``` python
import _thread
import pymongo
import json
import math
import csv
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

def url2Dict(url):
    query = urlparse(url).query  
    params = parse_qs(query)  
    result = {key: params[key][0] for key in params}  
    return result

class Provider(BaseHTTPRequestHandler):
    def do_GET(self):
        global isOnlySupportCSV, filePathForCSV
        try:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            dictParam = url2Dict(self.path)
            Log("Custom data source service received a request, self.path:", self.path, "query parameters:", dictParam)
            
            # Currently, the backtesting system can only choose an exchange name from a list. When adding a custom data source, set it to Binance.
            exName = exchange.GetName()                                     
            # Note: period is the underlying K-line interval.
            tabName = "%s_%s" % ("records", int(int(dictParam["period"]) / 1000))  
            priceRatio = math.pow(10, int(dictParam["round"]))
            amountRatio = math.pow(10, int(dictParam["vround"]))
            fromTS = int(dictParam["from"]) * int(1000)
            toTS = int(dictParam["to"]) * int(1000)

            # Required response data
            data = {
                "schema" : ["time", "open", "high", "low", "close", "vol"],
                "data" : []
            }
            
            if isOnlySupportCSV:
                # Handle CSV reading, filePathForCSV path
                listDataSequence = []
                with open(filePathForCSV, "r") as f:
                    reader = csv.reader(f)
                    # Get the header
                    header = next(reader)
                    headerIsNoneCount = 0
                    if len(header) != len(data["schema"]):
                        Log("Incorrect CSV file format, different number of columns. Please check!", "#FF0000")
                        return 
                    for ele in header:
                        for i in range(len(data["schema"])):
                            if data["schema"][i] == ele or ele == "":
                                if ele == "":
                                    headerIsNoneCount += 1
                                if headerIsNoneCount > 1:
                                    Log("Incorrect CSV file format. Please check!", "#FF0000")
                                    return 
                                listDataSequence.append(i)
                                break
                    
                    # Read content
                    while True:
                        record = next(reader, -1)
                        if record == -1:
                            break
                        index = 0
                        arr = [0, 0, 0, 0, 0, 0]
                        for ele in record:
                            arr[listDataSequence[index]] = int(ele) if listDataSequence[index] == 0 else (int(float(ele) * amountRatio) if listDataSequence[index] == 5 else int(float(ele) * priceRatio))
                            index += 1
                        data["data"].append(arr)
                
                Log("Data: ", data, "Responding to backtesting system request.")
                self.wfile.write(json.dumps(data).encode())
                return 
            
            # Connect to the database
            Log("Connecting to the database service, fetching data. Database: ", exName, " Table: ", tabName)
            myDBClient = pymongo.MongoClient("mongodb://localhost:27017")
            ex_DB = myDBClient[exName]
            exRecords = ex_DB[tabName]
            
            # Construct query conditions: greater than a value {'age': {'$gt': 20}} less than a value {'age': {'$lt': 20}}
            dbQuery = {"$and":[{'Time': {'$gt': fromTS}}, {'Time': {'$lt': toTS}}]}
            Log("Query conditions: ", dbQuery, "Number of query results: ", exRecords.find(dbQuery).count(), "Total number of records in the database: ", exRecords.find().count())
            
            for x in exRecords.find(dbQuery).sort("Time"):
                # Need to process data precision according to request parameters round and vround
                bar = [x["Time"], int(x["Open"] * priceRatio), int(x["High"] * priceRatio), int(x["Low"] * priceRatio), int(x["Close"] * priceRatio), int(x["Volume"] * amountRatio)]
                data["data"].append(bar)
            
            Log("Data: ", data, "Responding to backtesting system request.")
            # Write the response data
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
    if (isOnlySupportCSV):
        try:
            # _thread.start_new_thread(createServer, (("localhost", 9090), ))         # For local testing
            _thread.start_new_thread(createServer, (("0.0.0.0", 9090), ))         # For VPS server testing
            Log("Starting custom data source service thread, providing data from CSV files.", "#FF0000")
        except BaseException as e:
            Log("Failed to start custom data source service!")
            Log("Error message: ", e)
            raise Exception("stop")
        while True:
            LogStatus(_D(), "Only starting the custom data source service, not collecting data!")
            Sleep(2000)
    
    exName = exchange.GetName()
    period = exchange.GetPeriod()
    Log("Collecting K-line data from", exName, "exchange, K-line interval:", period, "seconds")
    
    # Connect to the database service, server address mongodb://127.0.0.1:27017 for specific settings based on MongoDB installation
    Log("Connecting to the MongoDB service running on the host device, mongodb://localhost:27017")
    myDBClient = pymongo.MongoClient("mongodb://localhost:27017")   
    # Create a database
    ex_DB = myDBClient[exName]
    
    # Print currently available tables in the database
    collist = ex_DB.list_collection_names()
    Log("MongoDB ", exName, " collist:", collist)
    
    # Check if any table should be deleted
    arrDropNames = json
```