# NumPy Matrix Operations and Linear Algebra Exercises

import numpy as np

# 1. Matrix Multiplication
# Write a NumPy program to compute the multiplication of two given matrix.

# matrix_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# matrix_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# for i in range(3):
#     for j in range(3):
#         print(matrix_1[i][j],end=" ")
#     print()
#
# for i in range(3):
#     for j in range(3):
#         print(matrix_2[i][j],end=" ")
#     print()
#
# mul = np.matmul(matrix_1,matrix_2)
# for i in range(3):
#     for j in range(3):
#         print(mul[i][j],end=" ")
#     print()

# 2. Outer Product of Vectors
# Writes a NumPy program to compute the outer product of two given vectors.

# p = [[1, 0], [0, 1]]
# q = [[1, 2], [3, 4]]
#
# print("Original matrices:")
# for row in p:
#     for val in row:
#         print(val, end=" ")
#     print()
#
# print()
#
# for row in q:
#     for val in row:
#         print(val, end=" ")
#     print()
#
# result = np.outer(p, q)
#
# print("Outer product of the said two vectors:")
# for row in result:
#     for val in row:
#         print(val, end=" ")
#     print()

# 3. Cross Product of Vectors
# Write a NumPy program to compute the cross product of two given vectors.

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[5,6,7],[8,9,10]])
#
# print("Original Matrix")
# print(a)
# print(b)
#
# cross_product = np.cross(a,b)
# print(cross_product)

# 4. Determinant of a Square Array
# Write a NumPy program to compute the determinant of a given square array.

# arr = np.array([[1,2],
#                [3,4]])
#
# print("Original Array:")
#
# for i in range(2):
#     for j in range(2):
#         print(arr[i][j],end=" ")
#     print()
#
# determinant = np.linalg.det(arr)
# print("Determinant of the array is : ",determinant)


# 5. Einstein Summation Convention
# Write a NumPy program to evaluate Einstein's summation convention of two given multidimensional arrays.

# a = np.array([1,2,3])
# b = np.array([0,1,0])
#
# result =  np.einsum("n,n", a, b)
# print("Einstein’s summation convention of the said arrays:")
# print(result)
#
# # Create two 3x3 arrays 'x' and 'y'
# x = np.arange(9).reshape(3, 3)
# y = np.arange(3, 12).reshape(3, 3)
#
# # Display the original higher-dimensional arrays 'x' and 'y'
# print("Original Higher dimension:")
# print(x)
# print(y)
#
# # Compute the Einstein’s summation convention of the 2-D arrays 'x' and 'y' using np.einsum()
# result = np.einsum("mk,kn", x, y)
# print("Einstein’s summation convention of the said arrays:")
# print(result)


# 6. Inner Product of Vectors
# Writes a NumPy program to compute the inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension.

# a = np.array([1, 2, 5])
# b = np.array([2, 1, 0])
#
# inner_product = np.dot(a, b)
# print(inner_product)