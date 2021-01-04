import numpy as np

def doolittles_decomposition(matrix, b):
    L = np.array([[1, 0, 0],
                  [1, 1, 0],
                  [1, 1, 1]], float)
    U = matrix

    for i in range(2):
        for j in range(3):
            if i == j:
                for k in range(j + 1, 3):
                    multiplier = matrix[k][i] / matrix[i][i]
                    matrix[k, :] = matrix[k, :] - multiplier * matrix[i, :]
                    matrix[k][i] = multiplier
                    U[k][i] = 0
                    L[k][i] = multiplier

    # print(matrix)
    # print("----L----")
    # print(L)
    y = np.linalg.inv(L).dot(b)
    # print("-----y-----")
    # print(y)
    # print("----U----")
    # print(U)
    x = np.linalg.inv(U).dot(y)
    print("----x----")
    print(x)


A3 = np.array([[2.34, -4.10, 1.78],
               [-1.98, 3.47, -2.22],
               [2.36, -15.17, 6.18]], float)

B3 = np.array([[0.02],
               [-0.73],
               [-6.63]], float)

v = doolittles_decomposition(A3, B3)