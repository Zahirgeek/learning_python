# RE-练习
# RE使用大致步骤
# 1. 使用compile将表示正则的字符串编译为一个pattern对象
# 2. 通过pattern对象提供一系列方法对文本进行查找匹配,获得匹配结果,一个Match对象
# 3. 最后使用Match对象提供的属性和方法获得信息,根据需要进行操作
# 导入相关包
import re

# 查找数字
# r表示字符串不转义
# p = re.compile(r"\d+")
# # 在字符串中进行查找,按照规则p指定的正则进行查找
# m = p.match("12sdf21")
#
# print(m)


# p = re.compile(r"\d+")
# # 参数5,6表示在字符串中查找的范围
# m = p.match("12sdf21", 5, 6)
# print(m)
# print(m[0])
# print(m.start(0))

# re.I表示忽略大小写
# p = re.compile(r"([a-z]+) ([a-z]+)", re.I)
#
# m = p.match("I am Zahir ,")
#
# print(m)
# print(m.group(0))   # I am
# print(m.group(1))   # I
# print("-"*30)
# print(m.start(1))   # 0
# print(m.end(1))     # 1
# print(m.groups())   # ('I', 'am')

# 查找
# p = re.compile(r"\d+")
# m = p.search("one12two456threefour56")
#
# print(m.group())
#
# res = p.findall("one12two456threefour56")
# print(type(res))
# print(res)

# sub替换
# p = re.compile(r"([a-z]+) ([a-z]+)", re.I)
#
# s = "hello 123 world 777 I am 23 Zahir"
#
# res = p.findall(s)
# print(res)
# print("*"*40)
# res0 = p.sub(r"Hello World", s)
# print(res0)

# 匹配中文
title = u"世界 你好, hello world"

p = re.compile(r"[\u4e00-\u9fa5]+")
res = p.findall(title)
print(res)
