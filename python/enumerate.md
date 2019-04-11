# enumerate

`enumerate()`是python的内置函数
可以用于将可遍历的数据对象组合成一个索引序列。

```python
i = 0
for item in iterable:
    print(i, item)
    i += 1
```

使用enumerate

```python
for i, item in enumerate(iterable):
    print(i, item)
```

`enumerate`还可以接受参数。`enumerate(iterable, 1)`

