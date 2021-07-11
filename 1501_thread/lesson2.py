"""
loggingモジュールにスレッド名を表示する機能あり
"""
import logging
import threading
import time


logging.basicConf
ig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    # print(threading.current_thread().getName(), 'start\n')
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started!!')  # t1, t2の完了を待たずに、本処理は実行される
