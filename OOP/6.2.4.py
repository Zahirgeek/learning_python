#构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次实例化的时候,第一个被自动调用
    #因为主要工作是进行初始化,所以得名
    def __init__(self):
        print("I am init in dog")

wang = Dog()