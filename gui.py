### gui.py
import tkinter as tk
from tkinter import messagebox
from rocket import Rocket
from plots import plot_results

def run_simulation():
    try:
        thrust = float(entry_thrust.get())
        mass = float(entry_mass.get())
        isp = float(entry_isp.get())
        burn_time = float(entry_burn_time.get())

        rocket = Rocket(thrust=thrust, mass=mass, isp=isp, burn_time=burn_time)
        time, altitude, velocity, mass = rocket.simulate()

        plot_results(time, altitude, velocity, mass)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI setup
root = tk.Tk()
root.title("Rocket Flight Path Simulator")

tk.Label(root, text="Thrust (N):").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Mass (kg):").grid(row=1, column=0, sticky="e")
tk.Label(root, text="ISP (s):").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Burn Time (s):").grid(row=3, column=0, sticky="e")

entry_thrust = tk.Entry(root)
entry_mass = tk.Entry(root)
entry_isp = tk.Entry(root)
entry_burn_time = tk.Entry(root)

entry_thrust.grid(row=0, column=1)
entry_mass.grid(row=1, column=1)
entry_isp.grid(row=2, column=1)
entry_burn_time.grid(row=3, column=1)

tk.Button(root, text="Run Simulation", command=run_simulation).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
