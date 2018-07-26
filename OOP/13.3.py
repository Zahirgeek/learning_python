#利用type造一个类

#先定义类应该具有的成员函数
def say(self):
    print("Saying...")

def talk(self):
    print("Talking...")

#用type来创建一个类
A = type("AName", (object, ), {"class_say":say, "class_talk":talk})

a = A()
a.class_say()
a.class_talk()

print(A.__name__)