#__getattr__
class A():
    name = "NoName"
    age = 19
    def __getattr__(self, name):
        print("meiyou")

a = A()
print(a.name)
print(a.addr)

