async def coro():
    print('coro!')
    return 100

try:
    coro().send(None)
except StopIteration as e:
    print('StopIteration({}) sent'.format(e))
