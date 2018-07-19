#Mixin案例
class Person():
    name = "Zahir"
    age = 18

    def eat(self):
        print("Eating...")

    def drink(self):
        print("Drinking...")

    def sleep(self):
        print("Sleeping...")

class Teacher(Person):
    def work(self):
        print("Working...")

class Student(Person):
    def study(self):
        print("Studing...")

class Tutor(Teacher, Student):
    pass

t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)

class TeacherMixin():
    def work(self):
        print("Work")

class StudentMixin():
    def study(self):
        print("Study")

class TutorM(Person, TeacherMixin, StudentMixin):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
