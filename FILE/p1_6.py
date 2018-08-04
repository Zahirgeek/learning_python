# write案例
# 1.向文件追加一句话
# with open(r"test01.txt", "a") as f:
#     f.write("\nZahir is a boy,\nHe is a boy ")

with open(r"test01.txt", "a") as f:
    f.writelines("Zahir is a boy,")
    f.writelines("He is a boy")