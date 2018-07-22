#内置属性举例
class Person():
    '''
    这是一个类的说明文档
    '''
    #函数的名称可以任意
    def fget(self):
        return self._name + " " + self._name

    def fset(self, name):
        #所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)