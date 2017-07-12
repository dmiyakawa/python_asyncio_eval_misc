import asyncio
import time

def is_prime(val):
    print('is_prime({:,})'.format(val))
    if val < 2:
        return False
    return all(val % i for i in range(2, val))

async def async_processes(values):
    return [is_prime(val) for val in values]

loop = asyncio.get_event_loop()
try:
    start = time.monotonic()
    values = [57_009_401, 39_526_741, 83_251_631, 29_920_507]
    print(loop.run_until_complete(async_processes(values)))
    end = time.monotonic()
    print('{} sec'.format(end - start))
finally:
    loop.close()
