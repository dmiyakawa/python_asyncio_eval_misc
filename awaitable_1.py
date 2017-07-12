import asyncio

async def f():
    return 1

class MyAwaitable():
    def __await__(self):
        r = f().__await__()
        print(type(r))
        return r

async def coro():
    print(await MyAwaitable())

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
loop.close()
