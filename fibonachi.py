def fib_generator(val):
    a, b = 0, 1
    for __ in range(val):
        yield a
        a, b = b, a + b

print(list(fib_generator(35)))