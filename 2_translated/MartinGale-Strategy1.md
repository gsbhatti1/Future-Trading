Name

MartinGale-Strategy1

Author

Zer3192

Source (javascript)

``` javascript
// Example of implementing Martingale on the FMZ platform
function main() {
    // Set basic parameters
    var initAsset = 1000000; // Initial asset
    var baseBet = 0.001; // Basic unit price
    var profitRate = 0.2; // Raising ratio when making profit
    var lossRate = 0.5; // Raising ratio when losing money
    var maxBetTimes = 10; // Maximum number of raises
    var maxLoseTimes = 4; // Number of consecutive losses

    // Initialization parameters
    var asset = initAsset; // Current asset
    var bet = baseBet; // Current single bet
    var betTimes = 0; // Current number of bets
    var loseTimes = 5; // Current number of consecutive losses
    var win = 0; // The current number of consecutive wins

    // Order function
    function placeOrder(direction) {
        var amount = bet; // Order amount
        if (direction == "buy") {
            // Buy
            exchange.Buy(-1, bet);
            Log("buy", bet);
        } else if (direction == "sell") {
            // Sell
            exchange.Sell(-1, bet);
            Log("sell", bet);
        }
    }

    // Transaction loop
    while (true) {
        // Get the information on the current K line
        var records = exchange.GetRecords();
        var lastRecord = records[records.length - 1];
        var currPrice = lastRecord.Close;

        // Determine the current trend
        var trend = "none";
        if (lastRecord.Open < lastRecord.Close) {
            trend = "up";
        } else if (lastRecord.Open > lastRecord.Close) {
            trend = "down";
        }

        // Execute trades based on trends
        if (trend == "up") {
            // If rising
            if (loseTimes > 0) {
                // If there was a loss before, reset the number of raises and the number of consecutive losses
                betTimes = 0;
                loseTimes = 0;
            }
            placeOrder("buy");

            win++;
            if (win == maxBetTimes) {
                // If the number of consecutive wins reaches the maximum number of raises, reset
                betTimes = 0;
                win = 0;
            }
        } else if (trend == "down") {
            // If dropped
            if (win > 0) {
                // If there was a previous win, reset the number of raises
                betTimes = 0;
            }
            if (loseTimes == maxLoseTimes) {
                // If the number of consecutive losses reaches the maximum number, stop trading
                break;
            }
            if (betTimes == 0) {
                // If it is the first time to raise, calculate the amount of the raise
                bet *= (1 + lossRate);
            } else {
                // If it is not the first time to raise, calculate the amount of raise
                bet *= 1.1;
            }
            placeOrder("sell");
            loseTimes++;
            betTimes++;
        }

        // Update assets
        var currAsset = exchange.GetAccount().Balance;
        if (currAsset > asset) {
            // Profit, raise
            bet *= (1 + profitRate);
        }
        asset = currAsset;

        // Wait for next transaction
        Sleep(1000);
    }
}
```

Detail

https://www.fmz.com/strategy/416875

Last Modified

2023-07-12 17:41:56