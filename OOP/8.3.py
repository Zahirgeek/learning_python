#变量的三种用法

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18

a = A()
#属性的三种用法
#1.赋值
#2.读取
#3.删除
a.name = "Zahir"
print(a.name)
del a.name
print(a.name)