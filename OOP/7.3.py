# hasattr
class A():
    name = "None"

a = A()
print(hasattr(a, "name"))   #True
print(hasattr(a,"age"))     #False