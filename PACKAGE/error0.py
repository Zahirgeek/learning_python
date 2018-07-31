#简单异常案例
try:
    num = int(input("输入一个除数"))
    result = 100 / num
    print("结果是:{0}".format(result))
except:
    print("输入错了,程序退出")
    exit()
