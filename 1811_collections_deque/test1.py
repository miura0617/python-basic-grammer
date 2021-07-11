import collections
import queue


# Double-end queue
collections.deque

q = queue.Queue()      # FIFO
lq = queue.LifoQueue() # LIFOなので、[1, 2, 3]と入れたら, 1, 2, 3を順に返す
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

for _ in range(3):
    print('FIFO queue = {}'.format(q.get()))
    print('LIFO queue = {}'.format(lq.get()))
    print('list       = {}'.format(l.pop()))
    print('deque      = {}'.format(d.pop()))
    print()

