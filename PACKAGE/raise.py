#raise案例 - 1
try:
    print("Zahir")
    print(12.3)
    #手动引发异常
    #注意语法: raise ErrorClassName
    raise ValueError
    print("还没有完")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常,未知")
finally:
    print("run")