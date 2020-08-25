# Imports
from scipy import integrate
import numpy as np
from math import cos,pi,sin
import matplotlib.pyplot as plt


def FourierCoeff(func,L,n):
    A = np.zeros(shape = (n+1,2))                                   # create empty matrices
    B = np.zeros(shape = (n+1,2))

    def f(x):
        return (1/2*L)*func(x)
    a_0=integrate.quad(f,-L,L)
    for j in range(1, n+1):                                         # Odd or even function
        def F1(x): return (1/L)*func(x)*cos(j*pi*x/L)

        def F2(x): return (1/L)*func(x)*sin(j*pi*x/L)
        A[j]=integrate.quad(F1, -L, L)
        B[j]=integrate.quad(F2, -L, L)
        # end of loop

    ans_A=np.array(A[0:n+1,0])                                      # Store answers are first column of quad output due
    ans_B=np.array(B[0:n+1,0])                                      # quad having two ouputs
    ans_A[0] = a_0[0]
    return ans_A, ans_B


def PlotFourier(A1,B1,L,xmin,xmax,npoints=5000):
    x = np.linspace(xmin, xmax, npoints)                            # create array for plotting points
    ans = 0

    def fourier(x):
        return A1[j] * np.cos(j * pi * x / L) + B1[j] * np.sin(j * pi * x / L)
    for j in range(1,len(A1)):
        ans = ans + fourier(x)                                      # getting the sum of the answers
    ans = ans + A1[0]                                               # adding first term to the total answer
    plt.plot(x,ans)                                                 # plot x vs y(ans)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.show()


def main():
    def Shark(x):
        if x<0: return (x+1)**2
        else: return 1-x**2

    L=1
    a,b=FourierCoeff(Shark,L,10)
    print(a,"\n",b,"\n")
    PlotFourier(a, b, L,  -3 * L, 3 * L)

    L = np.pi
    a, b = FourierCoeff(lambda x: x, L, 8)
    print(a, "\n", b, "\n")
    PlotFourier(a, b, L, -4*L, 4*L, npoints=10000)

main()