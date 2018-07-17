class A():
    name = "Zahir"
    age = 19

    def __init__(self):
        self.name = "aaaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = "bbbb"
    age = 20

a = A()
a.say()

A.say(a)
#此时,传入的是类实例B,因为B具有name和age属性,所以不会报错
A.say(B)
#以上代码,利用了鸭子模型