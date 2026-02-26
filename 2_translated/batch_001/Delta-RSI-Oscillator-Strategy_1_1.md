``` pinescript
/*backtest
start: 2022-04-29 00:00:00
end: 2022-05-28 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © tbiktag
//
// Delta-RSI Oscillator Strategy
//
// A strategy that uses Delta-RSI Oscillator (© tbiktag) as a stand-alone indicator:
// https://www.tradingview.com/script/OXQVFTQD-Delta-RSI-Oscillator/
//
// The Delta-RSI represents a smoothed time derivative of the RSI, plotted as a histogram and serves as a momentum indicator.
// 
// Strategy Arguments:

| Argument       | Default | Description                                                                                                                                                                                                                                                                                                                                 |
| -------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v_input_1      | 2       | (Model Parameters:) Polynomial Order                                                                                                                                                                                                                                                                                                         |
| v_input_2      | 21      | RSI Length                                                                                                                                                                                                                                                                                                                             |
| v_input_3      | 21      | Length (> Order)                                                                                                                                                                                                                                                                                                                        |
| v_input_4      | 9       | Signal Length                                                                                                                                                                                                                                                                                                                         |
| v_input_5      | true    | (Show Signals:) Buy                                                                                                                                                                                                                                                                                                                      |
| v_input_6      | true    | Sell                                                                                                                                                                                                                                                                                                                                |
| v_input_7      | true    | Exit                                                                                                                                                                                                                                                                                                                               |
| v_input_8      | Zero-Crossing  | (Entry and Exit Conditions:) Buy                                                                                                                                                                                                                                                                                                       |
| v_input_9      | Zero-Crossing  | Sell                                                                                                                                                                                                                                                                                                                              |
| v_input_10     | Zero-Crossing  | Exit                                                                                                                                                                                                                                                                                                                             |
| v_input_11     | false    | (Filter by Means of Root-Mean-Square Error of RSI Fitting:) useRmse                                                                                                                                                                                                                                                                    |
| v_input_12     | 10       | RSI fitting Error Threshold, %                                                                                                                                                                                                                                                                                                         |

// ---Subroutines---
matrix_get(_A,_i,_j,_nrows) =>
    // Get the value of an element in a pseudo 2D matrix
    // input: 
    // _A :: array: pseudo 2d matrix _A = [[column_0],[column_1],...,[column_(n-1)]]
    // _i :: integer: row number
    // _j :: integer: column number
    // _nrows :: integer: number of rows in the implied 2d matrix
    array.get(_A,_i+_nrows*_j)

matrix_set(_A,_value,_i,_j,_nrows) =>
    // Set a value to an element in a pseudo 2D matrix
    // input: 
    // _A :: array, changed on output: pseudo 2d matrix _A = [[column_0],[column_1],...,[column_(n-1)]]
    // _value :: float: the new value to be set
    // _i :: integer: row number
    // _j :: integer: column number
    // _nrows :: integer: number of rows in the implied 2d matrix
    array.set(_A,_i+_nrows*_j,_value)

transpose(_A,_nrows,_ncolumns) =>
    // Transpose a pseudo 2D matrix
    // input:
    // _A :: array: pseudo 2d matrix _A = [[column_0],[column_1],...,[column_(n-1)]]
    // _nrows :: integer: number of rows in _A
    // _ncolumns :: integer: number of columns in _A
    // output:
    // _AT :: array: pseudo 2d matrix with implied dimensions: _ncolumns x _nrows
    var _AT = array.new_float(_nrows*_ncolumns,0)
    for i = 0 to _nrows-1
        for j = 0 to _ncolumns-1
            matrix_set(_AT, matrix_get(_A,i,j,_nrows),j,i,_ncolumns)
    _AT

multiply(_A,_B,_nrowsA,_ncolumnsA,_ncolumnsB) => 
    // Calculate scalar product of two matrices
    // input: 
    // _A :: array: pseudo 2d matrix
    // _B :: array: pseudo 2d matrix
    // _nrowsA :: integer: number of rows in _A
    // _ncolumnsA :: integer: number of columns in _A
    // _ncolumnsB :: integer: number of columns in _B
    // output:
    // _C:: array: pseudo 2d matrix with implied dimensions _nrowsA x _ncolumnsB
    var _C = array.new_float(_nrowsA*_ncolumnsB,0)
    int _nrowsB = _ncolumnsA
    float elementC= 0.0
    for i = 0 to _nrowsA-1
        for j = 0 to _ncolumnsB-1
            elementC := 0
            for k = 0 to _ncolumnsA-1
                elementC := elementC + matrix_get(_A,i,k,_nrowsA)*matrix_get(_B,k,j,_nrowsB)
            matrix_set(_C,elementC,i,j,_nrowsA)
    _C

vnorm(_X,_n) =>
    // Square norm of vector _X with size _n
    float _norm = 0.0
    for i = 0 to _n-1
        _norm := _norm + pow(array.get(_X,i),2)
    sqrt(_norm)

qr_diag(_A,_nrows,_ncolumns) => 
    // QR Decomposition with Modified Gram-Schmidt Algorithm (Column-Oriented)
    // input:
    // _A :: array: pseudo 2d matrix _A = [[column_0],[column_1],...,[column_(n-1)]]
    // _nrows :: integer: number of rows in _A
    // _ncolumns :: integer: number of columns in _A
    // output:
    // _Q: unitary matrix, implied dimensions

```