import inspect

def gen():
    for i in range(5):
        yield i

print('generator-function?: {}'
      .format(inspect.isgeneratorfunction(gen)))

g = gen()
print('generator?: {}'.format(inspect.isgenerator(g)))
for i in g:
    print(i)
