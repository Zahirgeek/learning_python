# 继承的语法
# 在python中,任何类都有一个共同的父类叫object
class Person():
    name = "Noname"
    age = 0
    def sleep(self):
        print("Sleeping........")

#父类写在括号内
class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(Teacher.name)