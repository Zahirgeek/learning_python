# Decrator
# 任务:
# 对hello函数进行功能扩展,每次执行hello打印当前时间

import time

# 高阶函数,以函数作为参考
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper

@printTime
def hello():
    print("Hello World")

hello()
# 上述对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数
def hello3():
    print("手动执行")
hello3()

hello3 = printTime(hello3)
hello3()
