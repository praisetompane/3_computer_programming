import numpy as np
import time
import sys

number_of_elements = 1000
slist = range(number_of_elements)
nparray = np.arange(number_of_elements)

print(f'standard list memory size: {sys.getsizeof(slist)}')
print(f'numpy array memory size: {sys.getsizeof(nparray)}')
print(f'numpy array memory size: {nparray.size*nparray.itemsize}')
