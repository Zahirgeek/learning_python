#自己组装一个类

class A():
    pass

def say(self):
    print("Saying......")

A.say = say

a = A()
a.say()
