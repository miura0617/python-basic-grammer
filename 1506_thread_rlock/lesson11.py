"""
スレッドのRLock(Lockを2重でできる)
"""
import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    # print(threading.current_thread().getName(), 'start\n')
    logging.debug('start')
    with lock:               # lock取得することで、他スレッドはこのスレッドがreleaseされるまで実行されない
        i = d['x']
        time.sleep(5)        # これをすると、worker1,2もx=1
        d['x'] = i + 1
        logging.debug(d)
        with lock:           # RLockを使えば二重でLockしてもデッドロックしない
            d['x'] = i + 1
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()    # RLock
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
