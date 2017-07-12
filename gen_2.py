import inspect

def gen():
    return
    for i in range(5):
        yield i

g = gen()
print('generator?: {}'.format(inspect.isgenerator(g)))
for i in g:
    print(i)
