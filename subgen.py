def fz5(val):
    for i in range(5):
        if val % 15 == 0:
            yield 'FizzBuzz'
        elif val % 3 == 0:
            yield 'Fizz'
        elif val % 5 == 0:
            yield 'Buzz'
        else:
            yield val
        val = val + 1
    return val

def fz(initial):
    ret = yield from fz5(initial)
    ret = yield from fz5(ret)
    ret = yield from fz5(ret)
    return ret

g = fz(1)
try:
    val = next(g)
    while True:
        print(val)
        val = g.send(val)
except StopIteration as e:
    print('StopIteration:{}'.format(e))
