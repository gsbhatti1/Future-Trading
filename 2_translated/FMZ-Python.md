``` python
# Single-line comments are denoted by the # symbol.
""" Multi-line strings can be enclosed in triple quotes,
   but they can also serve as multi-line comments. """

####################################################
## 1. Basic Data Types and Operators
####################################################

# Numeric types
3           # => 3

# Simple arithmetic operations
1 + 1        # => 2
8 - 1        # => 7
10 * 2       # => 20
35 / 5       # => 7

# Integer division automatically truncates the result.
5 / 2        # => 2

# To perform exact division, we need to use floating-point numbers.
2.0          # A float
11.0 / 4.0   # => 2.75 - More precise.

# Parentheses have the highest precedence.
(1 + 3) * 2  # => 8

# Boolean values are also basic data types.
True
False

# Use `not` to negate a boolean value.
not True     # => False
not False    # => True

# Equality checks.
1 == 1       # => True
2 == 1       # => False

# Inequality check.
1 != 1       # => False
2 != 1       # => True

# More comparison operators.
1 < 10       # => True
1 > 10       # => False
2 <= 2       # => True
2 >= 2       # => True

# Comparison operations can be chained!
1 < 2 < 3    # => True
2 < 3 < 2    # => False

# Strings are enclosed in double or single quotes.
"This is a string."
'This is also a string.'

# Concatenation of strings using the plus operator.
"Hello " + "world!"   # => "Hello world!"

# Strings can be treated as lists of characters.
"This is a string"[0]  # => 'T'

# `%` can be used to format strings.
"%s can be %s" % ("strings", "interpolated")

# Alternatively, the `format` method can be used for string formatting,
# which is recommended.
"{0} can be {1}".format("strings", "formatted")
# Or using variable names instead of indices:
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# The `None` object represents the absence of a value.
None         # => None

# Do not use the `==` operator when comparing with `None`.
# Use `is` for such comparisons instead.
"etc" is None    # => False
None is None     # => True

# `is` can be used to check object identity.
# This operator has limited utility in comparison of primitive data types but is essential for objects.

# The `None`, `0`, and empty strings are considered false.
# All other values are considered true.
0 == False     # => True
"" == False    # => True


####################################################
## 2. Variables and Collections
####################################################

# Convenient print statement to output information.
print "I'm Python. Nice to meet you!"

# Assigning variables without prior declaration is straightforward.
some_var = 5    # It's generally recommended to use lowercase letters and underscores for variable names.
some_var        # => 5

# Accessing an undefined variable will raise an exception.
# Refer to the error handling section if you want to handle such errors.
some_other_var   # Raises a NameError.

# An `if` statement can be used as an expression.
"yahoo!" if 3 > 2 else 2    # => "yahoo!"

# Lists are used to store sequences.
li = []
# Initialize lists directly.
other_li = [4, 5, 6]

# Add elements to the end of a list.
li.append(1)           # li is now [1]
li.append(2)           # li is now [1, 2]
li.append(4)           # li is now [1, 2, 4]
li.append(3)           # li is now [1, 2, 4, 3]
# Remove the last element from a list.
li.pop()               # => 3; li is now [1, 2, 4]
# Re-add the removed element to the end of the list.
li.append(3)           # li is now [1, 2, 4, 3] again.

# Access elements in a list as you would with an array in other languages.
li[0]                  # => 1
# Access the last element.
li[-1]                 # => 3

# Indexing out of bounds will raise an exception.
li[4]                  # Raises an IndexError

# Slicing syntax can be used to access parts of a list,
# which works like mathematical left-closed, right-open intervals.
li[1:3]                # => [2, 4]
# Omit the start index to slice from the beginning.
li[2:]                 # => [4, 3]
# Omit the end index to slice until the end of the list.
li[:3]                 # => [1, 2, 4]

# Delete a specific element by its index.
del li[2]              # li is now [1, 2, 3]

# Concatenate lists using addition.
li + other_li          # => [1, 2, 3, 4, 5, 6]

# Use `&` to compute the intersection of sets.
other_set = {3, 4, 5, 6}
{1, 2, 3, 4} & other_set     # => {3, 4, 5}

# Use `|` to compute the union of sets.
{1, 2, 3, 4} | other_set     # => {1, 2, 3, 4, 5, 6}

# Use `-` to compute the difference between sets.
{1, 2, 3, 4} - {2, 3, 5}    # => {1, 4}

# Check if an element is in a set using `in`.
2 in filled_set           # => True
10 in filled_set          # => False


####################################################
## 3. Control Flow
####################################################

# Define a variable.
some_var = 5

# This is an `if` statement, indentation is crucial in Python.
# The following code snippet will output "some var is smaller than 10".
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:       # This `elif` clause is optional
    print("some_var is smaller than 10.")
else:                     # This `else` clause is also optional
    print("some_var is indeed 10.")


"""
Use a for loop to iterate over a list.
Outputs:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # Use `%` to format strings.
    print("%s is a mammal" % animal)

"""
The `range(number)` function returns a list of numbers from 0 up to (but not including) the given number.
Outputs:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
A while loop.
Outputs:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # `x = x + 1` is the shorthand for incrementing.

# Use a try/except block to handle exceptions.
try:
    # Use `raise` to throw an exception.
    raise IndexError("This is an index error")
except IndexError as e:
    pass     # Do nothing, but usually you would do some recovery here.


####################################################
## 4. Functions
####################################################

# Define a function using `def`.
def add(x, y):
    print("x is %s and y is %s" % (x, y))
    return x + y     # Return the result of the addition.

# Call a function with parameters.
add(5, 6)          # => Outputs "x is 5 and y is 6", returns 11

# Function calls can also be made using keyword arguments.
add(y=6, x=5)      # The order is not important here.

# We can also define a function that accepts multiple positional arguments.
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)

# Similarly, we can define a function that accepts multiple keyword arguments.
def keyword_args(**kwargs):
    return kwargs

# Effectively:
keyword_args(big="foot", loch="ness")      # => {"big": "foot", "loch": "ness"}

# You can also combine both positional and keyword arguments in the same function definition.
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_the_args(1, 2, a=3, b=4)               # => (1, 2) {"a": 3, "b": 4}
```