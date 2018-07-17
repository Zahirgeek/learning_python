#扩充父类功能
class Person():
    name = "Zahir"
    age = 18
    __score = 100
    _petname = "Za"

    def sleep(self):
        print("Sleeping...")
    def work(self):
        print("make some money")

class Teacher(Person):
    def make_test(self):
        print("attention")
    def work(self):
        #扩充父类功能只需要调用父类相应函数
        #Person.work(self)  #1
        #super代表得到父类
        super().work()
        self.make_test()

t = Teacher()
t.work()
