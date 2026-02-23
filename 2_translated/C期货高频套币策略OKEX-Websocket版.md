---
> Name

C++ Futures High-Frequency Arbitrage Strategy OKEX-Websocket Edition

> Author

Inventor Quantitative - Xiao Xiaomeng

> Strategy Description

## C++ Futures High-Frequency Arbitrage Strategy OKEX Websocket Edition

### Strategy Principle 

The principle of the strategy is simple, implementing cross-period hedging on the OKEX futures contracts. The position management design involves a differential grid hedging mechanism.
The strategy defines two contracts: Contract A and Contract B. Different contract codes can be set for different types of contracts to conduct hedging.
For example, setting Contract A as a quarterly contract and Contract B as an upcoming weekly contract (or vice versa).

### Hedging Operations 

- **Buy Short on A (quarterly), Long on B (similar to long-term futures arbitrage in commodity futures, where one sells the future contract for delivery while buying the near-term contract to achieve profit)**
- **Long on A, Sell Short on B (similar to shorting the near-term and going long on the future in commodity futures for reverse arbitrage)**

### Design Features 

1. **Programming Language** 
   - The strategy is written in C++, offering performance advantages with its speed.

2. **Market Data Source**
   - Market data driven by using OKEX WebSocket API, which provides timely price updates and uses real-time tick data to generate K-line charts. A K-line generator specifically constructs the differential K-lines based on the tick data.
   - The opening and closing positions of hedging operations are driven by the generated K-line data.

3. **Position Management**
   - Position management is controlled through a proportional allocation similar to the Fibonacci sequence, ensuring that larger price differences lead to increased arbitrage quantities for more dispersed positions.
   
4. **Stop Loss and Take Profit** 
   - Fixed stop loss and take profit levels are set.
   - Positions are closed when the current differential reaches either the stop loss or take profit level.

5. **Cycle Design for Entering and Exiting Markets**
   - A parameter `NPeriod` dynamically controls the opening and closing of positions in the strategy.
   
6. **Position Balancing System, Order Monitoring System** 
   - The strategy has a dedicated system to regularly check position balances and monitor orders.
   
7. **Strategy Expansion**
   - The code design is loosely coupled, allowing for further expansion into commodity futures hedging or additional optimization.

8. **Strategy Charts**
   - The strategy automatically generates differential K-line charts with relevant trade information marked on them.

### Backtest

