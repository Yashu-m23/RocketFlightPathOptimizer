### rocket.py
import numpy as np

g0 = 9.81  # gravitational acceleration in m/s^2

class Rocket:
    def __init__(self, thrust, mass, isp, burn_time):
        self.thrust = thrust      # Newtons
        self.mass = mass          # kg
        self.isp = isp            # seconds
        self.burn_time = burn_time  # seconds

    def mass_flow_rate(self):
        return self.thrust / (self.isp * g0)

    def simulate(self, dt=0.1):
        time = [0]
        altitude = [0]
        velocity = [0]
        mass = [self.mass]

        mfr = self.mass_flow_rate()
        t = 0
        y = 0
        v = 0
        m = self.mass

        while t <= self.burn_time and m > 0:
            a = (self.thrust - m * g0) / m  # basic thrust minus weight
            v += a * dt
            y += v * dt
            m -= mfr * dt

            time.append(t)
            altitude.append(y)
            velocity.append(v)
            mass.append(m)

            t += dt

        return np.array(time), np.array(altitude), np.array(velocity), np.array(mass)