"""Receive a function as parameter - Example 2"""


def create_function(operator):
    if operator == '+':
        def sum_numbers(val1=0, val2=0):
            return val1 + val2

        return sum_numbers


def operation(function, val1=0, val2=0):
    return function(val1, val2)


sum_function = create_function('+')
result = operation(sum_function, 10, 20)
print(result)
