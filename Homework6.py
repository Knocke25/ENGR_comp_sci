from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# define constants
I = 20
k = 300
mjf = 5
L = 0.1
R = 0.5
c = 50
v = 12

def ode_system_one(X, t, I, k, mjf, L, R, c, v):
    # Make names for the initial conditions, nice
    f = X[0];
    fdot = X[1];
    i = X[2];

    # re-arranged DE's
    fddot = (1 / I) * (mjf * i - c * fdot - k * f)
    idot = (1 / L) * (v - mjf * fdot - R * i)
    return [fdot, fddot, idot]                  # make sure these are in same order

def ode_system_two(X, t, I, k, mjf, L, R, c, v):
    # Make names for the initial conditions, nice
    F = X[0];
    Fdot = X[1];
    i = X[2];

    # re-arrange DE's
    Fddot = (1 / I) * (mjf * i - c * Fdot ** 2 * Fdot - k * F)
    idot = (1 / L) * (v - mjf * Fdot - R * i)
    return [Fdot, Fddot, idot]



t = np.linspace(0, 3, 200)  # Time from 0 to 3 seconds with 200 data points
c1 = 10
c2 = 100
ic = [0, 0, 0]  # Initial conditions
x = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c, v))  # c = 50
x2 = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c1, v))  # c = 10
x3 = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c2, v))  # c = 100
x1 = odeint(ode_system_two, ic, t, args=(I, k, mjf, L, R, c, v))  # Non linear damping

def main(eqn, t, I, k, mjf, L, R, c, v):

    # define constants
    I = 20
    k = 300
    mjf = 5
    L = 0.1
    R = 0.5
    c = 50
    v = 12

    t = np.linspace(0, 3, 200)  # Time from 0 to 3 seconds with 200 data points
    c1 = 10
    c2 = 100
    ic = [0, 0, 0]  # Initial conditions
    x = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c, v))  # c = 50
    x2 = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c1, v))  # c = 10
    x3 = odeint(ode_system_one, ic, t, args=(I, k, mjf, L, R, c2, v))  # c = 100
    x1 = odeint(ode_system_two, ic, t, args=(I, k, mjf, L, R, c, v))  # Non linear damping



# Part 1

plt.plot(t, x[:,0], 'r-', label='fx/dx')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Time warp flux')
plt.title('Time warp flux vs. Time')
plt.show()

plt.plot(t, x[:,2], 'r-', label='fx/dx')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Temporal reluctance')
plt.title('Temporal reluctance vs. Time')
plt.show()



# Plot 2

plt.plot(t, x2[:,0], 'b-', label='c=10')
plt.plot(t, x[:,0], 'g-', label='c=50')
plt.plot(t, x3[:,0], 'r-', label='c=100')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Time warp flux')
plt.title('Time warp flux vs. Time')
plt.show()

plt.plot(t, x2[:,2], 'b-', label='c=10')
plt.plot(t, x[:,2], 'g-', label='c=50')
plt.plot(t, x3[:,2], 'r-', label='c=100')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Temporal reluctance')
plt.title('Temporal reluctance vs. Time')
plt.show()


#plots for i and F Part 3

plt.plot(t, x[:,0], 'r-', label='Linear')
plt.plot(t, x1[:,0], 'g-', label='NonLinear')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Time warp flux')
plt.title('Time warp flux vs. Time')
plt.show()

plt.plot(t, x[:,2], 'r-', label='Linear')
plt.plot(t, x1[:,2], 'g-', label='NonLinear')
plt.legend(loc='best')
plt.xlabel('Time - seconds')
plt.ylabel('Temporal Reluctance')
plt.title('Temporal Reluctance vs. Time')
plt.show()