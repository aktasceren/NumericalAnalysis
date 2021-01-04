import numpy as np
import math


def cholesky_decomposition(matrix, b):
    L = np.zeros((3, 3), float)

    for j in range(3):
        for i in range(3):
            sum_of_elements = 0
            # for diagonal terms
            if i == j:
                for k in range(j):
                    sum_of_elements += L[j][k] ** 2
                L[j][j] = math.sqrt(matrix[j][j] - sum_of_elements)
                # for nondiagonal terms
            elif i > j:
                for k in range(j):
                    sum_of_elements += L[i][k] * L[j][k]
                L[i][j] = (matrix[i][j] - sum_of_elements) / L[j][j]
    # print("-----matrix L-----")
    # print(L)
    x_vector = lu_decomposition(L, b)
    print("\n-----x is equal-----")
    print(x_vector)


def transpose(matrix):
    transpose_of_matrix = np.zeros((3, 3), float)
    for i in range(3):
        for j in range(3):
            transpose_of_matrix[j][i] = matrix[i][j]
    # print("\n-----transpose of matrix L-----")
    # print(transpose_of_matrix)
    return transpose_of_matrix


def lu_decomposition(matrix, b):
    inverse_of_matrix = np.linalg.inv(matrix)
    inverse_of_transpose_of_matrix = np.linalg.inv(transpose(matrix))
    y = inverse_of_matrix.dot(b)
    # print("\n-----y is equal-----")
    # print(y)
    x = inverse_of_transpose_of_matrix.dot(y)
    return x


A2 = np.array([[1, 1, 1],
               [1, 2, 2],
               [1, 2, 3]])

B2 = np.array([[1],
               [1.5],
               [3]])

cholesky_decomposition(A2, B2)