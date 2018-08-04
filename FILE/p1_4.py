# seek案例
# 打开文件后,从第五个字节处开始读取
# 打开读写指针在0处,即文件的开头
with open("test01.txt", "r") as f:
    # seek移动单位是字节
    f.seek(4, 0)
    strChar = f.read()
    print(strChar)