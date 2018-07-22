#属性案例
#创建Student类,描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以用增加一个函数,然后自动调用的方式,但很蠢
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #构造函数调用setName
        self.setName(name)
    def intro(self):
        print("Hi,my name is {0}".format(self.name))

    def setName(self, name):
        self.name = name.upper()
s1 = Student("Zahir LIU", 18)
s2 = Student("za", 20)

s1.intro()
s2.intro()