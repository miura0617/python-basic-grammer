"""
スレッドのRLock(Lockを2重でできる)
"""
import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(lock):
    with lock:               # lock取得することで、他スレッドはこのスレッドがreleaseされるまで実行されない
        logging.debug('start')
        time.sleep(5)        # これをすると、worker1,2もx=1
        logging.debug('end')
def worker2(lock):
    with lock:               # lock取得することで、他スレッドはこのスレッドがreleaseされるまで実行されない
        logging.debug('start')
        time.sleep(5)        # これをすると、worker1,2もx=1
        logging.debug('end')
def worker3(lock):
    with lock:               # lock取得することで、他スレッドはこのスレッドがreleaseされるまで実行されない
        logging.debug('start')
        time.sleep(5)        # これをすると、worker1,2もx=1
        logging.debug('end')



if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()    # RLock
    t1 = threading.Thread(target=worker1, args=(lock,))
    t2 = threading.Thread(target=worker2, args=(lock,))
    t3 = threading.Thread(target=worker3, args=(lock,))
    t1.start()
    t2.start()
    t3.start()
