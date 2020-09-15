"""Map example with lambdas"""


def square(element=0):
    return element * element


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(square, list_numbers))
print(result)

# With lambdas
result = list(map(lambda value: value + 1, list_numbers))
print(result)
