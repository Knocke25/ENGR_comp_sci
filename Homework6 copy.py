import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Problem(I,k,mjf,L,R,c,v):
    def ode_systemA(X,t,I,k,mjf,L,R,c,v):

        # define my constants
        # no forcing function equation

        f = X[0]; fdot = X[1]; i = X[2];                                    # Nice names

        #non-trivial data
        fddot = (1/I)*(mjf*i-c*fdot-k*f)
        idot = (1/L)* (v-mjf*fdot-R*i)
        return [fdot,fddot,idot]

    def ode_systemb(X,t,I,k,mjf,L,R,c,v):                                   # non linear damping
        # define my constants
        # no forcing function equation

        f = X[0]; fdot = X[1]; i = X[2];                                    # Nice names

        #non-trivial data
        fddot = (1/I)*(mjf*i-c*fdot**2*np.sign(fdot)-k*f)
        idot = (1/L)* (v-mjf*fdot-R*i)
        return [fdot,fddot,idot]

    t = np.linspace(0, 3, 200)                                              # Time goes from 0 to 3 seconds
    c1 = 10
    c2 = 100
    ic = [0, 0, 0]                                                          # Initial conditions
    x = odeint(ode_systemA, ic, t, args = (I,k ,mjf, L, R, c, v))           # derive for c = 50
    x2 = odeint(ode_systemA, ic, t, args = (I,k ,mjf, L, R, c1, v))          # derive for c = 10
    x3 = odeint(ode_systemA, ic, t, args = (I,k ,mjf, L, R, c2, v))         # derive for c = 100
    x1 = odeint(ode_systemb, ic, t, args = (I,k ,mjf, L, R, c, v))          # Non linear damping


# plots for i and F part 1

    plt.plot(t, x[:,0], 'b-', label = 'fx/dx')
    plt.xlabel('Time - s')
    plt.ylabel('Time warp flux')
    plt.title('Time warp flux vs. Time')
    plt.show()

    plt.plot(t, x[:,2], 'b-', label = 'fx/dx')
    plt.xlabel('Time - s')
    plt.ylabel('Temporal reluctance')
    plt.title('Temporal reluctance vs. Time')
    plt.show()

#
# #plots for i and F part 2
#
#     plt.plot(t, x2[:,0], 'r-', label = 'c=10')
#     plt.plot(t, x[:,0], 'b-', label = 'c=50')
#     plt.plot(t, x3[:,0], 'g-', label = 'c=100')
#     plt.legend(loc = 'lower right')
#     plt.xlabel('Time - s')
#     plt.ylabel('Time warp flux')
#     plt.title('Time warp flux vs. Time')
#     plt.show()
#
#     plt.plot(t, x2[:,2], 'r-', label = 'c=10')
#     plt.plot(t, x[:,2], 'b-', label = 'c=50')
#     plt.plot(t, x3[:,2], 'g-', label = 'c=100')
#     plt.legend(loc = 'lower right')
#     plt.xlabel('Time - s')
#     plt.ylabel('Temporal reluctance')
#     plt.title('Temporal reluctance vs. Time')
#     plt.show()
#
#
# #plots for i and F Part 3
#
#     plt.plot(t, x[:,0], 'b-', label = 'Linear')
#     plt.plot(t, x1[:,0], 'g-', label = 'NonLinear')
#     plt.legend(loc = 'lower right')
#     plt.xlabel('Time - s')
#     plt.ylabel('Time warp flux')
#     plt.title('Time warp flux vs. Time')
#     plt.show()
#
#     plt.plot(t, x[:,2], 'b-', label = 'Linear')
#     plt.plot(t, x1[:,2], 'g-', label = 'NonLinear')
#     plt.legend(loc = 'lower right')
#     plt.xlabel('Time - s')
#     plt.ylabel('Temporal Reluctance')
#     plt.title('Temporal Reluctance vs. Time')
    plt.show()

def main():
    I = 20
    k = 300
    mjf = 5
    L = 0.1
    R = 0.5
    c = 50
    v = 12
    Problem(I, k, mjf, L, R, c, v)
main()



