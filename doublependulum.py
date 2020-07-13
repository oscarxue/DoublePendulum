
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate  import odeint
from numpy import cos, sin

#Parameters
G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def acceleration(y0, t):

    dydx = np.zeros_like(state)  #create an array filled with zeros
    dydx[0] = y0[1]
    delta = y0 [2] - y0[0]



    x = y0[1]  # ANGULAR VELOCITY 1
    y = y0[2]  # THETA 2
    z = y0[0]  # theta 1
    w = y0[3]  # angular valocity 2

    n1 = M2 * L1 * x ** 2 * sin(delta)

    n2 = M2 * G * sin(y) * cos(delta)
    n3 = M2 * L2 * w ** 2 * sin(delta)
    n4 = -(M1 + M2) * G * sin(z)

    den1 = (M1 + M2) * L1 - M2 * L1 * (cos(delta)) ** 2

    dydx[1] = (n1 + n2 + n3 + n4) / den1

    dydx[2] = y0[3]

    b1 = -M2 * L2 * w ** 2 * sin(delta) * cos(delta)
    b2 = (M1 + M2)*(G * sin(z) * cos(delta) - L1 * x ** 2 * sin(delta) - G * (sin(y)))
    den2 = (M1 + M2) * L2 - M2 * L2 * (cos(delta)) ** 2

    dydx[3] = (b1 + b2) / den2




    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w1 and w2 are the initial angular velocities (degrees per second)
th1 = 45
w1 = 0.0
th2 = 45
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# solving the differential equation using odeint
y = odeint(acceleration, state, t)

theta1 = y[:,0]
theta2 = y[:,2]

print(y)

#plot the results
def plot_results(time,theta1,theta2):
    plt.plot(time,theta1)
    plt.plot(time,theta2)


    ps = ('M1 initial angle : ' + str(th1) + ' degrees\n ' + 'M2 initial angle : ' + str(th2) + 'degrees')
    plt.title('Double Pendulum motion\n' + ps )

    plt.xlabel('time in secs')
    plt.ylabel('angle in radians')
    plt.grid(True)
    plt.legend(['Mass 1', 'Mass 2'], loc='lower right')
    plt.show()

plot_results(t,theta1,theta2)

