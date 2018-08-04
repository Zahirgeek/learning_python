# 序列化案例
import pickle

age = 19

with open(r"test01.txt", "wb") as f:
    pickle.dump(age, f)

# 反序列化案例

with open(r"test01.txt", "rb") as f:
    ag = pickle.load(f)
    print(ag)