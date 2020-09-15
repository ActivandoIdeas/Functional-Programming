"""Filter example with lambda"""


def major_to_five(element):
    return element > 5


numbers = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
result = tuple(filter(major_to_five, numbers))
result = result
print(result, " len ", len(result))

result = tuple(filter(lambda element: element > 5, numbers))
print(result)
