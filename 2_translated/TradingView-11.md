``` javascript

/*
Order Robot 1.1
Version: 1.1
Author: summer
Date: 2021.9.9
New Features:
1. Multi-account with different order sizes
2. Opponent limit sliding price for closing positions (Market orders are still used for closing)
3. Seasonal contract backtest statistics
4. Statistics of profit and loss across multiple accounts
5. Localized account data storage
6. Status information table display
7. Multi-threaded order placement
8. Additional interactive features for manual orders
9. Fixed an error in profit calculation
*/

// Order settings
var _PricePrecision = PricePrecision;                           // Price precision for placing orders
var _AmountPrecision = AmountPrecision;                         // Quantity precision for placing orders
var _OneSizeInCurrentCoin = OneSizeInCurrentCoin;               // Number of coins represented by one contract in U-asset contracts
var _QuarterOneSizeValue = QuarterOneSizeValue;                 // Number of USDT represented by one contract in coin-based contracts

// Auto transfer settings
var _UseAutoTransfer = UseAutoTransfer;                         // Whether to use auto transfer
var _UseCertainAmountTransfer = UseCertainAmountTransfer;       // Fixed amount transfer
var _AccountMaxBalance = AccountMaxBalance;                     // Transfer 100 U when available assets exceed this value
var _UseProfitToTransfer = UseProfitToTransfer;                 // Transfer based on profit (double the transfer for profits)
var _ProfitPercentToTransfer = ProfitPercentToTransfer;         // Percentage of profit to transfer

var _OKCoin = "Futures_OKCoin";
var _QuantitativeOrderHeader = "Quantitative:order:";
var _OrderSize = [];
var _InitAsset = [];
var _Accounts = [];
var _Positions = [];

var ProfitLocal = [];
var TotalAsset = [];
var TakeProfitCount = [];
var StopLossCount = [];
var WinRate = [];
var MaxLoss = [];
var MaxLossPercent = [];
var MaxProfit = [];
var MaxProfitPercent = [];
var ProfitPercent = [];
var _TransferAmount = [];
var _CurrentInitAssets = [];
var UserStartTime = [];
var UserDatas = [];
var StrategyRunTimeStampString = "strategy_run_time";
var StrategyDatas = { start_run_timestamp: 0, others: "" };

var _ClosePrice = 0;
var _MarginLevel = MarginLevel;

var _TradingFee = 0.0005;
var _RemainingSize = 20;            // In all-asset mode, the number of contracts that need to be reserved to avoid failed orders due to price fluctuations
var _IsOpponentOrder = false;

var _LogStatusRefreshTime = 10;     // Status bar update cycle in seconds
var _LastBarTime = 0;               // Latest bar time

// Save the start run timestamp of the strategy, in seconds since epoch
function saveStrategyRunTime() {
    var local_data_strategy_run_time = _G(StrategyRunTimeStampString);

    if (local_data_strategy_run_time == null) {
        StrategyDatas.start_run_timestamp = Unix();
        _G(StrategyRunTimeStampString, StrategyDatas.start_run_timestamp);
    }
    else {
        StrategyDatas.start_run_timestamp = local_data_strategy_run_time;
    }
}

// Set the start run timestamp of the strategy, in seconds since epoch
function setStrategyRunTime(timestamp) {
    _G(StrategyRunTimeStampString, timestamp);
    StrategyDatas.start_run_timestamp = timestamp;
}

// Calculate the number of days between two timestamps, both in seconds
function getDaysFromTimeStamp(start_time, end_time) {
    if (end_time < start_time)
        return 0;

    return Math.trunc((end_time - start_time) / (60 * 60 * 24));
}

function saveUserDatasLocal() {
    // Save trading statistics to local storage when the interactive button is clicked
    // Clear UserData data before saving
    UserDatas = null;
    UserDatas = [];

    for (var i = 0; i < exchanges.length; i++) {
        // Add data to UserData
        UserDatas.push({
            init_assets: _InitAsset[i],
            profit_local: ProfitLocal[i],
            max_profit_percent: MaxProfitPercent[i],
            max_loss_percent: MaxLossPercent[i],
            max_profit: MaxProfit[i],
            max_loss: MaxLoss[i],
            take_profit_count: TakeProfitCount[i],
            stop_loss_count: StopLossCount[i],
            start_time: UserStartTime[i],
            order_size: _OrderSize[i],
            transfer_amount: _TransferAmount[i],
            current_init_assets: _CurrentInitAssets[i]
        });
        // Save to local storage
        _G(exchanges[i].GetLabel(), UserDatas[i]);
    }
    Log("All account data has been saved locally.");
}

function readUserDataLocal() {
    // Read user data from local storage, not completed in this snippet
}