"""Basic example with lambda functions"""

without_params = lambda: True
print(without_params())

with_params = lambda val, val1=10, val2=10: val + val1 + val2
print(with_params(val=5))

with_asterisk = lambda *args: args[0]
print(with_asterisk(5))

with_doble_asterisk = lambda **kwargs: kwargs
print(with_doble_asterisk(a=1))

with_asterisks = lambda *args, **kwargs: kwargs.get('key', False)
print(with_asterisks())
