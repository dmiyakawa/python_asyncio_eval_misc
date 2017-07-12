import asyncio

async def gen():
    try:
        await asyncio.sleep(0.1)
        yield 'hello'
    except ZeroDivisionError:
        await asyncio.sleep(0.2)
        yield 'world'

async def async_main():
    g = gen()
    v = await g.asend(None)
    print(v)

    v = await g.athrow(ZeroDivisionError)
    print(v)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
loop.close()
