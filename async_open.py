import asyncio

async def async_main():
    with open(__file__) as f:
        

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(async_main())
finally:
    loop.close()
