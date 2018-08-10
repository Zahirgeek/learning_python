import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at: ", time.ctime())
    # 睡眠多长时间,单位是秒
    print("attribute1: ", in1)
    time.sleep(4)
    print("End loop 1 at: ", time.ctime())

def loop2(in1, in2):
    print("Start loop2 at: ", time.ctime())
    print("attribute1: ",in1, "attribute2: ", in2)
    time.sleep(2)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())

    t1 = threading.Thread(target=loop1, args=("Zahir", ))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("Zahir1", "Zahir2"))
    t2.start()
    # 不一定是最后一个执行
    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()