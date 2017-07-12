import asyncio


async def spam(n):
    await asyncio.sleep(0.1)
    return f'spam:{n}'


async def pred(n):
    return n % 2


async def spam_restrant():
    print({n: await spam(n) for n in range(5) if await pred(n)})

loop = asyncio.get_event_loop()
loop.run_until_complete(spam_restrant())
