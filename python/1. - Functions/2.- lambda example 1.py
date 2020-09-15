"""Basic example with lambda functions"""

sum_numbers = lambda val1=0, val2=0: val1 + val2
operation = lambda operation, val1=0, val2=0: operation(val1, val2)

result = operation(sum_numbers, 10, 20)

print(result)
