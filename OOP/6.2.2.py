class Person():
    name = "Zahir"
    age = 18
    __score = 100
    _petname = "Za"

    def sleep(self):
        print("Sleeping...")

class Teacher(Person):
    def make_test(self):
        pass

t = Teacher()
print(t.name)
#访问受保护的变量
print(t._petname)
#直接访问私有变量
print(t.__score)

print(t._Teacher_score)