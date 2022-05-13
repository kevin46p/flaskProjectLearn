import threading
import time


class MyThread1(threading.Thread):
    def run(self) -> None:
        print("============thread1=============\n")
        lock1.acquire()
        print("thread1-------------获取锁1-------------\n")
        time.sleep(1)

        lock2.acquire()
        print("thread1-------------获取锁2-------------\n")
        lock2.release()
        print("thread1-------------释放锁2-------------\n")
        lock1.release()
        print("thread1-------------释放锁1-------------\n")


class MyThread2(threading.Thread):
    def run(self) -> None:
        print("============thread2=============\n")
        lock2.acquire()
        print("thread2-------------获取锁2-------------\n")
        time.sleep(10)
        lock2.release()
        print("thread2-------------释放锁2-------------\n")
        lock1.acquire()
        print("thread2-------------获取锁1-------------\n")
        lock1.release()
        print("thread2-------------释放锁1-------------\n")


num = 0


def add1(nums, mutex):
    # mutex.acquire()
    for i in range(nums):
        global num
        num += 1
    # mutex.release()
    # 这样就会阻塞，不会向下进行
    # time.sleep(1)
    # print(f'-----add1----{num}')


def add2(nums, mutex):
    # mutex.acquire()
    # mutex.acquire()
    for i in range(nums):
        global num
        num += 1
    # mutex.release()
    # 这样就会阻塞，不会向下进行
    # time.sleep(1)
    # print(f'-----add2----{num}')


count = 0


# Define a function for the thread
def print_time(threadName):
    global count

    c = 0
    while (c < 100):
        c += 1
        count += 1
        print("{0}: set count to {1}".format(threadName, count))


lock1 = threading.Lock()
lock2 = threading.Lock()
if __name__ == '__main__':
    # t1 = MyThread1()
    # t2 = MyThread2()
    # t1.start()
    # t2.start()
    # # mutex = threading.Lock()
    # mutex = threading.RLock()
    # t1 = threading.Thread(target=add1, args=(100000, mutex))
    # t2 = threading.Thread(target=add2, args=(100000, mutex))
    # t1.start()
    # t2.start()
    # print("2000000\n",num)
    try:
        t1 = threading.Thread(target=print_time, args=("Thread-1",))
        t2 = threading.Thread(target=print_time, args=("Thread-2",))
        t3 = threading.Thread(target=print_time, args=("Thread-3",))
        t1.start()
        t2.start()
        t3.start()
    except Exception as e:
        print("Error: unable to start thread")
