import numpy as np
from numpy import array



def read_integers(filename):
    with open(filename) as f:
        return [x for x in next(f).split(':')]

array = read_integers('text.txt')

array = array[:-1]

print(array)

new_array = [1 * len(array)]

for j, i in enumerate(array):
    new_array[j] = i


print(new_array)
