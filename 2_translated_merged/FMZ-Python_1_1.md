``` python
all_the_args(1, 2, a=3, b=4)  # => Prints: 
                                 (1, 2)
                                 {'a': 3, 'b': 4}
```

# 嵌套函数和闭包
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(1, 2)  # => 3

# 递归函数，注意 Python 的默认限制是 1000 次递归调用
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

factorial(5)  # => 120

# 匿名函数，使用 lambda 关键字
lambda x, y: x + y

# 通过 map 函数来迭代并修改序列中的每个元素
li = [5, 4, 3]
list(map(lambda x: x**2, li))  # => [25, 16, 9]

# 使用 filter 来筛选一个序列
li = [0, 1, 2, 3, 4, 5]
list(filter(lambda x: x > 1, li))  # => [2, 3, 4, 5]

# 使用 sorted 对列表进行排序
li = [1, 3, 2]
sorted(li)  # => [1, 2, 3]
```

> Summary

This Python quick guide covers basic data types and operations, variables and collections, control flow, functions, and more. It's intended for traders looking to get up to speed with the language quickly.
```