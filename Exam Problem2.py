import copy


def det2(A):
    ans = (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
    return ans


def solve2(A, b):
    D = det2(A)
    Atemp = copy.deepcopy(A)
    Atemp[0][0] = b[0][0]
    Atemp[1][0] = b[1][0]
    dx1 = (det2(Atemp))/D
    Atemp1 = copy.deepcopy(A)
    Atemp1[0][1] = b[0][0]
    Atemp1[1][1] = b[1][0]
    dx2 = (det2(Atemp1))/D
    x = ([dx1], [dx2])
    return x


def main():
    A1 = ([1, -3],
          [2, -4])

    b1 = ([-1],
          [1])

    A2 = ([2, -2],
          [5, -4])

    b2 = ([2],
          [-3])

    print('Solution set of A1 matrix set is =', solve2(A1, b1))
    print('Solution set of A2 matrix set is =', solve2(A2, b2))


main()