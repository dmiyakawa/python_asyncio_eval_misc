def foo(n):
    if n in (0, 1):
        return [1]
    for item in range(n):
        yield item * 2

print(list(foo(0)))  # []
print(list(foo(1)))  # []
print(list(foo(2)))  # [0, 2]
