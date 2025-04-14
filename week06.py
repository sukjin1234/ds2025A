from  queue import Queue

q = Queue()
q.put("Data structure")
q.put("Data base")
q.put("Java script")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
