#time
import time

# 时间模块的属性
# timezone: 当前时区和UTC时间相差的秒数,在没有夏令时的情况下的间隔,东八区的是 -28800
# altzone: 获取当前时区与UTC时间相差的秒数,在有夏令时的情况下
# daylight: 测当前是否是夏令时时间状态,默认为0
print(time.timezone)
print(time.altzone)
print(time.daylight)

# 得到时间戳
print(time.time())

# localtime,得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容
t = time.localtime()
print(t)

# asctime() 返回元组的正常字符串化之后的时间格式
# 格式: time.asctime(时间元组)
# 返回值: 字符串 Tue Jun 6 11:11:00 2017
t = time.localtime()

tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime: 获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime() 使用时间元组获取对应的时间戳
# 格式: time.mktime(时间元祖)
# 返回值: 浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)