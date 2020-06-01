# list loops
values = ['a', 'b', 'c', 'd', 'e']

for value in values:
    print(value)

[print(value) for value in values]
[value for value in values if value == 'a']

# tuple loops
values = ('a', 'b', 'c', 'd', 'e')

for value in values:
    print(value)

[print(value) for value in values]

for idx, value in enumerate(values):
    print(f"{idx} {value}")

# dictionary loops
values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 20}

for key, value in values.items():
    print(f"{key} {value}")
