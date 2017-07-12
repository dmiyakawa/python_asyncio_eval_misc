import inspect

def gen():
    yield 1

async def coro():
    return 0

g = gen()
print(inspect.iscoroutinefunction(gen),
      inspect.isgeneratorfunction(gen),
      inspect.iscoroutine(g),
      inspect.isgenerator(g))
c = coro()
print(inspect.iscoroutinefunction(coro),
      inspect.isgeneratorfunction(coro),
      inspect.iscoroutine(c),
      inspect.isgenerator(c))
