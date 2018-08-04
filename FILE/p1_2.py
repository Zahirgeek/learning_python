# with语句案例

# with open(r"test01.txt","r") as f:
#     pass
    # 下面语句块开始时对文件f进行操作
    # 在本模块中不需要再使用close关闭文件f

# with案例

# with open(r"test01.txt", "r") as f:
#     # 按行读取内容
#     strline = f.readline()
#     # 此结构保证能够完整读取文件直到结束
#     while strline:
#         print(strline)
#         strline = f.readline()

# with案例
# with open(r"test01.txt", "r") as f:
#     li = list(f)
#     for line in li:
#         print(line)
