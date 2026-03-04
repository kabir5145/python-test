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
