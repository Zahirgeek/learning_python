#继承中的构造函数4

class Animal():
    pass

class PaxingAni(Animal):
    def __init__(self,name):
        print("Paxing Dongwu {0}".format(name))
class Dog(PaxingAni):
    #__init__就是构造函数
    #每次实例化的时候,第一个被自动调用
    #因为主要工作是进行初始化,所以得名
    def __init__(self):
        print("I am init in dog")
#Cat没有写构造函数
class Cat(PaxingAni):
    pass
#实例化的时候,括号内的参数需要跟构造函数参数匹配
#实例化的时候,自动调用了Dog的构造函数
#没有调用父类构造函数
wang = Dog()

#此时应该自动调用构造函数,因为Cat没有构造函数,所以查找父类构造函数
#因为在PaxingAni中构造函数需要两个参数,实例化的时候给了一个,报错
miao = Cat()