import asyncio

class MyAsyncContextManager:

    def __init__(self, id_, n):
        self.id_ = id_
        self.n = n
        self.i = 0

    async def __aenter__(self):
        print('__aenter__({})'.format(self.id_))
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print('__aexit__({})'.format(self.id_))
        return self

    def __aiter__(self):
        print('__aiter__({})'.format(self.id_))
        return self

    async def __anext__(self):
        if self.i < self.n:
            ret = self.i
            self.i += 1
            return ret
        else:
            raise StopAsyncIteration

    async def __await__(self):
        print('__await__({})'.format(self.id_))
        return asyncio.sleep(0)


async def coro(id_):
    async with MyAsyncContextManager(id_, 3) as it:
        print('{}: {}'.format(id_, it))
        async for i in it:
            print('{}: {}'.format(id_, i))

loop = asyncio.get_event_loop()
f1 = asyncio.ensure_future(coro(1))
f2 = asyncio.ensure_future(coro(2))
loop.run_until_complete(asyncio.gather(f1, f2))
# loop.run_until_complete(asyncio.gather(coro(1), coro(2)))
loop.close()
