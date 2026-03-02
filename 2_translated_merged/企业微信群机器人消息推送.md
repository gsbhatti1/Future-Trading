> Name

Enterprise WeChat group robot message push

> Author

BTC【Strategy Ghostwriting】Team


> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|webhook|https://...|webhook|


> Source(python)

```python
#!Python3

"""
"Strategy Ghostwriting" and (Help for this program), write to QQ: 35787501

Enterprise WeChat message push for group custom robots
In the same way: you can modify data and connect to webhooks of other software.
"""

import requests


def send(text):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": text,
        }
    }
    response = requests.post(webhook, headers=headers, json=data)
    records = response.json()
    return records


def LogQYWX(*args):
    text = " ".join(args)
    Log(text, send(text))


ext.LogQYWX = LogQYWX

```

> Detail

https://www.fmz.com/strategy/430810

> Last Modified

2023-11-02 10:14:01