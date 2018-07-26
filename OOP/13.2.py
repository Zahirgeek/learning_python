#组装类例子 2
from types import MethodType

class A():
    pass

def say(self):
    print("saying...")

a = A()
#手动给类传实例
a.say = MethodType(say, A)
a.say()
