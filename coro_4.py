import asyncio

async def async_main():
    for i in range(10):
        print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
loop.close()
