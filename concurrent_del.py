import sys
import threading
import time

sys.setswitchinterval(0.000000001)


lst = [i for i in range(1000)]
new_lst = []


def del_first():
    global a
    time.sleep(0.01)
    elem = lst.pop()
    new_lst.append(elem)


threads = []
for i in range(1000):
    t = threading.Thread(target=del_first)
    t.start()
    threads.append(t)

for i, t in enumerate(threads):
    t.join()

print(len(set(new_lst)))
