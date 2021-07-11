"""
生存中のスレッドを確認
"""
import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    # print(threading.current_thread().getName(), 'start\n')
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)    # 5秒待たずして、プログラムを強制終了できる
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    # t1 = threading.Thread(target=worker1)
    # t1.setDaemon(True)    # 5秒待たずして、プログラムを強制終了できる
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # print('started!!\n')  # t1, t2の完了を待たずに、本処理は実行される
    # t1.join()
    # t2.join()             # デーモンでないスレッドも明示的にする人もいる