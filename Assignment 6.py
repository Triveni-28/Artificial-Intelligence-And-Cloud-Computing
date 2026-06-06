""" Assignment of 20th Feb """

import time
import numpy as np

size = 1000000

start = time.time()
py_list = list(range(size))
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python list time:", end - start)

start = time.time()
np_array = np.arange(size)
np_result = np_array * 2
end = time.time()
print("NumPy array time:", end - start)