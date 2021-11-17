def f(n):
    if n > 0:
        print(n, end='')
        f(n - 1)


print(f(5))
