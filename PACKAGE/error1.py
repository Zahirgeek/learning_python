#简单异常案例
#给出提示信息
try:
    num = int(input("输入一个除数"))
    result = 100 / num
    print("结果是:{0}".format(result))
#捕获异常后,把异常实例化,出错信息会在实例里
#注意以下写法
#以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
    print("输入错了,程序退出")
    print(e)
    exit()