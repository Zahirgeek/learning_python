#__setattr__
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性:{0}".format(name))
        #以下语句会出问题,进入死循环
        #self.name = value
        #这种情况,为了避免死循环,规定统一调用父类魔法函数
        super().__setattr__(name, value)
p = Person()
print(p.__dict__)
p.age = 18
