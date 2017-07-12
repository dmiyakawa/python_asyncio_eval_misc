import asyncio
import random
import string
import time


@asyncio.coroutine
def gen_str_generator():
    while True:
        print('gen_random_str()')
        yield ''.join(s for s in random.choices(string.ascii_letters, k=5))


async def gen_str_native():
    while True:
        print('gen_random_str()')
        yield ''.join(s for s in random.choices(string.ascii_letters, k=5))


async def async_main():
    async for s in gen_str_native():
        print('generated: {}'.format(s))
        time.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
