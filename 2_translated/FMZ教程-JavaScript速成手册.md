> Name

FMZ Tutorial - JavaScript Quick Start Guide

> Author

Author: TradeMan

---

> Source (javascript)

``` javascript
// The `console.log` in FMZ debugging can be replaced with Log functions.
// Comments are similar to C, this is a single-line comment.
/* This is a multi-line
   comment */

// Statements can end with a semicolon.
doStuff();

// However, semicolons can also be omitted as they are automatically inserted at the beginning of new lines (except in some special cases).
doStuff()

// Semicolons must be retained due to unexpected results caused by these special cases.

///////////////////////////////////
// 1. Numbers, Strings and Operators

// JavaScript has only one numeric type: double-precision floating-point number (64-bit IEEE 754).
// Doubles have 52 bits of mantissa, which can precisely represent integers up to 9✕10¹⁵.
3; // = 3
1.5; // = 1.5

// Basic arithmetic operations behave as expected.
1 + 1; // = 2
0.1 + 0.2; // = 0.30000000000000004
8 - 1; // = 7
10 * 2; // = 20
35 / 5; // = 7

// Division results in a floating-point number, including non-integer divisions.
5 / 2; // = 2.5

// Bitwise operations are the same as in other languages; when bitwise operators are applied to floats,
// they get converted to *at most* 32-bit unsigned integers.
1 << 2; // = 4

// Parentheses can determine precedence.
(1 + 3) * 2; // = 8

// There are three non-numeric number types:
Infinity; // Result of 1/0
-Infinity; // Result of -1/0
NaN; // Result of 0/0

// There are also Boolean values.
true;
false;

// Strings can be constructed with single or double quotes.
'abc';
"Hello, world";

// The `!` operator is used for logical NOT.
!true; // = false
!false; // = true

// Equality ===
1 === 1; // = true
2 === 1; // = false

// Inequality !=
1 !== 1; // = false
2 !== 1; // = true

// More comparison operators
1 < 10; // = true
1 > 10; // = false
2 <= 2; // = true
2 >= 2; // = true

// Strings are concatenated using `+`.
"Hello " + "world!"; // = "Hello world!"

// Strings can also be compared with < and >
"a" < "b"; // = true

// The equality operator `==` performs type coercion...
"5" == 5; // = true
null == undefined; // = true

// ...unless you use ===.
"5" === 5; // = false
null === undefined; // = false 

// This can lead to unexpected results.
13 + !0; // 14
"13" + !0; // '13true'

// You can get characters from a string using `charAt`.
"This is a string".charAt(0);  // = 'T'

// ...or use `substring` for larger parts.
"Hello world".substring(0, 5); // = "Hello"

// The `length` property of a string does not require parentheses.
"Hello".length; // = 5

// There are two special values: `null` and `undefined`.
null;      // Represents a deliberately set empty value
undefined; // Represents an unset value (although undefined itself is actually a value)

// false, null, undefined, NaN, 0 and "" are falsy; everything else is truthy.
// Note that 0 is falsy while "0" is truthy, despite the fact that 0 == "0".

///////////////////////////////////
// 2. Variables, Arrays, and Objects

// Variables must be declared with the `var` keyword in JavaScript, which is a dynamically typed language,
// so you don't need to specify types. Assignments use `=`.
var someVar = 5;

// If you declare a variable without using `var`, it won't give an error...
someOtherVar = 10;

// ...but the variable will be created in the global scope, rather than the current scope.

// Uninitialized variables are set to undefined.
var someThirdVar; // = undefined

// There are shorthand ways for performing arithmetic operations on a variable:
someVar += 5; // Equivalent to `someVar = someVar + 5`. Now someVar is 10
someVar *= 10; // Now someVar is 100

// Increment and decrement have their own short forms.
someVar++; // Now someVar is 101
someVar--; // Back to 100

// Arrays are ordered lists of arbitrary types.
var myArray = ["Hello", 45, true];

// Array elements can be accessed using square bracket indices. Array indices start from 0.
myArray[1]; // = 45

// Arrays can change and have a `length` property.
myArray.push("World");
myArray.length; // = 4

// Elements can also be added or modified at specific indices.
myArray[3] = "Hello";

// JavaScript objects are equivalent to dictionaries or maps in other languages: they are unordered collections of key-value pairs.
var myObj = {key1: "Hello", key2: "World"};

// Keys are strings, but the quotes can be omitted if they form valid JS identifiers.
// Values can be any type.
var myObj = {myKey: "myValue", "my other key": 4};

// Object properties can be accessed using square brackets or dot notation.
// Dot notation is used when the property name forms a valid identifier.
myObj["my other key"]; // = 4
myObj.myKey; // = "myValue"

// Objects are mutable, so values can also be changed or new keys added.
myObj.myThirdKey = true;

// Trying to get an undefined value will return `undefined`.
myObj.myFourthKey; // = undefined

///////////////////////////////////
// 3. Logic and Control Structures

// The syntax for this section is almost the same as Java's.

// `if` statements work as in other languages.
var count = 1;
if (count == 3){
    // Code block
}
else {
    // Alternative code block
}

// Semicolons are automatically inserted at the beginning of new lines, so omitting them is fine.
if (count == 3) {
    var i = 5; // Semicolon omitted

} else {
    // Code block
}

// setTimeout is not part of JavaScript but provided by browsers and Node.js.
setTimeout(myFunction, 5000);

// Functions can be passed as arguments directly without naming them — you can define a function in the parameter list.
setTimeout(function(){
    // This code will be called after 5 seconds.
}, 5000);

// JavaScript has lexical scope; functions have their own scope while other code blocks do not.
if (true){
    var i = 5;
}
i; // = 5 - Unlike in other languages, this does not return `undefined`.

// This leads to the common pattern of "immediately-invoked function expressions" (IIFE) to avoid polluting the global scope with temporary variables.
(function(){
    var temporary = 5;
    // We can access and modify the global object ("global object") to reach the global scope, which is `window` in web browsers. 
    // In other environments like Node.js, this object might have a different name.
    window.permanent = 10;
})();
temporary; // Throws ReferenceError
permanent; // = 10

// One of JavaScript's most powerful features is closures.
// If a function is defined inside another function, the inner function has access to all variables in the outer function even after the outer function ends.
function sayHelloInFiveSeconds(name){
    var prompt = "Hello, " + name + "!";
    // Inner functions are by default local, just like with `var`.
    function inner(){
        alert(prompt);
    }
    setTimeout(inner, 5000);
    // setTimeout is asynchronous, so the outer function exits immediately,
    // while setTimeout calls inner after a delay.
    // However, since inner is "closed over" by sayHelloInFiveSeconds,
    // it can still access the `prompt` variable when called later.
}
sayHelloInFiveSeconds("Adam"); // A message box with "Hello, Adam!" will appear after 5 seconds.

///////////////////////////////////
// 4. Objects, Constructors and Prototypes

// Objects can contain methods.
var myObj = {
    myFunc: function(){
        return "Hello world!";
    }
};
myObj.myFunc(); // = "Hello world!"

// When a method of an object is called, the `this` keyword allows access to its dependent object.
myObj = {
    myString: "Hello world!",
    myFunc: function(){
        return this.myString;
    }
};
myObj.myFunc(); // = "Hello world!"

// However, it actually refers to its runtime context rather than its definition context.
```