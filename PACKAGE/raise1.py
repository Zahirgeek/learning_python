#raise案例 - 2
#自己定义异常
#需要注意: 自定义异常必须是系统异常的子类
class ZahirValueError(ValueError):
    pass
try:
    print("Zahir")
    print(12.3)
    #手动引发异常
    #注意语法: raise ErrorClassName
    raise ZahirValueError
    print("还没有完")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常,未知")
finally:
    print("run")