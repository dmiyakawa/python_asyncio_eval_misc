import asyncio

async def coro():
    print('coro!')

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
loop.close()
