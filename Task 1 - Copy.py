""" Task 13th Feb"""
import numpy as np

my_list = [1, 2, 4, 5, 6, 7]
numpy_array = np.array(my_list)
print("Numpy Array:", numpy_array)

temperature = np.array([43, 65, 75, 67, 78])

print("Maximum temperature:", np.max(temperature))
print("Minimum temperature:", np.min(temperature))
print("Average temperature:", np.mean(temperature))
print("Last 3 days temperature:", temperature[-3:])
