#类属性 property
#应用场景:
#对变量除了普通的三种操作,还想增加一些附加的操作,那么可以通过property完成
class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
    #此功能,是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("I'm fget")
        return self.name
    #模拟对变量进行写操作的时候执行的功能
    def fset(self, name):
        print("除了写入,还可以做更多事情")
        self.name = "图灵学院:"  + name

    def fdel(self):
        pass

    #property的四个参数顺序是固定的
    #第一个参数代表读取的时候需要调用的函数
    #第二个参数代表写入的时候需要调用的函数
    #第三个是删除
    name2 = property(fget,fset,fdel,"这是一个property的读取例子")
    name3 = property(fget,fset,fdel,"这是写入的例子")

a = A()
print(a.name)
print(a.name2)
a.name3 = "Zahir"
print(a.name3)
