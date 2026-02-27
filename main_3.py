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

# Exercise 6:
# Convert a 1D array to a boolean array where all positive values become True.
# array = np.array([-1,0,1,2])
# bool_array = array > 0
# print(bool_array)

# Exercise 7:
# Replace all even numbers in a 1D array with their negative.
# array = np.arange(1,11)
# array[array % 2 == 0 ] = -array[array % 2 == 0]
# print(array)

# Exercise 8:
# Create a random 3x3 matrix and normalize it.
# matrix = np.random.random((3,3))
# normalized_matrix = (matrix - np.mean(matrix)) / np.std(matrix)
# print(normalized_matrix)

# Exercise 9:
# Calculate the sum of the diagonal elements of a 3x3 matrix.
# matrix = np.random.random((3,3))
# print(matrix)
# sum_of_diagonal = np.trace(matrix)
# print(sum_of_diagonal)

# Exercise 10:
# Find the indices of non-zero elements from [1,2,0,0,4,0].
# array = np.array([1,2,0,0,4,0])
# non_zero_indices = np.nonzero(array)
# print(non_zero_indices)

# Exercise 11:
# Reverse a 1D array (first element becomes the last).
# array = np.arange(1,11)
# reverse_array = np.flip(array)
# print(reverse_array)

# Exercise 12:
# Create a 3x3 identity matrix.
# identity_matrix = np.eye(3)
# Or
# identity_matrix = np.identity(3)
# print(identity_matrix)

# Exercise 13:
# Reshape a 1D array to a 2D array with 5 rows and 2 columns.
# array = np.arange(10)
# arr = array.reshape(5,2)
# print(arr)