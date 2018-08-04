# Python语言的高级特性

## 函数式编程(FunctionalProgramming)
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数,同样可以作为返回值
    - 纯函数式编程语言: LISP, Haskell
    
- Python函数式编程只是借鉴函数式编程的一些特点,可以理解成一半函数式一半Python
- 内容:
    - 高级函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
    
### lambda表达式
- 函数: 最大程度复用代码
    - 存在问题: 如果函数很小,很短,则会造成啰嗦

### 装饰器(Decrator)   (p1_1.py)
- 在不改动函数代码的基础上无限制扩展函数功能的一种机制,
本质上讲,装饰器是一个返回函数的高阶函数
- 装饰器的使用: 使用@语法,即在每次要扩展到函数定义前使用@+函数名
- 装饰器的好处是,一旦定义,则可以装饰任意函数
- 一旦被其装饰,则把装饰器的功能直接添加到定义函数的功能上

### 偏函数  (p1_2.py)
- 参考固定的函数,相当于一个有特定参数的函数体
- functools.partial的作用是,把一个函数某些函数固定,返回一个新的函数

### zip
- 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容

### collections模块
- namedtuple
    - tuple类型
    - 给元组命名
    
            import collections

            Person = collections.namedtuple("Student",["name","age","sex"])

            Zahir = Person("Zahir", "18", "male")

            print(Zahir.sex)
- deque

        from collections import  deque

        q = deque(["a", "b", "c"])
        print(q)

        q.append("d")
        print(q)

        q.appendleft("x")
        print(q)
- 比较方便的解决了频繁删除插入带来的效率问题

- defaultdict
    - 当直接读取dict不存在的属性时,直接返回默认值
 
            from collections import defaultdict

            func = lambda : "Zahir"
            d1 = defaultdict(func)
            d1["one"] = 1

            print(d1["one"])
            print(d1["four"])
- counter
    -统计字符串个数
        
            from collections import Counter
            #下面结果不以abcdefgabcabcdabcaba作为键值,而是以其中每一个字母作为键值
            # 因为括号里的内容是可迭代的
            c = Counter("abcdefgabcabcdabcaba") 
            #Counter({'a': 6, 'b': 5, 'c': 4, 'd': 2, 'e': 1, 'f': 1, 'g': 1})
            print(c)
            
            
            from collections import Counter
            s = ["Zahir", "is", "is", "is", "a", "boy"]
            c = Count(s)
            #Counter({'is': 3, 'Zahir': 1, 'a': 1, 'boy': 1})
            print(c)