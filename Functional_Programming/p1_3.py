# zip案例
l1 = ["Zahir", "RZ", "ZH"]
l2 = [100, 23, 78]

z = zip(l1, l2)

for i in z:
    print(i)
# 因为是zip是可迭代的,所以下面结果为空
l3 = [i for i in z]
print(l3)

