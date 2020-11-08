# map, filter, lambda

from functools import partial
from functools import reduce
def squarify(a):
    return a ** 2


list(map(squarify, range(5)))
squared_list = []

for number in range(5):
    squared_list.append(squarify(number))

print(squared_list)


def is_positive(a):
    return a > 0


list(filter(is_positive, range(-2, 3)))

positive_list = []

for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)

print(positive_list)

list(map(lambda x: x ** 2, range(5)))

type(lambda x: x ** 2)

list(filter(lambda x: x > 0, range(-2, 3)))

# функція перетворює список чисел у список рядків


def stringify_list(num_list):
    return list(map(str, num_list))


print(stringify_list(range(10)))

# functools


def multiply(a, b):
    return a * b


reduce(multiply, [1, 2, 3, 4, 5])

reduce(lambda x, y: x * y, range(1, 5))


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')


print(hier('brother'))
print(helloer('sir'))

# Списочные выражения
square_list = []
for number in range(10):
    square_list.append(number ** 2)

print(square_list)
# До этого момента мы с вами определяли списки стандартным способом, однако в питоне существует более красивая и лаконичная конструкция для создания списков и других коллекций.
square_list = [number ** 2 for number in range(10)]
print(square_list)

square_map = {number: number ** 2 for number in range(5)}

print(square_map)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
reminders_set = {num % 10 for num in range(100)}

print(reminders_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(number ** 2 for number in range(5)))
# <class 'generator'>
num_list = range(7)
squared_list = [x ** 2 for x in num_list]

list(zip(num_list, squared_list))
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]