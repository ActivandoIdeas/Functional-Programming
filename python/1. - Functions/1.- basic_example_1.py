"""Receive a function as parameter - Example 1"""


def sum_numbers(val1=0, val2=0):
    return val1 + val2


def operation(function, val1=0, val2=0):
    return function(val1, val2)


sum_function = sum_numbers

result = operation(sum_function, 10, 20)
print(result)
