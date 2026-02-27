> Name

Uniswap-V3-Trade-Template for Trading Library

> Author

InventorQuantitative

> Strategy Description

The Inventor Platform officially supports web3 contract interaction and calls. This template is a trading library based on Uniswap V3, allowing developers to easily integrate with other DeFi exchanges.

Here are some example function calls. Detailed documentation will be merged into the platform API documents after completion; these examples provide a starting point.


For calling contracts that follow standard ERC20 methods, there's no need to register them and they can be directly invoked. The third parameter has strong compatibility and can include method names or method IDs such as `"0x571ac8b0"` or the full standard method name.
Constant properties return function results directly; non-constant functions like `approve` return the txid after broadcasting:
```
exchange.IO("api", tokenAddress, "decimals")
exchange.IO("api", tokenAddress, "approve", 0x......., "0xfffffffffffff")
exchange.IO("api", tokenAddress, "approve(address,uint256)", 0x......., "0xfffffffffffff")
```

For calling non-standard contract methods, you need to register the ABI content as shown in this template code example. After registration, you can call other functions of the contract:
```
exchange.IO("abi", tokenAddress, abiContent)
```

To get the ABI content of a contract, use the following URL and only take the `result` field:

```
https://api.etherscan.io/api?module=contract&action=getabi&address=0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45
```

If the method is `payable`, you need to add the amount of ETH to be transferred as the fourth parameter, such as 123 in the example function. You can also pass a string representation of the number.

```
exchange.IO("api", ContractV3SwapRouterV2, "multicall(uint256,bytes[])", 123, (new Date().getTime() / 1000) + 3600, "")
```

You can also specify additional parameters for `gasLimit`, `gasPrice`, or `nonce`:

```
exchange.IO("api", ContractV3SwapRouterV2, "multicall(uint256,bytes[])", ..., {gasPrice: 123456, gasLimit: 21000})
```

If the second parameter of IO is `eth`, it directly invokes all available RPC methods on the node server. For example:

```
exchange.IO("api", "eth", "eth_getBalance", self.walletAddress, "latest")
```

> To facilitate transfers, an additional `send` function for sending ETH has been added.

```
exchange.IO("api", "eth", "send", toAddress, toAmount)
```

> Provided are `encode`/`encodePacked` and `decode` methods that can encode function calls into hex string format. You can read the documentation in this template code for an example of calling uniswap v3's multicall.

```javascript
// Can encode with tuple
let types = "tuple(a uint256,b uint8,c address),bytes"
let ret = exchange.IO("encode", types, {
    a: 30,
    b: 20,
    c: "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
}, "0011")
Log("encode: ", ret)
// Decode tuple
Log("decode:", exchange.IO("decode", types, ret))

// Join packed types
let path = exchange.IO("encodePacked", "address,uint24,address", tokenAddressMap['1INCH'], 3000, tokenAddressMap['USDT'])
// Pack method call
let rawData = exchange.IO("encode", ContractV3SwapRouterV2, "checkOracleSlippage(bytes,uint24,uint32)", path, 10000, 600)
// Parse ABI raw data
Log("method hash:", rawData.slice(0, 8))
```

> You can switch keys at any time to operate on multiple addresses, as follows:

```
exchange.IO("key", "219103fb1e058720b8431580cdc61ed77a270bac1f87503145b9e9b5cd8a92ce")
```

> Rules for ABI internal variable conversion

- `address`: String starting with "0x"
- `bytes`: Hex-encoded string, e.g., `"008395"`
- `uint256`: Can be a string or number, such as `"0x12345"` or `123`
- `tuple`: Pass in the structure directly, like `{path: "", amountIn: 0x123}`
- Other types are passed directly.

> Uniswap Template Call Example

Add web3 exchange, fill node address and private key. The private key can be saved locally (private key as file path). See API documentation for details:

Node addresses can use Infura's free nodes after applying with your own key: https://mainnet.infura.io/v3/{apikey}

```javascript
$.testUniswap = function() {
    let ex = $.NewUniswapV3()
    Log("walletAddress: ", ex.walletAddress)
    let tokenAddressMap = {
        "ETH": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", // WETH
        "USDT": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "1INCH": "0x111111111117dC0aa78b770fA6A738034120C302",
    }
    for (let name in tokenAddressMap) {
        ex.addToken(name, tokenAddressMap[name])
    }

    Log(ex.getPrice('ETH_USDT'))
    Log(ex.getPrice('1INCH_USDT'))
    // Swap 0.01 ETH to USDT
    Log(ex.swapToken('ETH', 0.01, 'USDT'))
    let usdtBalance = ex.balanceOf('USDT')
    Log("balance of USDT", usdtBalance)
    // Swap USDT to DAI then to ETH
    Log(ex.swapToken('USDT', usdtBalance, 'DAI,ETH'))

    Log("balance of ETH", ex.getETHBalance())

    // Log(ex.sendETH('0x11111', 0.02))
}
```

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|ChainType|0|ChainType: Default|Ethereum|Arbitrum|Optimism|Avalanche|Polygon|Celo|
|AutoFetchTokens|false|AutoFetchTokens|

> Source (javascript)

```javascript
/* jshint esversion: 7 */

const ABI_Route = '[{"inputs":[{"internalType":"address","name":"_factoryV2","type":"address"},{"internalType":"address","name":"factoryV3","type":"address"},{"internalType":"address","name":"_positionManager","type":"address"},{"internalType":"address","name":"_WETH9","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"approveMax","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"approveMaxMinusOne","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"approveZeroThenMax","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"approveZeroThenMaxMinusOne","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],"name":"checkOracleSlippage","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"uint24","name":"maximumTickDivergence","type":"uint256"},{"internalType":"uint32","name":"secondsAgo","type":"uint256"}],"name":"checkOracleSlippage","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum",