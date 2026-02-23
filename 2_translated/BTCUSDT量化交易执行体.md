<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

BTCUSDT Quantitative Trading Executor

> Author

zomo

> Strategy Description

```
https://github.com/Find-Dream/BTCUSDT
```

> Currently only supports OKX API interface, BTCUSDT perpetual contract trading. Quantitative trading pursues stable returns, so please do not set high leverage. It is recommended to use leverage of 5x or below.

- The Windows version is the GUI version. After downloading, first configure the exchange API through set_api, then run the btcusdt program to start automatic trading;
- The Python source code GUI version can run on any desktop operating system, as long as Python environment is installed and configured. It is recommended to use Python 3.7.7 version and requires the requests library. The usage is similar to the Windows GUI version;
- The Python source code command line version can run on any operating system, as long as Python environment is installed and configured. It is recommended to use Python 3.7.7 version and requires the requests library. Configure the exchange API by manually modifying the `okex_api.json` file. In CentOS, the following command can make the executor run automatically in the background:
```
nohup python3 start.py &
```
Use the following command to terminate the process and stop trading:
```
ps -aux | grep start.py
kill -9 process number obtained
```


### API Precautions:

- If you are not running on a cloud host with a fixed IP, please do not set IP binding, otherwise it will not work;
- For your account security, when applying for API, please check read-only and trading permissions, do not check withdrawal permissions;
- The flag in `okex_api.json` is the trading disk option, 0 for real disk, 1 for simulated disk;

### Common Issues
##### Stuck after starting trading

- Incorrect API settings, please check if the API is configured correctly. Real disk and simulated disk APIs are different and need to be set separately;
- Domestic network cannot access the exchange, please use overseas cloud hosts to run the executor. Hong Kong cloud hosts are recommended;
- Do not use VPN software in China to start the executor. Due to compatibility issues, using VPN software will likely cause it to fail to run;





> Source (python)

