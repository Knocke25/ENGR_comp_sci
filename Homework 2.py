from math import fabs, sin
from copy import deepcopy


def Secant(fcn, x0, x1, xtol=1e-5, maxiter=10):
    for i in range(maxiter):                            # go through max iterations
        x2 = x1 - (fcn(x1)*(x0-x1))/(fcn(x0)-fcn(x1))   # run calculation
        i += 1
        if fabs(x2-x1) < xtol:                          # test if the value is within tolerace
            return x2, i                                # returning values and index number
        x0 = x1
        x1 = x2
    return x2, i                                        # return incase it does not fit tolerance and maxiter


def Simpson(fcn, a, b, npoints):
    h = (b-a)/(npoints+1)                               # calc h value, npoints plus one because that makes it the even amount of rectangles
    ans = fcn(a) + fcn(b)                               # start calc for answer with first and last value because neither is multiplied
    for i in range(npoints):
        a = a + h                                       # step up
        if i % 2 == 0:                                  # check odd or even
            ans = ans + 4*fcn(a)
        else:
            ans = ans + 2*fcn(a)
    return (h/3)*ans                                    # finish the formula with summed answer


def GaussJacobi(Aaug, x, xtol= 1e-6, maxiter = 50):
    ans = [0] * len(Aaug)                                           # set initial answer list
    for n in range(maxiter):                                        # go through
        for i in range(len(Aaug)):                                  # go through the rows
            summ = 0
            for j in range(len(Aaug)):                              # go through columns
                if i !=j:
                    summ = summ - (Aaug[i][j])*x[j]                 # sum using the equation
                ans[i] = (Aaug[i][(len(Aaug))] + summ) / (Aaug[i][i])
        for q in range(len(ans)):
            if abs(ans[q]-x[q]) < xtol:                             # check tolerance
                return ans
            else:
                x[q] = ans[q]                                       # make x values the new answer list
    return ans

def main():
    # for part a)

    def f1(x):
        return x - 2 * sin(x)

    def f2(x):
        return (x - 2.5) * (x - 7) * (x - 4) * (x + 3)

    x0 = 1
    x1 = 2
    root, niter = Secant(f1, x0, x1)
    print('the root is: {:.6f} after {:d} iterations'.format(root, niter))

    root, niter = Secant(f2, x0, x1, xtol=0.001, maxiter=8)
    print('the root is: {:.6f} after {:d} iterations'.format(root, niter))

    root, niter = Secant(lambda x: (x - 1.523) * (x - 5), x0, x1, xtol=1e-4, maxiter=6)
    print('the root is: {:.6f} after {:d} iterations'.format(root, niter))

    root, niter = Secant(lambda x: x - 2 * sin(x), x0, x1, maxiter=2)
    print('the root is: {:.6f} after {:d} iterations'.format(root, niter))

    # for part b)

    a = 1
    b = 3
    nsteps = 81
    integral = Simpson(f1, a, b, nsteps)
    print('the integral of function 1 is: {:.5f} '.format(integral))

    a = 1
    b = 3
    nsteps = 8001
    integral = Simpson(f1, a, b, nsteps)
    print('the integral of function 1 is: {:.5f} '.format(integral))

    a = 1
    b = 3
    nsteps = 800001
    integral = Simpson(f1, a, b, nsteps)
    print('the integral of function 1 is: {:.5f} '.format(integral))

    a = 0
    b = 4
    nsteps = 11
    integral = Simpson(f2, a, b, nsteps)
    print('the integral of function 2 is: {:.2f} '.format(integral))

    # # for part c)

    MyA = [[4, -1, -1, 3],
           [-2, 6, 1, 9],
           [-1, 1, 7, -6]]

    MyX = [0, 0, 0]

    answer = GaussJacobi(MyA, MyX, maxiter=2)
    print("\n", answer)

    answer = GaussJacobi(MyA, MyX, maxiter=15)
    print(answer)


main()
