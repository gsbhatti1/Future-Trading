```python
{
"a": 3,
"b": 4}
}
```

# 函数可以嵌套在其他函数之中
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(1, 2)  # => 内部函数内返回 3

# 匿名函数，通常通过 lambda 表达式定义
# 下面的匿名函数会将两个数相加，并返回结果
lambda a, b: a + b

# 上面的匿名函数可以如下调用：
(lambda a, b: a + b)(1, 2)  # => 3

```