```python
{
"a": 3,
"b": 4
}
}
```

# 函数也可以接受其他函数作为参数，以及返回另一个函数
def sum_args(*args):
    return sum(args)

def higher_order fun(x, func):
    return x + func(x)

higher_order_fun(2, sum_args)  # => 4

# Python 支持带有默认值的参数定义
def power(x, n=2):
    'Calculate the x raised to the power n. If n not specified, uses 2.'
    return pow(x, n)

power(2)   # => 4
power(2, 3)  # => 8

# 可以使用 lambda 来定义函数表达式
do_something = lambda x, y: "x is %s" % x + " and y is %s" % y
do_something("one", "two")  # => "x is one and y is two"
```