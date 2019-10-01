import sys
import numpy as np
from scipy.integrate import odeint


# The gravitational acceleration (m.s-2).
g = 9.81


def deriv(y, t, L1, L2, m1, m2):
    """Return the first derivatives of y = theta1, z1, theta2, z2."""
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    theta1dot = z1
    z1dot = (m2 * g * np.sin(theta2) * c - m2 * s * (L1 * z1**2 * c + L2 * z2**2) -
             (m1 + m2) * g * np.sin(theta1)) / L1 / (m1 + m2 * s**2)
    theta2dot = z2
    z2dot = ((m1 + m2) * (L1 * z1**2 * s - g * np.sin(theta2) + g * np.sin(theta1) * c) +
             m2 * L2 * z2**2 * s * c) / L2 / (m1 + m2 * s**2)
    return theta1dot, z1dot, theta2dot, z2dot


class Pendulum:
    def __init__(
        self,
        theta1=3*np.pi/7,
        theta1_dot=0,
        theta2=3*np.pi/4,
        theta2_dot=0,
        noise_scale=1e-3):

        # Initial state
        self.y0 = np.array([
            theta1 + np.random.normal(scale=noise_scale),
            theta1_dot,
            theta2 + np.random.normal(scale=noise_scale),
            theta2_dot
        ])

        # Pendulum rod lengths (m), bob masses (kg).
        self.L1, self.L2 = 1, 1
        self.m1, self.m2 = 1, 1

    def calc_E(self, y):
        """Return the total energy of the system."""

        th1, th1d, th2, th2d = y.T
        V = -(self.m1 + self.m2) * self.L1 * g * np.cos(th1) - self.m2 * self.L2 * g * np.cos(th2)
        T = 0.5 * self.m1 * (self.L1 * th1d)**2 + 0.5 * self.m2 * ((self.L1 * th1d)**2 + (self.L2 * th2d)**2 +
                2 * self.L1 * self.L2 * th1d * th2d * np.cos(th1 - th2))
        return T + V

    def simulate(self, max_t, dt):
        ts = np.arange(0, max_t + dt, dt)

        # Do the numerical integration of the equations of motion
        y = odeint(deriv, self.y0, ts, args=(self.L1, self.L2, self.m1, self.m2))

        # Check that the calculation conserves total energy to within some tolerance.
        EDRIFT = 0.05
        # Total energy from the initial conditions
        E = self.calc_E(self.y0)
        if np.max(np.sum(np.abs(self.calc_E(y) - E))) > EDRIFT:
            sys.exit('Maximum energy drift of {} exceeded.'.format(EDRIFT))

        # Unpack z and theta as a function of time
        theta1, theta2 = y[:, 0], y[:, 2]

        # Convert to Cartesian coordinates of the two bob positions.
        self.x1 = self.L1 * np.sin(theta1)
        self.y1 = -self.L1 * np.cos(theta1)
        self.x2 = self.x1 + self.L2 * np.sin(theta2)
        self.y2 = self.y1 - self.L2 * np.cos(theta2)

