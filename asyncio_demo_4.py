#
import asyncio
import datetime
import random


def notify_exit(signame):
    print("got signal %s: exit" % signame)
    # loop.stop()


@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print('Loop: {} Time: {}'.format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))
    print('Exiting {}'.format(num))


loop = asyncio.get_event_loop()

f1 = asyncio.ensure_future(display_date(1, loop))
f2 = asyncio.ensure_future(display_date(2, loop))

loop.run_until_complete(asyncio.wait([f1, f2]))
loop.close()
print('closed.')
