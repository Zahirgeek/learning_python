import time

# 导入多线程包并更名为 thread
import _thread as thread

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

    thread.start_new_thread(loop1, ("Zahir", ))

    thread.start_new_thread(loop2, ("Zahir1", "Zahir2"))

    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()

    while True:
        time.sleep(1)