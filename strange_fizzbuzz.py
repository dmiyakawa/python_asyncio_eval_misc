def fz(init_val):
    val = init_val
    while True:
        if val % 15 == 0:
            val = yield 'FizzBuzz'
        elif val % 3 == 0:
            val = yield 'Fizz'
        elif val % 5 == 0:
            val = yield 'Buzz'
        else:
            val = yield val
        if val > 15:
            return val

g = fz(1)
try:
    val = next(g)
    while True:
        print(g.send(val))
        val += 1

except StopIteration as e:
    print('StopIteration: {}'.format(e))
