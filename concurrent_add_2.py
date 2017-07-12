from concurrent.futures import ThreadPoolExecutor
import sys
import time

# sys.setswitchinterval(0.000000001)

a = 0

def increment_one():
    global a
    time.sleep(0.01)
    a += 1


with ThreadPoolExecutor() as executor:
    futures = []
    for i in range(1000):
        futures.append(executor.submit(increment_one))

    for f in futures:
        f.result()

print(a)
