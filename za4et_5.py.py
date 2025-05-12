def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b
