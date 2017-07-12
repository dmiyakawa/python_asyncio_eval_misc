import asyncio
import concurrent.futures
from multiprocessing import cpu_count
import os
import time

def is_prime(val):
    if val < 2:
        return False
    if all(val % i for i in range(2, val)):
        print('{} is prime (PID: {})'.format(val, os.getpid()))

async def async_processes():
    executor = concurrent.futures.ProcessPoolExecutor()
    # executor = concurrent.futures.ThreadPoolExecutor()
    queue = asyncio.Queue()

    values = [78_577, 164_363, 459_937, 469_2979,
              6_700_417, 8_336_501, 9_999_593]
    # You wanna be the guy?
    # values = [2_147_483_647, 2_147_483_649, 67_280_421_310_721]
    for val in values:
        queue.put_nowait(val)

    async def proc(q):
        while not q.empty():
            val = await q.get()
            await loop.run_in_executor(executor, is_prime, val)

    tasks = [proc(queue) for i in range(4)]
    return await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
try:
    start = time.monotonic()
    loop.run_until_complete(async_processes())
    end = time.monotonic()
    print('{} sec'.format(end - start))
finally:
    loop.close()
