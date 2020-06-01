# list loops
values = ['a', 'b', 'c', 'd', 'e']

for value in values:
    print(value)

[print(value) for value in values]

# tuple loops
values = ('a', 'b', 'c', 'd', 'e')

for value in values:
    print(value)

[print(value) for value in values]

# dictionary loops
values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 20}

for key, value in values.items():
    print(f"{key} {value}")
