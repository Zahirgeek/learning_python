#calendar
import calendar

# cal = calendar.calendar(2018, l=1, c=3)
# print(cal)
# isleap: 判断某一年是否是闰年
print(calendar.isleap(1900))

# leapdays: 获取指定年份之间的闰年的个数
print(calendar.leapdays(2008, 2013))

# month() 获取某个月的日历字符串
# 格式:calendar.month(年,月)
# 返回值:月日历的字符串
m8 = calendar.month(2018, 8)
print(m8)

# monthrange() 获取一个月的周几开始和天数
# 格式: calendar.monthrange(年, 月)
# 返回值: 元组(周几开始, 总天数)
# 注意: 周默认 0 - 6 表示周一到周日
m1 = calendar.monthrange(2018, 1)
print(m1)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式: calendar.monthcalendar(年, 月)
# 返回值: 二级列表
# 注意: 矩阵中没有天数用0表示
m3 = calendar.monthcalendar(2018, 3)
print(m3)

# prcal: print calendar 直接打印日历
calendar.prcal(2018)

# prmonth() 直接打印整个月的日历
# 格式: calendar.prmonth(年, 月)
# 返回值: None
calendar.prmonth(2018, 3)

# weekday() 获取周几
# 格式: calendar.weekday(年, 月, 日)
# 返回值: 周几对应的数字
print(calendar.weekday(2018, 8, 1))
