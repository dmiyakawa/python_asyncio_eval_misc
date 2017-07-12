import asyncio
import collections.abc
import inspect
import types

async def coro():
    return 1

def f1(g):
    yield from g

@asyncio.coroutine
def f2(g):
    yield from g
    
@types.coroutine
def f3(g):
    yield from g

loop = asyncio.get_event_loop()
    
for f in [f1, f2, f3]:
    g = f(coro())
    print(inspect.isgeneratorfunction(f),
          inspect.iscoroutinefunction(f),
          asyncio.iscoroutinefunction(f),
          '|',
          inspect.isgenerator(g),
          asyncio.iscoroutine(g),
          inspect.iscoroutine(g),
          isinstance(g, collections.abc.Coroutine),
          inspect.isawaitable(g))
    try:
        loop.run_until_complete(g)
    except TypeError as e:
        print('error: {}'.format(e))

loop.close()
