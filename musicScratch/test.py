from threading import Thread
import queue

q = queue.PriorityQueue()

q.put((10, 'fd'),True,None)
q.put_nowait((20, 'adsf',))
q.put_nowait((10, 'sadf',))
q.put_nowait((-5, 'dd',))
q.put_nowait((1, 'f',))
print(q.get(block=True))
print(q.get())
print(q.get())
print(q.get())
print(q.get())