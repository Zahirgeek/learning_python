#多继承的例子
#子类可以直接拥有父类的属性和方法,私有属性和方法除外
class Fish():
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("I am swimming....")

class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print("I am flying...")

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Working...")

class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
        print("init in SuperMan")

s = SuperMan("Zahir")
s.fly()
s.swim()

