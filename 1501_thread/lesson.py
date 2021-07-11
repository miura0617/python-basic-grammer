import threading
import time


def worker1():
    print(threading.current_thread().getName(), 'start\n')
    time.sleep(5)
    print(threading.current_thread().getName(), 'end\n')


def worker2():
    print(threading.current_thread().getName(), 'start\n')
    time.sleep(5)
    print(threading.current_thread().getName(), 'end\n')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started!!')  # t1, t2の完了を待たずに、本処理は実行される
