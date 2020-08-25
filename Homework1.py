def ArraySumNegative(vals):
    sumneg= 0   # defines summation and starts at zero
    for i in vals:  # loop for all variables within the array
        if i < 0:
            sumneg = sumneg + abs(i)
    return sumneg


def MatrixSumLarge(vals,large):
    summatrix = 0
    for i in vals:
        for j in i:
            if abs(j) >= large:
                summatrix = summatrix + abs(j)
    return summatrix


def Horner(x, coeffs):
    ans = 0
    for i in range(len(coeffs)-1, -1, -1):
        ans = (ans * x) + coeffs[i]
    return ans


def interp1D(x, xvals, yvals):

    increment = 0
    for i in xvals:
        if i > x:
            minx = xvals[increment - 1]
            miny = yvals[increment - 1]
            maxx = xvals[increment]
            maxy = yvals[increment]
            slope = (maxy - miny) / (maxx - minx)
            inc = x - minx
            aa = slope * inc
            y = aa + miny
            return y
        increment += 1


def main():
    # define the variables needed to test the required functions
    myvals =  [1, -1, 2, -3.5, 8.5]
    mymatrix = [[1, -2.5, 7, 4],
               [-8, 9, 2, -1.5],
               [-12, 7.5, 4.2, 11]
                ]
    a = [3, 2, -2, 4]
    xvals = [1, 3, 5, 6, 7]
    yvals = [2, 4, 1, 4, 3]
    x1 = 2.5
    mylarge = 7.1
    x2 = 6.5
    # for part a)
    mysum1 = ArraySumNegative(myvals)
    print('a) Sum of negatives = {:.1f}'.format(mysum1))
    # for part b)
    mysum2 = MatrixSumLarge(mymatrix, mylarge)
    print('b) Sum of large values = {:.1f}'.format(mysum2))
    # for part c)
    poly = Horner(x1, a)
    print('c) Polynomial value for (x1= {:.2f}) = {:.1f}'.format(x1, poly))
    # for part d)
    y = interp1D(x2, xvals, yvals)
    print('d) Interpolated value for (x2= {:.2f}) = {:.1f}'.format(x2, y))




main()