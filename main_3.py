#Mastering NumPy: 100 Exercises with solutions for Python numerical computing

import numpy as np

# Exercise 14:
# Stack two arrays vertically.
# array_1 = np.array([1,2,3])
# array_2 = np.array([4,5,6])
# stack_arr = np.vstack((array_1,array_2))
# print(stack_arr)


# Exercise 15:
# Get the common items between two arrays.
# arr_1 = np.array([[1,2,3,4,5,6]])
# arr_2 = np.array([7,8,9,10,5,6])
# common_items = np.intersect1d(arr_1, arr_2)
# print(common_items)

# Exercise 16:
# Create a 5x5 matrix with row values ranging from 0 to 4.
# matrix = np.zeros((5,5))
# matrix += np.arange(5)
# print(matrix)

# Exercise 17:
# Find the index of the maximum value in a 1D array.
# array = np.array([1,2,10,3,4,5,6,7,0])
# find_index = array.argmax()
# print(find_index)

# Exercise 18:
# Normalize the values in a 1D array between 0 and 1.
arr = np.array([2, 5, 10, 3, 8])
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print(normalized_arr)