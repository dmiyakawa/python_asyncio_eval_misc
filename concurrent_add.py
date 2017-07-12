import sys
import threading
import time

sys.setswitchinterval(0.000000001)


a = 0


def del_first():
    global a
    time.sleep(0.01)
    a += 1


threads = []
for i in range(1000):
    t = threading.Thread(target=del_first)
    t.start()
    threads.append(t)

for i, t in enumerate(threads):
    t.join()


print(a)
