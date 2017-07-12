import asyncio
import inspect
import time
import types


# @asyncio.coroutine
@types.coroutine
def gen():
    for i in range(10):
        yield i


async def asyncgen():
    yield 10


async def async_main():
    g = asyncgen()
    v = await g
    print(v)
    time.sleep(0.1)


loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
