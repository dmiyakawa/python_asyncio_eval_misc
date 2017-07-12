import asyncio
import time

async def coro_async():
    print('coro_async started')
    for i in range(3):
        print('coro_async: {}'.format(i))
        await asyncio.sleep(0)
    print('coro_async ended')


async def coro_sync():
    print('coro_sync started')
    for i in range(3):
        print('coro_sync: {}'.format(i))
        time.sleep(0)
    print('coro_sync ended')
        
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(coro_async(), coro_sync()))
loop.close()
