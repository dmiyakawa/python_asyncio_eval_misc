import asyncio
import inspect

async def gen2():
    for i in range(10):
        yield 'hello{}'.format(i)

async def gen():
    try:
        await asyncio.sleep(0.1)
        async for message in gen2():
            yield message
    except ZeroDivisionError:
        # await asyncio.sleep(0.2)
        yield 'world'

async def async_main():
    g = gen()
    async for v in g:
        print(v)
    #v = await g.asend(None)
    #print(v)

    v = await g.athrow(ZeroDivisionError)
    print(v)
 
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(async_main())
finally:
    loop.close()
