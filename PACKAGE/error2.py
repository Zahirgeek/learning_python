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
#如果是多种error的情况
#需要把越具体的错误,越往前放
#在异常类继承关系中,越是子类的异常,越要往前放
#越是父类的异常,越要往后放

#在处理异常的时候,一旦拦截到某一个异常,则不再往下
#查看,直接进行下一条代码,即有finally则执行finally语句块,
#否则就执行下一个大的语句
except NameError as e:
    print("名字起错了,程序退出")
    print(e)
    exit()
except AttributeError as e:
    print("属性有点问题,程序退出")
    print(e)
    exit()
#所有异常都是继承自Exception
#如果写上下面这句话,任何异常都会拦住
#而且,下面这句话一定是最后一个exception
except Exception as e:
    print("未知错误,程序退出")
    print(e)
    exit()

print("だいじょうぶ")