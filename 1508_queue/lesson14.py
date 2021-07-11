"""
キューを使ってスレッド間(worker1 – worker2)でデータを入れたり、受け取ったりすることができます
"""
import logging
import queue
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):
    logging.debug('start')
    queue.put(100)       # FIFO
    queue.put(200)       # FIFO
    time.sleep(5)        # これをすると、worker1,2もx=1
    logging.debug('end')


def worker2(queue):
    logging.debug('start')
    time.sleep(5)        # これをすると、worker1,2もx=1
    print(queue.get())   # worker1でputした100をgetできる
    print(queue.get())   # worker1でputした200をgetできる
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue,))
    t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    t2.start()
