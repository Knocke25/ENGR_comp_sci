import math


def Norm(x):
    ans = (1/(math.sqrt(2*math.pi)))*math.e**((-(x**2))/2)
    return ans


def Simpson(fcn, a, b, npoints = 1000):
    h = (b-a)/(npoints+1)                               # calc h value, npoints plus one because that makes it the even amount of rectangles
    ans = fcn(a) + fcn(b)                               # start calc for answer with first and last value because neither is multiplied
    for i in range(npoints):
        a = a + h                                       # step up
        if i % 2 == 0:                                  # check odd or even
            ans = ans + 4*fcn(a)
        else:
            ans = ans + 2*fcn(a)
    return (h/3)*ans


def Secant(fcn, x0, x1, xtol=1e-5, maxiter=100):
    for i in range(maxiter):                            # go through max iterations
        x2 = x1 - (fcn(x1)*(x0-x1))/(fcn(x0)-fcn(x1))   # run calculation
        i += 1
        if math.fabs(x2-x1) < xtol:                          # test if the value is within tolerance
            return x2                                # returning values and index number
        x0 = x1
        x1 = x2
    return x2


def CumNorm(xvals):
    def fcn(x): return Norm(x)
    ans = Simpson(fcn, -5, xvals)
    return ans


def InvCumNorm(givenValue):
    def fcn(x): return CumNorm(x) - givenValue
    ans = Secant(fcn, givenValue, 1)
    return ans


def main():
    print('The value of the normal function is: {:.6f}'.format(Norm(1.5)))
    print('The value of the cumulative normal function is: {:.6f}'.format(CumNorm(1.5)))
    print('Back solving gives the value: {:.6f}'.format(InvCumNorm(.9)))


main()