#issubclass
class A():
    pass

class B(A):
    pass

class C():
    pass

print(issubclass(B,A))  #True
print(issubclass(C,A))  #False