#__gt__
class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("???,{0}和{1}到底哪个大".format(self, obj))
        return self._name > obj._name

stu1 = Student("One")
stu2 = Student("Two")

print(stu1 > stu2)