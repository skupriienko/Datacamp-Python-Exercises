import math
# Convert these three normally defined functions into lambda expressions:

# Returns a bigger of the two numbers
def func1(x, y):
    if x >= y:
        return x

    return y

# Convert func1() to a lambda expression
lambda1 = lambda x, y: x if x >= y else y
print(str(func1(5, 4)) + ', ' + str(lambda1(5, 4)))
print(str(func1(4, 5)) + ', ' + str(lambda1(4, 5)))

# Returns a dictionary counting charaters in a string
def func2(s):
    d = dict()
    for c in set(s):
        d[c] = s.count(c)
    return d

# Convert func2() to a lambda expression
lambda2 = lambda s: dict([(c, s.count(c)) for c in set(s)])
print(func2('DataCamp'))
print(lambda2('DataCamp'))


# Returns a squared root of a sum of squared numbers
def func3(*nums):
    squared_nums = [n**2 for n in nums]
    sum_squared_nums = sum(squared_nums)

    return math.sqrt(sum_squared_nums)

# Convert func3() to a lambda expression
lambda3 = lambda *nums: math.sqrt(sum([n**2 for n in nums]))
print(str(func3(3, 4)) + ', ' + str(lambda3(3, 4)))
print(str(func3(3, 4, 5)) + ', ' + str(lambda3(3, 4, 5)))
