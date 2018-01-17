# 装饰器

**定义：** 不修改原函数，动态增加功能的方式称为装饰器（Decorator）

## 1. 装饰器入门

### 1.1 需求怎么来的

**举例：**</br>

```python
def foo():
    print('hello world!')

foo()
```

上面是一个打印hello world！的函数，但是当我们希望知道这个函数执行时间有多久的时候，我们可以怎么做？

```python
import time
def foo():
    start = time.clock()
    print('hello world!')
    end = time.clock()
    print('used:', end - start)

foo()
```

但是当我们遇到另外一个函数foo2()时候，我们也想知道他的运行时间，就需要继续修改foo2()函数，这样就会很繁琐，我们能不能写一个函数专门计算函数运行时间的呢？

### 1.2 将计算功能剥离出来

怎样写这个函数？

```python
import time
def foo():
    print('hello world!')

def timefunc(func):
    start = time.clock()
    func()
    end = time.clock()
    print('used:', end - start)

timefunc(foo)

```

上面这个逻辑看上去没问题，但是当我们使用时，所有的地方都需要修改调用timefunc()函数，这样太麻烦了。

### 1.3 最大限度的少改动

```python
import time

def foo():
    print('hello world!')

def timeit(func):

    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print('used:', end - start)

    return wrapper

foo = timeit(foo)
foo()
```

这样，计时功能就做好了，当我们调用foo时，只需要添加foo = timeit(foo),就可以达到目的，添加代码比修改代码容易多了。

## 2. python的额外支持

### 2.1 语法糖

python提供了一个方法降低字符输入量

```python
import time

def timefunc(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper

@timefunc
def foo():
    print 'in foo()'

foo()
```

@timefunc，相当与foo = timefunc(foo)
