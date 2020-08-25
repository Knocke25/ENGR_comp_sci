# Imports numpy, copy
import numpy as np
import copy


def Determinant(A):
    n = len(A)                                              # length of matrix
    ans = 0                                                 # set initial answer so set up variable
    if n > 2:                                               # for anything higher than 2x2 matrix
        t = 0                                               # indexing
        i = 1
        while t < n:                                        # Go through each column
            coeff = A[0][t]                                 # pick up coefficient
            d = Determinant(Submatrix(A, 0, t))             # Get determinant of the smaller matrix
            ans += coeff * d * i
            t += 1                                          # index up
            i *= -1                                         # i is used to add or subtract values
        return ans
    else:                                                   # this is a 2x2 matrix
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def Submatrix(A, x, y):
    sub = np.delete(A, x, axis = 0)                         # delete x row
    sub = np.delete(sub, y, axis = 1)                       # delete y column
    return sub


def Cramers(a, b):
    n = len(a)                                              # length of matrix
    ans = [0] * n                                           # set answer array full of zeros
    DET = Determinant(a)                                    # find the whole matrix determinant
    for i in range(0,n):                                    # for each column.....
        copyofmatrix = copy.deepcopy(a)                     # create new copy so that original is not messed up
        for j in range(0,n):                                # input b matrix into a matrix for each row
            copyofmatrix[j][i] = b[j]
        littleans = Determinant(copyofmatrix)               # get matrix of newly created matrix and set as little ans
        ans[i] = (littleans)/DET                            # set corresponding ans as little ans / overall determinant
    return ans


def main():
    A = np.array([[ 1, -2,  3,  4],
                  [ 5,  6,  7,  8],
                  [-9, 10, -11, 6],
                  [ 5,  4, -3,  2]])

    b = np.array([1, 2, 3,  4])
    print(Submatrix(A,1,2))
    print(Determinant(A))
    print(Cramers(A,b))

    A = np.array([[-5,  1, -5, 0,  1, -4],
                  [ 5,  0,  3, 5,  3,  5],
                  [-2, -2,  1, 4,  3, -5],
                  [ 4,  5,  0, 3,  4, -1],
                  [-5, -2, -5, 5, -2, -2],
                  [ 4,  5,  5, 0,  0, -2]])

    b = np.array([99, 45, 49, -50, -90, 30])
    print("\n", Submatrix(A,1,2))
    print("\n", Determinant(A))
    print("\n", Cramers(A,b))


main()