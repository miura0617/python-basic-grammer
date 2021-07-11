"""
メインキューでたくさんの処理をしないといけない場合
"""
import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(barrier):
    r = barrier.wait()      # 1つ目のスレッド立ち上がり待ち
    logging.debug('num = {}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait()     # 2つ目のスレッド立ち上がり待ち。ここでworker1, 2が初めて動く
    logging.debug('num = {}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


if __name__ == '__main__':
    barrier = threading.Barrier(2)  # 2個スレッドが立ち上がるまで待つ
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))
    t1.start()
    t2.start()
