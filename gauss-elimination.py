import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})


def gauss_elimination(matrix, b):
    L = np.zeros((3, 3), float)
    x_vector = np.zeros((3, 1), float)
    # print("-----multipliers-----")

    for i in range(2):
        for j in range(3):
            if i == j:
                for k in range(j + 1, 3):
                    multiplier = matrix[k][i] / matrix[i][i]
                    # print(multiplier)
                    matrix[k, :] = matrix[k, :] - multiplier * matrix[i, :]
                    b[k] = b[k] - multiplier * b[i]

    # print("-----after elimination transformation----- \n\n-----matrix A-----")
    # print(matrix)
    # print("\n-----vector b-----")
    # print(b)
    # inverse = np.linalg.inv(matrix)
    # print(matrix)

    print("-----After Back Substitution Phase-----\n\n-----vector x-----")
    # print(inverse.dot(b))
    x_vector[2] = b[2] / matrix[2][2]

    for i in range(1, -1, -1):
        eq = b[i]
        for j in range(i + 1, 3):
            eq = eq - matrix[i][j] * x_vector[j]
        x_vector[i] = eq / matrix[i][i]
    print(x_vector)


A1 = np.array([[2, -3, -1],
               [3, 2, -5],
               [2, 4, -1]], float)

B1 = np.array([[3],
               [-9],
               [-5]], float)

second_question = gauss_elimination(A1, B1)