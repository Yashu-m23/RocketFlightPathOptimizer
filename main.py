### main.py
from rocket import Rocket
from optimizer import optimize_rocket
from plots import plot_results

if __name__ == "__main__":
    best_params, score = optimize_rocket()
    print(f"Optimal parameters: Thrust = {best_params[0]:.2f} N, ISP = {best_params[1]:.2f} s")
    print(f"Optimization score (fuel per meter): {score:.6f}")

    rocket = Rocket(thrust=best_params[0], mass=500, isp=best_params[1], burn_time=50)
    time, altitude, velocity, mass = rocket.simulate()

    plot_results(time, altitude, velocity, mass)
