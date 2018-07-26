# 抽象
class Animal():
    #抽象方法
    def sayHello(self):
        pass
class Dog():
    def sayHello(self):
        print("闻一下对方")

class Person():
    def sayHello(self):
        print("kiss another")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()
