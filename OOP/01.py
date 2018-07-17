'''
定义一个学生类,用来形容学生
'''
#定义一个空类
class Student():
    # 一个空类,pass代表直接跳过
    # 此处pass必须有
    pass

#定义一个对象
Zahir = Student()

#再定义一个类,用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("I'm doing my homework")

        #推荐在函数末尾使用return 语句
        return

#实例化一个叫Za的学生,是一个具体的人
Za = PythonStudent()
print(Za.name)
print(Za.age)
Za.doHomework()
print(Za.__dict__)
print(PythonStudent.__dict__)