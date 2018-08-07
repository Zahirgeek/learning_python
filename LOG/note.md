# LOG
- [Python之日志处理（logging模块）](https://www.cnblogs.com/yyds/p/6901864.html)
logging
----
- logging模块提供模块级别的函数记录日志
- 包括四大组件

## 1. 日志相关概念
- 日志
- 日志的级别(level)
	- 不同的用户关注不同的程序信息
	- DEBUG
	- INFO
	- NOTICE
	- WARING
	- ERROR
	- CRITICAL
	- ALERT
	- EMERGENCY
- IO操作->不要频繁操作
- LOG的作用
	- 调试
	- 了解软件的运行情况
	- 分析定位问题
- 日志信息
	- time
	- 地点
	- level
	- 内容
- 成熟的第三方日志
	- log4j
	- log4php
	- logging
## 2.logging模块
- 日志级别
	- 级别可自定义
	- DEBUG
	- INFO
	- WARING
	- ERROR
	- CRITICAL
- 初始化/写日志实例需要制定级别,只有当级别等于或高于制定级别才被记录
- 使用方式
	- 直接使用logging(封装了其他组件)
	- logging四大组件直接定制
### 2.1 logging模块级别的日志
- 使用以下几个函数
	
		logging.debug(msg, *args, **kwargs)		创建一条严重级别为DEBUG的日志记录
		logging.info(msg, *args, **kwargs)		创建一条严重级别为INFO的日志记录
		logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
		logging.error(msg, *args, **kwargs)		创建一条严重级别为ERROR的日志记录
		logging.critical(msg, *args, **kwargs)	创建一条严重级别为Level的日志记录
		logging.basicConfig(**kwargs)			对root logger进行一次性配置
- logging.basicConfig(**kwargs)	(p1.py)
	- 只在第一次调用的时候起作用
	- 不配置logger则使用默认值
		- 输出: sys.stderr
		- 级别: WARNING
		- 格式: level:log_name:content
- logging.basicConfig()函数中的具体参数：
	- filename：指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中；
	- filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“w”还可指定为“a”；
	- format：指定handler使用的日志显示格式；
	- datefmt：指定日期时间格式。，格式参考strftime时间格式化（下文）
	- level：设置rootlogger的日志级别
	- stream：用指定的stream创建StreamHandler。可以指定输出到- sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

- format参数中可能用到的格式化信息：

		%(name)s			Logger的名字 
	
		%(levelno)s 		数字形式的日志级别 
	
		%(levelname)s 		文本形式的日志级别 
	
		%(pathname)s		调用日志输出函数的模块的完整路径名，可能没有
		
		%(filename)s		调用日志输出函数的模块的文件名
		
		%(module)s			调用日志输出函数的模块名
		
		%(funcName)s		调用日志输出函数的函数名
		
		%(lineno)d			调用日志输出函数的语句所在的代码行
		
		%(created)f			当前时间，用UNIX标准的表示时间的浮 点数表示
		
		%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
		
		%(asctime)s 		字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
		
		%(thread)d 			线程ID。可能没有
		
		%(threadName)s 		线程名。可能没有
		
		%(process)d 		进程ID。可能没有
		
		%(message)s 		用户输出的消息

### 2.2 logging模块的处理流程
- 四大组件
	- 日志器(Logger): 产生日志的一个接口
	- 处理器(Handler): 把产生的日志发送到相应的目的地
	- 过滤器(Filter): 更精细的控制那些日志输出
	- 格式器(Formatter): 对输出信息进行格式化
- Logger
	- 产生一个日志
	- 操作

			Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
			Logger.addHandler() 和 Logger.removeHandler()	为该Logger对象添加和移除一个处理器
			Logger.addFilter() 和 Logger.removeFilter()		为该logger对象添加和移除一个过滤器
			Logger.debug: 产生一条debug级别的日志,同理,info,error等
			Logger.exception(): 创建类似于Logger.error的日志消息
			Logger.log(): 获取一个明确的日志level参数类创建一个日志记录
	- 如何得到一个logger对象
		- 实例化
		- logging.getLogger()		#推荐
- Handler
	- 把log发送到指定位置
	- 方法
		- setLevel
		- setFormat
		- addFilter, removeFilter

	- 不需要直接使用,Handler是基类

			logging.StreamHandler	将日志消息发送到输出流Stream,如std.out, std.err或任何file-like对象
			logging.FileHandler		将日志消息发送到磁盘文件,默认情况下文件大小会无线增长
			logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件,并支持日志文件按大小切割
			logging.handlers.TimedRotatingFileHandler	将日志消息发送到磁盘文件,并支持日志文件按时间切割
			logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
			logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
			logging.NullHandler	该Handler实例会忽略error messages,通常被想使用logging的library开发者使用
	- Format类
		- 直接实例化
		- 可以继承Format添加特殊内容
		- 三个参数
			- fmt: 指定消息格式化字符串,如果不指定改参数则默认使用message的原始值
			- datefmt: 指定日期格式字符串,如果不指定改参数则默认使用"%Y-%m%d %H:%M:%S"
			- style: Python 3.2新增的参数,可取值为"%","{"和"$", 如果不指定该参数则默认使用"%"

	- Filter类
		- 可以被Handler和Logger使用
		- 控制传递过来的信息的具体内容
		- 案例(p2.py)