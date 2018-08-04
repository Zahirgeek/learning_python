with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()
# tell的返回数字的单位是byte
# read是以字符为单位