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
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('longgggggggggggggggggggggggg')
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)
    t1 = threading.Thread(target=worker1, args=(queue,))
    t1.start()
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    queue.put(None)

    t1.join()