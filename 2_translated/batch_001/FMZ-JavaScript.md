---
> Name

FMZ Tutorial - JavaScript Quick Reference Guide

> Author

Author: TradeMan

---

> Source (javascript)

``` javascript
// The `console.log` in the text can be replaced with a Log function for FMZ debugging.
// Comments are similar to C, this is a single-line comment.
/* This is a
   multi-line
   comment */

// Statements can end with a semicolon
doStuff();

// ... but semicolons can also be omitted; they will be inserted at the start of each new line (except in some special cases).
doStuff()

// Semicolons are retained for those special cases to avoid unexpected results.

///////////////////////////////////
// 1. Numbers, Strings, and Operators

// JavaScript has only one numeric type: double-precision IEEE 754 floating-point.
// Doubles have 52 bits of mantissa precision, sufficient to store integers up to 9✕10¹⁵ precisely.
3; // = 3
1.5; // = 1.5

// Basic arithmetic operations behave as expected.
1 + 1; // = 2
0.1 + 0.2; // = 0.30000000000000004
8 - 1; // = 7
10 * 2; // = 20
35 / 5; // = 7

// Division that does not yield an integer produces a floating-point result.
5 / 2; // = 2.5

// Bitwise operations work the same as in other languages, though when operating on floating point numbers,
// they are converted to *at most* 32-bit unsigned integers.
1 << 2; // = 4

// Parentheses can decide precedence.
(1 + 3) * 2; // = 8

// There are three non-numeric numeric types:
Infinity; // The result of 1/0
-Infinity; // The result of -1/0
NaN; // The result of 0/0

// There are also boolean values.
true;
false;

// Strings can be constructed using single or double quotes.
'abc';
"Hello, world";

// `!` is used to negate.
!true; // = false
!false; // = true

// Equality `===`
1 === 1; // = true
2 === 1; // = false

// Inequality `!=`
1 !== 1; // = false
2 !== 1; // = true

// More comparison operators 
1 < 10; // = true
1 > 10; // = false
2 <= 2; // = true
2 >= 2; // = true

// Strings can be concatenated with `+`.
"Hello " + "world!"; // = "Hello world!"

// Strings can also be compared using < and >
"a" < "b"; // = true

// When comparing with `==`, type conversion may occur...
"5" == 5; // = true
null == undefined; // = true

// ... unless you use `===`
"5" === 5; // = false
null === undefined; // = false 

// This can lead to unexpected behavior.
13 + !0; // 14
"13" + !0; // '13true'

// You can use `charAt` to get a character from a string.
"This is a string".charAt(0);  // = 'T'

// ... or use `substring` to get larger parts.
"Hello world".substring(0, 5); // = "Hello"

// The length of a string is an attribute, so do not use `.` for it.
"Hello".length; // = 5

// There are two special values: `null` and `undefined`.
null;      // Used to represent explicitly undefined values
undefined; // Represents values that have never been set (despite `undefined` itself being a value)

// false, null, undefined, NaN, 0, and "" are falsy; everything else is truthy.
// Note that 0 is considered falsy while "0" is truthy, even though 0 == "0".

///////////////////////////////////
// 2. Variables, Arrays, and Objects

// Variables must be declared with the `var` keyword. JavaScript is a dynamically typed language,
// so you do not need to specify types. Assignment uses `=`.
var someVar = 5;

// If you declare a variable without using the `var` keyword, no error will occur...
someOtherVar = 10;

// ... but this will create the variable in the global scope rather than the current scope.

// Unassigned variables are set to `undefined`.
var someThirdVar; // = undefined

// There are shorthand ways for doing math with variables:
someVar += 5; // equivalent to `someVar = someVar + 5`, now `someVar` is 10
someVar *= 10; // now `someVar` is 100

// Increment and decrement also have shorthands.
someVar++; // now `someVar` is 101
someVar--; // back to 100

// Arrays are ordered lists of arbitrary types.
var myArray = ["Hello", 45, true];

// Array elements can be accessed using bracket notation. Indexing starts at 0.
myArray[1]; // = 45

// Arrays are mutable and have a `length` property.
myArray.push("World");
myArray.length; // = 4

// Elements can be added or modified by index.
myArray[3] = "Hello";

// In JavaScript, objects act as dictionaries or maps: unordered collections of key-value pairs.
var myObj = {key1: "Hello", key2: "World"};

// Keys are strings, but they do not need to be quoted if the name is a valid JavaScript identifier.
// Values can be any type.
var myObj = {myKey: "myValue", "my other key": 4};

// Object properties can be accessed using bracket notation
myObj["my other key"]; // = 4

// ... or with `.` if the property name is a valid identifier.
myObj.myKey; // = "myValue"

// Objects are mutable; values can be changed or new keys added.
myObj.myThirdKey = true;

// If you try to access an undefined value, it will return `undefined`.
myObj.myFourthKey; // = undefined

///////////////////////////////////
// 3. Logic and Control Structures

// The syntax in this section is almost identical to Java's.

// An `if` statement.
if (true) {
    var i = 5;
}
i; // = 5 - unlike in other languages, we do not get `undefined`.

// This leads to the common "immediately-invoked function expression" pattern,
// which avoids polluting the global scope with temporary variables.
(function(){
    var temporary = 5;
    // We can access and modify the global object (the "global object") through `window` in web browsers, or a different name in other environments like Node.js.
    window.permanent = 10;
})();
temporary; // throws a reference error
permanent; // = 10

// One of JavaScript's most powerful features is closures.
// If a function is defined inside another function, the inner function retains access to all variables of its outer parent even after the outer function has finished executing.
function sayHelloInFiveSeconds(name) {
    var prompt = "Hello, " + name + "!";
    // The inner function defaults to having local scope,
    // just like a `var` declaration would create it.
    function inner() {
        alert(prompt);
    }
    setTimeout(inner, 5000);
    // `setTimeout` is asynchronous so the parent function `sayHelloInFiveSeconds` returns immediately,
    // while `setTimeout` will call `inner` later on.
    // However, since `inner` was "closed over" by `sayHelloInFiveSeconds`,
    // it still has access to the `prompt` variable when called eventually.
}
sayHelloInFiveSeconds("Adam"); // alerts "Hello, Adam!" after 5 seconds

///////////////////////////////////
// 4. Objects, Constructors, and Prototypes

// Objects can contain methods.
var myObj = {
    myFunc: function(){
        return "Hello world!";
    }
};
myObj.myFunc(); // = "Hello world!"

// When a method in an object is called, it has access to its parent object through the `this` keyword.
myObj = {
    myString: "Hello world!",
    myFunc: function(){
        return this.myString;
    }
};
myObj.myFunc(); // = "Hello world!"

// However, it actually accesses the runtime context rather than the definition context.

```