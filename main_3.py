#Mastering NumPy: 100 Exercises with solutions for Python numerical computing

import numpy as np

# Exercise 1:
# Create a 1D array with values ranging from 0 to 9.
# array = np.array(range(1,10))
# print(array)

# Exercise 2:
# Convert a 1D array to a 2D array with 2 rows.
# array = np.arange(10).reshape(2, -1)
# print(array)

# Exercise 3:
# Multiply a 5x3 matrix by a 3x2 matrix.
# matrix_1 = np.random.rand(5,3)
# matrix_2 = np.random.rand(3,2)
# result = np.dot(matrix_1, matrix_2)
# print(result)

# Exercise 4:
# Extract all odd numbers from an array of 1-10.
# arr = np.arange(1,11)
# for i in arr:
#     if i % 2 != 0:
#         print(i, end=" ")

# Exercise 5:
# Replace all odd numbers in an array of 1-10 with -1.
# arr = np.arange(1,11)
# arr[arr % 2 != 0] = -1
# print(arr)