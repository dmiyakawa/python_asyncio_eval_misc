import asyncio
import time

class SimpleAwaitable:
    def __await__(self):
        yield 1

async def coro(n):
    print('coro_{} started'.format(n))
    loop = asyncio.get_event_loop()
    loop.stop()
    await SimpleAwaitable()
    print('coro_{} exiting'.format(n))

loop = asyncio.get_event_loop()
tasks = [loop.create_task(coro(i)) for i in range(5)]
try:
    while tasks:
        loop.run_forever()
        tasks = [f for f in tasks if not f.done()]
finally:
    print('closing')
    loop.close()
print('exiting')
