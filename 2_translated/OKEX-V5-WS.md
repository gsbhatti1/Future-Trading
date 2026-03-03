Name

OKEX-V5-WS interface account position push example

Author

Inventor Quantification-Little Dream

Strategy Description

## OKEX V5 WS interface account position push example

Example of using the private interface of OKEX V5 WS, with policy parameters ```accessKey```, ```secretKey```, ```passphrase```. Among them, ```passphrase``` is the secret key password filled in when creating APIKEY on the exchange website. The strategy example first logs in to verify and then subscribes to all position information. Send ping regularly, and the exchange server will respond with pong.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|accessKey|$$$__enc__$$$|accessKey|
|secretKey|$$$__enc__$$$|secretKey|
|passphrase|$$$__enc__$$$|passphrase|


> Source (javascript)

``` javascript
function getLogin(pAccessKey, pSecretKey, pPassphrase) {
    // Signature function, used for login
    var ts = (new Date().getTime() / 1000) + ""
    var login = {
        "op": "login",
        "args":[{
            "apiKey" : pAccessKey,
            "passphrase" : pPassphrase,
            "timestamp" : ts,
            "sign" : exchange.HMAC("sha256", "base64", ts + "GET" + "/users/self/verify", pSecretKey)
        }]
    }
    return login
}

var client_private = null
function main() {
    // Because the read function uses a timeout setting, filter timeout errors, otherwise there will be redundant error output.
    SetErrorFilter("timeout")

    // Position channel subscription information
    var posSubscribe = {
        "op": "subscribe",
        "args": [{
            "channel": "positions",
            "instType": "ANY"
        }]
    }

    var payload = JSON.stringify(getLogin(accessKey, secretKey, passphrase))
    client_private = Dial("wss://ws.okex.com:8443/ws/v5/private|reconnect=true&payload=" + payload)
    Sleep(3000) // When logging in, you cannot subscribe to the private channel immediately and need to wait for the server response.
    if (client_private) {
        client_private.write(JSON.stringify(posSubscribe))
        var lastPingTS = new Date().getTime()
        while (true) {
            var buf = client_private.read(2000)
            if (buf) {
                Log(buf)
            }
            // Send heartbeat packet
            var nowPingTS = new Date().getTime()
            if (nowPingTS - lastPingTS > 10 * 1000) {
                client_private.write("ping")
                lastPingTS = nowPingTS
            }
        }
    }
}

function onexit() {
    var ret = client_private.close()
    Log("Close the connection!", ret)
}
```

> Detail

https://www.fmz.com/strategy/313116

> Last Modified

2021-09-03 11:49:54