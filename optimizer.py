### optimizer.py
from scipy.optimize import minimize
from rocket import Rocket
import numpy as np

def objective(x):
    thrust, isp = x
    rocket = Rocket(thrust=thrust, mass=500, isp=isp, burn_time=50)
    t, y, v, m = rocket.simulate()
    final_altitude = y[-1]
    fuel_used = 500 - m[-1]
    return fuel_used / final_altitude  # minimize fuel per meter

def optimize_rocket():
    bounds = [(1000, 20000), (100, 450)]
    result = minimize(objective, [5000, 300], bounds=bounds)
    return result.x, result.fun