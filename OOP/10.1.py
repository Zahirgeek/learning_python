# __call__ 举例
class A():
    def __init__(self, name = 0):
        print("init in A")

    def __call__(self):
        print("call in A")

    def __str__(self):
        return "String"

a = A()
a()
print(a)