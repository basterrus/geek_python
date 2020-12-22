from itertools import cycle

numbers = [1, 'Слово', True, 0x2255]


for el1 in cycle(numbers):
    print(el1)
