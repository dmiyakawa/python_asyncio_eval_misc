import asyncio

async def coro(coro_id):
    print('coro({}) started'.format(coro_id))
    for i in range(3):
        print('coro({}): {}'.format(coro_id, i))
        await asyncio.sleep(0)
    print('coro({}) ended'.format(coro_id))

loop = asyncio.get_event_loop()
try:
    coros = [coro(i) for i in range(2)]
    loop.run_until_complete(asyncio.gather(*coros))
finally:
    loop.close()
