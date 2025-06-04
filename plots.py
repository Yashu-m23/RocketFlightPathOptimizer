### plots.py
import matplotlib.pyplot as plt

def plot_results(time, altitude, velocity, mass):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(time, altitude)
    axs[0].set_title('Altitude vs Time')
    axs[0].set_ylabel('Altitude (m)')

    axs[1].plot(time, velocity)
    axs[1].set_title('Velocity vs Time')
    axs[1].set_ylabel('Velocity (m/s)')

    axs[2].plot(time, mass)
    axs[2].set_title('Mass vs Time')
    axs[2].set_ylabel('Mass (kg)')
    axs[2].set_xlabel('Time (s)')

    plt.tight_layout()
    plt.show()
