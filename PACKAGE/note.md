# 1.模块
- 一个模块就是一个包含Python代码的文件,后缀名是.py就可以,模块就是个Python文件
- 为什么要用模块
    - 程序太大,编写维护非常不方便,需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,所以任何代码可以直接书写
    - 不过根据模块的规范,最好在模块中编写以下内容
        - 函数(单一功能)
        - 类(相似功能的组合,或者类似业务模块)
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 假如模块名称直接以数字开头,需要借助importlib帮助
    - 语法
        
            import  module_name
            module_name.function_name
            module_name.class_name
    - 案例p1_1 p1_2
    - 运行导入模块就相当于被导入的模块从头到尾执行了一遍
    - 可以借助importlib包实现导入以数字开头的模块名称
        
            import importlib
            //相当于导入了一个叫01的模块并把导入模块赋值给了Zahir
            Zahir = importlib.import_module("01")
    
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
        - 案例p1_3            
    
    - from module_name import func_name, class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容,不需要前缀
        - 案例p1_4
        
    - from module_name import *
        - 导入模块所有内容
        - 案例p1_5
    
- 'if __name__ == "__main__"'的使用
    - 可以有效避免模块代码被导入是的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口

# 2.模块的搜索路径和存储
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
    
        import sys
        sys.path 属性可以获取路径列表
        # 案例 p2_1
- 添加搜索路径
    
        sys.path.apppend(dir)
- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索Python的内置模块
    3. 搜索sys.path路径

# 3.包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构
    
    
        |--- 包
        |---|--- __init__.py 包的标志文件
        |---|--- 模块1
        |---|--- 模块2
        |---|--- 子包(子文件夹)
        |---|---|--- __init__.py 包的标志文件
        |---|---|--- 子包模块1
        |---|---|--- 子包模块2

- 包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py中的内容
        - 使用方式是:
            
                package_name.func_name
                package_name.class_name.func_name()
        - 此种方式的访问内容是
        - 案例 pkg01, p3_1.py
    - import package_name as p
        - 用法跟作用方式,跟上述简单导入一致
        - 注意的是此种方法是默认对__init__.py内容的导入
        
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
            
            package.module.func_name
            package.module.class.fun()
            package.module.class.var
        - 案例p3_2
    
    - import package.module as pm
    
- from ... import 导入
    - from package import module module1, module2, module3, ......
    -此种导入方法不执行"__init__"的内容
        
            from pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包 '__init__.py'文件中所有的函数和类
        - 使用方法
            
                func_name()
                class_name.func_name()
                class_name.var
                
        - 案例p3_3.py, 注意此种导入的具体内容
        
- from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
        
            func_name()
            class_name.func_name()

- 在开发环境中经常会引用其他模块,可以在当前包中直接导入其他模块中的内容
    -import 完整的包或者模块的路径
    
- '__all__'的用法
    - 在使用from package import * 的时候, *可以导入的内容
    - '__init__.py'中如果文件为空,或者没有'__all__', 那么只可以把'__init__'中的内容导入
    - '__init__'如果设置了'__all__'的值,那么则按照'__all__'指定的子包或者模块进行加载
    如此则不会载入'__init__'中的其他内容
    
        
            - '__all__=['module1', 'module2', 'package1'.........]'
            
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突
    
        setName()
        Student.setName()
        Dog.setName()
        
#4.异常
- 广义上的错误分为错误和异常
- 错误是指可以人为避免
- 异常是指在语法逻辑正确的前提下,出现的问题
- 在python中,异常是一个类,可以处理和使用
## [异常的分类](https://www.cnblogs.com/zln1021/p/6106185.html)
##异常处理
- 不能保证程序永远正确运行
- 但是,必须保证程序在最坏的情况下得到的问题被妥善处理
- python的异常处理模块全部语法
    
        try:
            尝试实现某个操作
            如果没有出现异常,任务就可以完成
            如果出现异常,将异常从当前代码块扔出去尝试解决异常
        except 异常类型1:
            解决方案1:用于尝试在此处处理异常解决问题
        except 异常类型2:
            解决方案2:用于尝试在此处处理异常解决问题
        except (异常类型1, 异常类型2)
            解决方案: 针对多个异常使用相同的处理方式
        except:
            解决方案: 所有异常的解决方案
        else:
            如果没有出现任何异常,将会执行此处代码
        finally:
            管你有没有异常都要执行的代码
- 流程
    1.执行try下面的语句
    2.如果出现异常,则在except语句里查找对应异常并进行处理
    3.如果没有出现异常,则执行else语句内容
    4.最后,不管是否出现异常,都要执行finally语句
- 除except(最少一个)以外,else和finally可选
- else语句案例(else.py)

## 4.1用户手动引发异常
- 当某些情况,用户希望自己引发一个异常的时候,可以
使用raise关键字来引发异常
- raise案例(raise.py, raise1.py)
    - 语法: raise ErrorClassName 

## 4.2关于自定义异常
- 只要是raise异常,则推荐自定义异常
- 在自定义异常的时候,一般包含以下内容:
    - 自定义发生异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
- 最终的目的是,一旦发生异常,方便程序员快速定位错误现场

# 5.常用模块
- 以下所有模块使用理论上都应该先导入,string是特例
## 5.1 calendar (p5_1.py)
    - 跟日历相关的模块
    - 参数:
        
            w = 每个日期之间的间隔字符数
            l = 每周所占用的行数
            c = 每个月之间的间隔字符数
    
## 5.2time (p5_2.py)
    - 时间戳
        - 一个时间表示,根据不同语言,可以使整数或者浮点数
        - 是从1970年1月1日0时0分0秒到现在经历的秒数
        - 如果表示的时间是1970年以前或者太遥远的未来,可能出现异常
        - 32位操作系统能够支持到2038年

    - UTC时间
        - UTC又称为世界协调时间,以英国的格林尼治天文所在地区
        的时间作为参考时间,也叫世界标准时间
        - 中国的时间是 UTC + 8 东八区
    
    - 夏令时
        - 夏令时就是在夏天的时候将时间调快一个小时,
        本意是督促大家早睡早起节省蜡烛.每天变成25小时
        本质没变还是24小时
        
    - 时间元组
        - 一个包含时间内容的普通元组
            
                索引      内容      属性      值
                0         年        tm_year   2015
                1         月        tm_mon    1~12
                2         日        tm_mday   1~31
                3         时        tm_hour   0~23
                4         分        tm_min    0~59
                5         秒        tm_sec    0~61
                6         周几      tm_wday   0~6
                7         第几天    tm_yday   1~366
                8         夏令时    tm_isdst  0, 1, -1(表示夏令时)

        


- datetime
- timeit
- os
- shutil
- zip
- math
- string