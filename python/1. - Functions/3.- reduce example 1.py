"""Reduce examples"""
from functools import reduce

numbers = [1, 2, 3, 4]
accumulator = 0

for element in numbers:
    accumulator += element

print(accumulator)


# With reduce
def accumulator_function(acc=0, e=0):
    return acc + e


result = reduce(accumulator_function, numbers)
print(result)

# With lambda

result = reduce(lambda accum=0, elem=0: accum + elem, numbers)
print(result)

# With lists

values_list = ['Python', 'Java', 'Php', 'Dart', 'Javascript']
result = reduce(lambda acc='', el='': acc + " - " + el, values_list)

print(result)
