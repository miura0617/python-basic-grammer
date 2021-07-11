from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager)

import logging
import multiprocessing
import time


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i


if __name__ == '__main__':
    #t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(5) as p:       # プールの数でワーカープロセスの数をコントールできる
        logging.debug(p.apply(worker1, (200,)))  # p.applyで同期処理
        logging.debug('executed apply')
        p1 = p.apply_async(worker1, (100,))      # p.apply_asyncで非同期処理
        p2 = p.apply_async(worker1, (100,))      # p.apply_asyncで非同期処理
        logging.debug('executed')
        logging.debug(p1.get())
        logging.debug(p2.get())
