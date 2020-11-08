def fib(n):

    if n < 2:
        return (n, 1)

    fib1 = fib(n-1)
    fib2 = fib(n-2)

    return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)


print(fib(15))
print(fib(20))
