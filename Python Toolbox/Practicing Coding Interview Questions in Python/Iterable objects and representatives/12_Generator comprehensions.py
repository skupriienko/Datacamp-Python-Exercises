def func1(n):
    for i in range(0, n):
        yield i**2
def func2(n):
    for i in range(0, n):
        if i%2 == 0:
            yield 2*i
def func3(n, m):
    for i in func1(n):
        for j in func2(m):
            yield ((i, j), i + j)

# Rewrite func1() as a generator comprehension
gen = (i**2 for i in range(0, 10))

for item in zip(gen, func1(10)):
    print(item)

# Rewrite func2() as a generator comprehension
gen = (2*i for i in range(0, 20) if i%2 == 0)

for item in zip(gen, func2(20)):
    print(item)

# Rewrite func3() as a generator comprehension
gen = (((i,j), i+j) for i in func1(8) for j in func2(10))

for item in zip(gen, func3(8, 10)):
    print(item)