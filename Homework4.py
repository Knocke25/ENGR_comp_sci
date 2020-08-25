import numpy as np, matplotlib.pyplot as plt


def cubicspline(x, f, k0, kf):
    h = x[1] - x[0]                                 # Find the steps

    A = np.zeros(shape=(len(x), len(f)))            # Get A matrix to multiply by each k value
    A[0][0] = 1
    A[len(x) - 1][len(f) - 1] = 1
    for i in range(1, len(x) -1):
        A[i][i] = 4
        A[i][i -1] = 1
        A[i][i +1] = 1

    S = np.zeros(len(x))                            # rhs
    S[0] = k0
    S[len(x)-1] = kf
    for i in range(1, len(x) -1):
        S[i] = (3/h)*(f[i+1] - f[i-1])

    k = np.zeros(len(x))
    k = np.linalg.solve(A,S)                        # solves A^(-1) * S to get k values


    j = np.zeros(len(x))
    for i in range(0, len(x)):                      # set values for j 0 .....n
        j[i] = i

    # set blank a matrix
    a = np.zeros(shape=(len(x)-1, len(x)))

    # solve for the cubic spline equations for a
    for j in range(0, len(a[0]) - 1):
        a[j][0] = f[j]
        a[j][1] = k[j]
        a[j][2] = (3/(h**2))*(f[j+1]-f[j]) - (1/h)*(k[j+1] + 2*k[j])
        a[j][3] = (2 / (h ** 3)) * (f[j] - f[j + 1]) + (1 / h**2) * (k[j + 1] + k[j])


    q = np.zeros(shape=(len(x) - 1,100))
    xvalues = np.zeros(shape=(len(x), 100))

    # calculate all x values
    for i in range(len(x)-1):
        for j in range(0,100):
            xvalues[i][j] = (h / 100) * (j) + x[i]

    # calculate the y values
    for j in range(0, len(x)-1):
        for i in range(0,100):
            q[j][i] = a[j][0] + (a[j][1]*(xvalues[j][i]-x[j])) + (a[j][2]*((xvalues[j][i]-x[j])**2)) + (a[j][3]*((xvalues[j][i]-x[j])**3))
        plt.plot(xvalues[j], q[j])          # plot each value after found
    plt.plot(x,f, 'bs')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Spline')
    plt.show()


def main():
    x = np.array([2, 4, 6, 8])
    f = np.array([4, 0, 4, 80])
    k_first = 0
    k_last = 20

    cubicspline(x,f,k_first,k_last)

    x2 = np.array([1.5, 3, 4.5, 6, 7.5, 9])
    f2 = np.array([3.5, 1.5, -2, 6.9, 8.2, 1.5])
    k_first2 = 2
    k_last2 = -4

    cubicspline(x2, f2, k_first2, k_last2)


main()