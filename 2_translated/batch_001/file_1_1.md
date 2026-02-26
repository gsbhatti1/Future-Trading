Name

Interactive Template

Author

Inventor Quantification-Little Dream

Strategy Description

- Test Code

```
// test code
function main() {
$.BindingFunc("test1", function(cmd, param){ // Bind the button with the control name test1, function(cmd, param){...} is the response function of the button, the first parameter of the response function is the name of the control that triggers the response function: test1
var ticker = exchange.GetTicker() // The second param parameter is the parameter that comes when the control is clicked (numeric type, string type, Boolean type, and drop-down box all have parameters, but the button type does not have parameters)
Log("Control:", cmd, "ticker:", ticker, "Parameter:", param)
})
$.BindingFunc("test3", function(cmd, param){ // Bind test3 ...
var account = exchange.GetAccount()
Log("account:", account, "cmd:", cmd, "param:", param)
})
$.BindingFunc("test5", function(){ // Bind test5 ...
Log(exchange.GetName())
})
while(1){
$.GetCommand() // Detect interactive commands in the main loop.
Sleep(2000)
}
}
```

- Interface Functions

- Control Response Function Binding
$.BindingFunc(cmdControlName, function(cmd, param){...})

- Interactive Command Detection Function
Replaces Platform API GetCommand() function
$.GetCommand()

- Screenshot of the control configured by the test code
![IMG](https://www.fmz.com/upload/asset/166da027c40813fe1311.png)

- If you have any questions, please ask and leave a message.


Source (javascript)

``` javascript
var _CmdMap = {}

$.BindingFunc = function(cmdName, cmdFunc) {
_CmdMap[cmdName] = cmdFunc
}

$.GetCommand = function() {
var cmd = GetCommand()
if(cmd) {
strArr = cmd.split(":")
func = _CmdMap[strArr[0]]
if(strArr.length == 1) {
//Call the response function corresponding to the command
if(func) {
func(strArr[0])
}
} else if(strArr.length == 2) {
//Call the response function corresponding to the command
if(func) {
func(strArr[0], strArr[1])
}
} else {
var param = strArr[1]
for(var i = 2; i < strArr.length; i++) {
param += (":" + strArr[i])
}

//Call the response function corresponding to the command
if(func) {
func(strArr[0], param)
}
}
if(!func) {
Log(strArr[0], "This command does not register a response function.", "#FF0000")
}
}
}

// test code
function main() {
$.BindingFunc("test1", function(cmd, param){ // Bind the button with the control name test1, function(cmd, param){...} is the response function of the button, the first parameter of the response function is the name of the control that triggers the response function: test1
var ticker = exchange.GetTicker() // The second param parameter is the parameter that comes when the control is clicked (numeric type, string type, Boolean type, and drop-down box all have parameters, but the button type does not have parameters)
Log("Control:", cmd, "ticker:", ticker, "Parameter:", param)
})
$.BindingFunc("test3", function(cmd, param){ // Bind test3 ...
var account = exchange.GetAccount()
Log("account:", account, "cmd:", cmd, "param:", param)
})
$.BindingFunc("test5", function(){ // Bind test5 ...
Log(exchange.GetName())
})
while(1){
$.GetCommand() // Detect interactive commands in the main loop.
Sleep(2000)
}
}
```

Detail

https://www.fmz.com/strategy/137403

Last Modified

2019-02-15 11:49:52