``` python
from okex.trade import trade,pos_info,acc_info,select_last
import okex.api as api
import okex.Trade_api as Trade
import time
import json
from okex.log import log

# Full strategy source code download address https://github.com/Find-Dream/BTCUSDT

def main():
    nowtime = time.time()
    st = time.localtime(nowtime)
    update = time.strftime('%Y-%m-%d',st)
    filenamedate = time.strftime('%Y%m%d',st)
    logfilename = 'mark_'+ str(filenamedate)

    log(logfilename,'========================【Getting basic information starts】========================')

    btcusdt_api_data = api.btcusdt_api()

    log(logfilename,'btcusdt_api_data：'+str(btcusdt_api_data))

    btcusdt_api = btcusdt_api_data['rule']
    log(logfilename,'btcusdt_api'+str(btcusdt_api))

    pos_api = btcusdt_api_data['pos']
    log(logfilename,'pos_api'+str(pos_api))

    pos_okex = {}
    acc_okex = {}
    try:
        acc_api = api.select_acc()
        log(logfilename,'Read locally saved account information'+str(acc_api))
    except:
        acc_okex['lever'] = 1


    acc_info_data = acc_info()[0]['details']


    for i in acc_info_data:
        if i['ccy'] == 'USDT':
            acc_okex['ccy'] = i['cashBal']
            log(logfilename,'Read interface account balance'+str(i['cashBal']))

    for i in pos_info():
        if i['mgnMode'] == 'cross' and i['posSide'] == 'long':
            pos_okex['long'] = i['pos']
            if i['pos'] != '0':
                acc_okex['lever'] = i['lever']
                log(logfilename,'Read interface long account leverage multiple：'+str(i['lever']))
            else:
                acc_okex['lever'] = acc_api['lever']
                log(logfilename,'Read local long account leverage multiple：'+str(acc_api['lever']))
        elif i['mgnMode'] == 'cross' and i['posSide'] == 'short':
            pos_okex['short'] = i['pos']
            if i['pos'] != '0':
                acc_okex['lever'] = i['lever']
                log(logfilename,'Read interface short account leverage multiple：'+str(i['lever']))
            

    api.set_acc(json.dumps(acc_okex))
    log(logfilename,'Write local account information：'+str(acc_okex))
    last = float(select_last())
    log(logfilename,'Read current price：'+str(last))

    max_sz = int(float(acc_okex['ccy']) * float(acc_okex['lever']) / last * 100)
    log(logfilename,'Maximum trading volume：'+str(max_sz))

    sz_r = max_sz / 20
    log(logfilename,'Trading volume coefficient：'+str(sz_r))

    pos_api_id = int(btcusdt_api['id'])
    pos_api_posSide = btcusdt_api['posside']
    pos_api_side = btcusdt_api['side']
    pos_api_sz = int(int(btcusdt_api['sz']) * sz_r)
    pos_api_uptime = int(btcusdt_api['uptime'])
    pos_api_long = int(int(pos_api['long']) * sz_r)
    pos_api_short = int(int(pos_api['short']) * sz_r)

    log(logfilename,'pos_api_long：'+str(pos_api_long)+',pos_api_short:'+str(pos_api_short)+',pos_api_sz:'+str(pos_api_sz))
    log(logfilename,'Local position information pos_okex：'+str(pos_okex))


    try:
        pos_log_done = int(api.pos_log_done())
    except:
        pos_log_done = api.pos_log_done()
    
    log(logfilename,'pos_log_done:'+str(pos_log_done))

    log(logfilename,'========================【Getting basic information ends】========================')
    log(logfilename,'========================【mark task starts】========================')
    log(logfilename,'Determine whether pos_log_done_id is int type:'+str(type(pos_log_done)))
    if isinstance(pos_log_done,int):
        log(logfilename,'pos_log_done_id is int type, determine pos_log_done_id and pos_log_id,pos_api_id:'+str(pos_api_id)+',pos_log_done:'+str(pos_log_done))
        if pos_api_id > pos_log_done:
            log(logfilename,'API's pos_log_id is greater than pos_log_done_id, determine whether API update time is within 10 seconds,nowtime:'+str(nowtime)+',pos_api_uptime:'+str(pos_api_uptime))
            if nowtime < (pos_api_uptime + 13):
                log(logfilename,'API update time is within 10 seconds, determine API trading direction,pos_api_posSide'+str(pos_api_posSide)+',pos_api_side:'+str(pos_api_side))
                if pos_api_posSide == 'long' and pos_api_side == 'buy':
                    log(logfilename,'API trading direction：long-buy，determine whether current position information matches API')
                    if int(pos_okex['long']) + int(pos_api_sz) == int(pos_api_long):
                        log(logfilename,'Current position information matches API, execute trading, current position：'+str(pos_okex['long'])+',API position：'+str(pos_api_long)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,pos_api_sz,pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    elif int(pos_okex['long']) + int(pos_api_sz) < int(pos_api_long):
                        log(logfilename,'Current position information matches API, execute trading, current position：'+str(pos_okex['long'])+',API position：'+str(pos_api_long)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,pos_api_sz,pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    else:
                        log(logfilename,'Long position information inconsistent, please manually close the long position before automatic trading, current position：'+str(pos_okex['long'])+',API position：'+str(pos_api_long)+',API trading quantity：'+str(pos_api_sz))

                elif pos_api_posSide == 'long' and pos_api_side == 'sell':
                    log(logfilename,'API trading direction：long-sell，determine whether closing conditions are met')
                    if int(pos_okex['long']) > 0:
                        log(logfilename,'Closing conditions met, current position：'+str(pos_okex['long'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,int(pos_okex['long']),pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    else:
                        log(logfilename,'Long position information inconsistent, please manually close the long position before automatic trading, current position：'+str(pos_okex['long'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))

                elif pos_api_posSide == 'short' and pos_api_side == 'sell':
                    log(logfilename,'API trading direction：short-sell，determine whether current position information matches API')
                    if int(pos_okex['short']) + int(pos_api_sz) == int(pos_api_short):
                        log(logfilename,'Opening conditions met, execute trading, current position：'+str(pos_okex['short'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,pos_api_sz,pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    elif int(pos_okex['short']) + int(pos_api_sz) < int(pos_api_short):
                        log(logfilename,'Opening conditions met, execute trading, current position：'+str(pos_okex['short'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,pos_api_sz,pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    else:
                        log(logfilename,'Short position information inconsistent, please manually close the short position before automatic trading, current position：'+str(pos_okex['short'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))

                elif pos_api_posSide == 'short' and pos_api_side == 'buy':
                    log(logfilename,'API trading direction：short-buy，determine whether closing conditions are met')
                    if int(pos_okex['short']) > 0:
                        log(logfilename,'Closing conditions met, current position：'+str(pos_okex['short'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))
                        trade_ok = trade(pos_api_side,pos_api_posSide,pos_okex['short'],pos_api_id)
                        log(logfilename,'Execution result：'+str(trade_ok))
                    else:
                        log(logfilename,'Short position information inconsistent, please manually close the short position before automatic trading, current position：'+str(pos_okex['short'])+',API position：'+str(pos_api_short)+',API trading quantity：'+str(pos_api_sz))
            else:
                log(logfilename,'API update time exceeds 10 seconds, missed best trading time,nowtime:'+str(nowtime)+',pos_api_uptime:'+str(pos_api_uptime))
        else:
            log(logfilename,'API's pos_log_id is not greater than pos_log_done_id, no new API data, continue monitoring,pos_api_id:'+str(pos_api_id)+',pos_log_done:'+str(pos_log_done))
    else:
        log(logfilename,'pos_log_done_id is not int type')
        api.set_pos_log_done(pos_api_id)
    log(logfilename,'========================【mark task ends】========================')

```

> Detail

https://www.fmz.com/strategy/321120

> Last Modified

2021-10-03 09:32:41