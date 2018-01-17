# 函数
def foo():
    print('hello world!')

foo()

# 第一个版本
import time

def foo():
    start = time.clock()
    print('hello world!')
    end = time.clock()
    print('used:', end - start)

foo()

# 第二个版本
import time

def foo():
    print('hello world!')

def timefunc(func):
    start = time.clock()
    func()
    end = time.clock()
    print('used:', end - start)

timefunc(foo)

# 第三个版本
#-*- coding: UTF-8 -*-

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

# 第四个版本，python语法糖
import time
 
def timefunc(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
 
@timeitfunc
def foo():
    print 'in foo()'
 
foo()