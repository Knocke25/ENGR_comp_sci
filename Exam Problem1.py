def SumOfAllNegatives(Amatrix):
    summ = 0
    for i in Amatrix:
        for j in i:
            if j < 0:
                summ = summ + j
    return summ


def main():
    A1 = ([1, 2, 3],
          [5, -6, 7],
          [-9, 10, -11])

    A2 = ([0, 0, -8, 0],
          [0, 0, 0, 0],
          [0, -2, 0, 0],
          [-1, 0, 0, 0])

    print('Sum of all negative values in A1 is: {:.2f} '.format(SumOfAllNegatives(A1)))
    print('Sum of all negative values in A2 is: {:.2f} '.format(SumOfAllNegatives(A2)))

main()