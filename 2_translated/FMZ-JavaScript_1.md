> Name

FMZ Tutorial - JavaScript Quick Start Guide

> Author

TradeMan Craftsmanship


> Source (javascript)

``` javascript
// The console.log in FMZ can be replaced with Log functions during debugging.
// Comments are similar to C; this is a single-line comment.
/* This is a multi-line
   comment. */

// Statements can end with a semicolon, but they can also omit it as a new line automatically inserts a semicolon (except in some special cases).
doStuff();

// In those special cases where automatic semicolon insertion results in unexpected outcomes, we keep the semicolon.
///////////////////////////////////
// 1. Numbers, Strings, and Operators

// JavaScript has only one numeric type: double-precision IEEE 754 floating point.
// A double can represent an integer up to 9✕10¹⁵ precisely with its 52-bit exponent.
3; // = 3
1.5; // = 1.5

// Basic arithmetic operations work as expected.
1 + 1; // = 2
0.1 + 0.2; // = 0.30000000000000004
8 - 1; // = 7
10 * 2; // = 20
35 / 5; // = 7

// Including non-integer divisions.
5 / 2; // = 2.5

// Bitwise operations are similar to other languages, and when a floating-point number is used in bitwise operations,
// the number will be converted to an unsigned integer of at most 32 bits.
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

// The exclamation mark (!) is used for negation.
!true; // = false
!false; // = true

// Equality (===)
1 === 1; // = true
2 === 1; // = false

// Inequality (!=)
1 !== 1; // = false
2 !== 1; // = true

// More comparison operators.
1 < 10; // = true
1 > 10; // = false
2 <= 2; // = true
2 >= 2; // = true

// Strings are concatenated using +
"Hello " + "world!"; // = "Hello world!"

// Strings can also be compared with < and >
"a" < "b"; // = true

// Using == for comparison performs type conversion...
"5" == 5; // = true
null == undefined; // = true

// ...unless you use ===.
"5" === 5; // = false
null === undefined; // = false 

// ...which can result in unexpected behavior.
13 + !0; // 14
"13" + !0; // '13true'

// You can use charAt to get a character from a string.
"This is a string".charAt(0);  // = 'T'

// ...or use substring to get larger portions.
"Hello world".substring(0, 5); // = "Hello"

// length is a property, so do not use ().
"Hello".length; // = 5

// There are two special values: null and undefined.
null;      // used for explicitly set empty values
undefined; // used for values that have not been set yet (despite undefined itself being a value)

// false, null, undefined, NaN, 0, and "" are all falsy; everything else is truthy.
// Note that 0 is false while "0" is true, even though 0 == "0".

///////////////////////////////////
// 2. Variables, Arrays, and Objects

// Variables need to be declared using the var keyword. JavaScript is a dynamically typed language,
// so you do not have to specify types. Assignment uses =.
var someVar = 5;

// If you declare a variable without the var keyword, no error will be thrown...
someOtherVar = 10;

// ...but this will create a global variable rather than in the current scope.

// Uninitialized variables are set to undefined.
var someThirdVar; // = undefined

// Mathematical operations on variables have shorthand:
someVar += 5; // equivalent to someVar = someVar + 5; now someVar is 10
someVar *= 10; // now someVar is 100

// Increment and decrement also have shorthand.
someVar++; // now someVar is 101
someVar--; // back to 100

// Arrays are ordered lists of any type.
var myArray = ["Hello", 45, true];

// Array elements can be accessed using square bracket notation. Indexing starts at 0.
myArray[1]; // = 45

// Arrays are mutable and have a length property.
myArray.push("World");
myArray.length; // = 4

// You can add or modify values by index.
myArray[3] = "Hello";

// JavaScript objects are similar to other languages' "dictionaries" or "maps": they are unordered collections of key-value pairs.
var myObj = {key1: "Hello", key2: "World"};

// Keys are strings, but you do not need quotes if the key is a valid identifier.
// Values can be any type.
var myObj = {myKey: "myValue", "my other key": 4};

// Object properties can be accessed using square bracket notation:
myObj["my other key"]; // = 4

// ...or with dot notation, if the property is a valid identifier:
myObj.myKey; // = "myValue"

// Objects are mutable; values can be changed or new keys added.
myObj.myThirdKey = true;

// If you want to retrieve an undefined value, it will return undefined.
myObj.myFourthKey; // = undefined

///////////////////////////////////
// 3. Logic and Control Structures

// The syntax in this section is almost identical to Java's.

// if statements work as expected:
var count = 1;
if (count == 3){
    // This block runs when count is 3.
} else if (count == 4){
    // This block runs when count is 4.
} else {
    // This block runs otherwise.
}

// setTimeout is not a part of the JavaScript language but provided by browsers and Node.js:
function myFunction() {
    // This code will be called after 5 seconds.
}
setTimeout(myFunction, 5000);

// Function objects do not need to be named - you can define a function directly in another function's parameters:
setTimeout(function(){
    // This code will also be called after 5 seconds.
}, 5000);

// JavaScript has function scope; functions have their own scope while other code blocks do not.
if (true){
    var i = 5;
}
i; // = 5 - unlike in some other languages, this is not undefined.

// This leads to the common pattern of "immediately-invoked function expressions" (IIFE),
// which helps avoid leaking temporary variables into the global scope.
(function(){
    var temporary = 5;
    // We can access and modify the global object ("global object") using `window` in web browsers,
    // or a different name depending on the environment, like Node.js.
    window.permanent = 10;
})();
temporary; // throws ReferenceError
permanent; // = 10

// One of JavaScript's most powerful features is closures.
// If a function is defined inside another function, it has access to all variables in the outer function,
// even after the outer function has ended.
function sayHelloInFiveSeconds(name){
    var prompt = "Hello, " + name + "!";
    // The inner function defaults to being local scope as if declared with `var`.
    function inner(){
        alert(prompt);
    }
    setTimeout(inner, 5000);
    // setTimeout is asynchronous so the outer sayHelloInFiveSeconds will exit immediately,
    // while setTimeout will call inner later.
    // However, since inner was "closed over" by sayHelloInFiveSeconds,
    // it still has access to the `prompt` variable when finally called.
}
sayHelloInFiveSeconds("Adam"); // alerts "Hello, Adam!" after 5 seconds.

///////////////////////////////////
// 4. Objects, Constructors, and Prototypes

// Objects can contain methods:
var myObj = {
    myFunc: function(){
        return "Hello world!";
    }
};
myObj.myFunc(); // = "Hello world!"

// When a method of an object is called, this keyword refers to the object on which it was invoked.
myObj = {
    myString: "Hello world!",
    myFunc: function(){
        return this.myString;
    }
};
myObj.myFunc(); // = "Hello world!"

// But the function accesses its runtime environment rather than the definition context.
```