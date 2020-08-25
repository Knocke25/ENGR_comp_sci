def GaussElim(Aaug):
    length = len(Aaug)                  # get length of matrix
    for i in range(0, length):
        max = (Aaug[i][i])
        for j in range(i + 1, length):
            if (Aaug[j][i]) > max:
                max = (Aaug[j][i])

        for j in range(1 + i, length):
            b = (-Aaug[j][i]) / (Aaug[i][i])
            for k in range(i, length + 1):
                if i == k:
                    Aaug[j][k] = 0
                else:
                    Aaug[j][k] += b * Aaug[i][k]

    x = [0] * length
    for i in range(length - 1, -1, -1):
        x[i] = Aaug[i][length] / (Aaug[i][i])
        for k in range(i - 1, -1, -1):
            Aaug[k][length] -= Aaug[k][i] * x[i]
    return x


def main():
    Matrix = ([2, 7, 3, 6, 2],
              [3, 3, 4, 4, 6],
              [6, 9, 5, 3, 3],
              [4, 2, 1, 7, 5])
    print('The x value solutions to the Gauss elimination are: ', GaussElim(Matrix))


main()


