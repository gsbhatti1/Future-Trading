> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2010|From Year|
|v_input_4|true|To Month|
|v_input_5|true|To Day|
|v_input_6|9999|To Year|
|v_input_7|-10|Target Loss to Average Down (%)|
|v_input_8|10|Target Take Profit|
|v_input_9|50|% Of Current Holdings to Buy|
|v_input_10|20|SMA Period|


> Source (PineScript)

``` pinescript
//@version=3
// ########################################################################## // 
//
// This script is intended to demonstrate how pyramiding can be used to average
// down a position.
//
// We will buy when a stock closes above its 20 day MA and Averag