![IMG](https://www.fmz.com/upload/asset/165549c612d8ba5ae550.png) 

![IMG](https://www.fmz.com/upload/asset/168d0e671a56094b28c3.png) 

![IMG](https://www.fmz.com/upload/asset/170dcc772a1925d46885.png)

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|InstrumentA|this_week|Recent Contract|
|InstrumentB|next_week|Future Contract|
|DPeriod|30|Differential Period (Seconds)|
|NPeriod|20|Cycle Length|
|LeavePeriod|5|Exit Cycle|
|AddMax|5|Maximum Add Times|
|StopLoss|10|Stop Loss Differential|
|StopWin|30|Take Profit Differential|
|OpenAmount|10|Lot Size|
|SlidePrice|true|Slippage|
|MaxDelay|500|Maximum Market Delay (Milliseconds)|
|IsSetProxy|false|(? Proxy) Set Proxy|

> Source Code (C++)

``` cpp
/*backtest
start: 2019-07-22 00:00:00
end: 2019-08-21 00:00:00
period: 1m
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD","stocks":0.1,"fee":[0.02,0.05]}]
args: [["InstrumentB","quarter"],["NPeriod",200],["LeavePeriod",100],["AddMax",3],["StopLoss",20],["StopWin",50],["OpenAmount",2]]
*/

enum State {
    STATE_NA,
    STATE_IDLE,
    STATE_HOLD_LONG,
    STATE_HOLD_SHORT,
};

string replace(string s, const string from, const string& to) {
    if(!from.empty())
        for(size_t pos = 0; (pos = s.find(from, pos)) != std::string::npos; pos += to.size())
            s.replace(pos, from.size(), to);
    return s;
}

class BarFeeder {
public:
    BarFeeder(int period) : _period(period) {
        _rs.Valid = true;
    }

    void feed(double price, Chart *c=nullptr, int chartIdx=0) {
        uint64_t epoch = uint64_t(Unix() / _period) * _period * 1000;
        bool newBar = false;
        if (_rs.size() == 0 || _rs[_rs.size()-1].Time < epoch) {
            Record r;
            r.Time = epoch;
            r.Open = r.High = r.Low = r.Close = price;
            _rs.push_back(r);
            if (_rs.size() > 2000) {
                _rs.erase(_rs.begin());
            }
            newBar = true;
        } else {
            Record &r = _rs[_rs.size() - 1];
            r.High = max(r.High, price);
            r.Low = min(r.Low, price);
            r.Close = price;
        }

        auto bar = _rs[_rs.size()-1];
        json point = {bar.Time, bar.Open, bar.High, bar.Low, bar.Close};
        if (c != nullptr) {
           if (newBar) {
                c->add(chartIdx, point);
                c->reset(1000);
            } else {
                c->add(chartIdx, point, -1);
            }
        }
    }

    Records & get() {
        return _rs;
    }

private:
    int _period;
    Records _rs;
};

class Hedge {
public:
    Hedge() {
        _isCover = true;
        _needCheckOrder = true;
        _st = STATE_NA;
        for (int i = 0; i < AddMax + 1; i++) {
            if (_addArr.size() < 2) {
                _addArr.push_back((i+1)*OpenAmount);
            }
            _addArr.push_back(_addArr[_addArr.size()-1] + _addArr[_addArr.size()-2]);
        }

        _cfgStr = R"EOF(
        [{
        "extension": { "layout": "single", "col": 6, "height": "500px"},
        "rangeSelector": {"enabled": false},
        "tooltip": {"xDateFormat": "%Y-%m-%d %H:%M:%S, %A"},
        "plotOptions": {"candlestick": {"color": "#d75442", "upColor": "#6ba583"}},
        "chart":{"type":"line"},
        "title":{"text":"Spread Long"},
        "xAxis":{"title":{"text":"Date"}},
        "series":[
            {"type":"candlestick", "name":"Long Spread","data":[], "id":"dataseriesA"},
            {"type":"flags","data":[], "onSeries": "dataseriesA"}
            ]
        },
        {
        "extension": { "layout": "single", "col": 6, "height": "500px"},
        "rangeSelector": {"enabled": false},
        "tooltip": {"xDateFormat": "%Y-%m-%d %H:%M:%S, %A"},
        "plotOptions": {"candlestick": {"color": "#d75442", "upColor": "#6ba583"}},
        "chart":{"type":"line"},
        "title":{"text":"Spread Short"},
        "xAxis":{"title":{"text":"Date"}},
        "series":[
            {"type":"candlestick", "name":"Long Spread","data":[], "id":"dataseriesA"},
            {"type":"flags","data":[], "onSeries": "dataseriesA"}
            ]
        }
        ]
        )EOF";
        _c.update(_cfgStr);
        _c.reset();
    };

    State getState(string &symbolA, Depth &depthA, string &symbolB, Depth &depthB) {
        
        if (!_needCheckOrder && _st != STATE_NA) {
            return _st;
        }

        //Log("sync orders");
        auto orders = exchange.GetOrders();
        if (!orders.Valid) {
            return STATE_NA;
        }

        if (orders.size() > 0) {
            for (auto &order : orders) {
                exchange.CancelOrder(order.Id);
            }
            return STATE_NA;
        }
        
        Sleep(500);
        
        //Log("sync positions");
        
        auto positions = exchange.GetPosition();
        if (!positions.Valid) {
            return STATE_NA;
        }
``` 

Note: The source code has been translated and is intended to provide a high-level understanding of the strategy, but it may need further adjustments for specific implementation. Adjustments such as the `Sleep` function might require changes based on the environment where this strategy is being deployed. Additionally, ensure that all necessary libraries or configurations are included in your development setup. 

If you have any specific questions about the code or its functionality, feel free to ask! 🚀