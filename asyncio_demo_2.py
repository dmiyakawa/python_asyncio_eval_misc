#
# http://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
#
import asyncio
import datetime
import functools
import random
import signal


def notify_exit(signame):
    print("got signal %s: exit" % signame)
    loop.stop()


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

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame),
                            functools.partial(notify_exit, signame))

loop.run_forever()
