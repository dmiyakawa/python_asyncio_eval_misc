import time

def is_prime(val):
    print('is_prime({})'.format(val))
    if val < 2:
        return False
    return all(val % i for i in range(2, val))

values = [57_009_401, 39_526_741, 83_251_631, 29_920_507]
start = time.monotonic()
print([is_prime(val) for val in values])
end = time.monotonic()
print('{} sec'.format(end - start))
