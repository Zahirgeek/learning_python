# 新建一个函数,此函数是默认输入的字符串是16进制数
# 把此字符串返回十进制的数字
# def int16(x, base = 16):
#     return int(x, base)
# print(int16("1"))

# 偏函数
import  functools
#实现上面int16的功能
int16 = functools.partial(int, base=16)

print(int16("271c"))