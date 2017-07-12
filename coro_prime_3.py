import asyncio
import concurrent.futures
import time

def is_prime(val):
    print('is_prime({})'.format(val))
    if val < 2:
        return False
    return all(val % i for i in range(2, val))

async def async_processes(values):
    executor = concurrent.futures.ProcessPoolExecutor()
    # executor = concurrent.futures.ThreadPoolExecutor()
    queue = asyncio.Queue()

    for val in values:
        queue.put_nowait(val)

    async def proc(q):
        ret = []
        while not q.empty():
            val = await q.get()
            ret.append(await loop.run_in_executor(executor, is_prime, val))
        return ret

    tasks = [proc(queue) for i in range(4)]
    return [f.result() for f in (await asyncio.wait(tasks))[0]]


loop = asyncio.get_event_loop()
try:
    start = time.monotonic()
    values = [57_009_401, 39_526_741, 83_251_631, 29_920_507]
    print(loop.run_until_complete(async_processes(values)))
    end = time.monotonic()
    print('{} sec'.format(end - start))
finally:
    loop.close()
