Rocket Flight Optimizer is a computer simulation and optimization tool that models how a rocket flies through the atmosphere and helps figure out the best way to launch it so it uses minimum fuel and minimum time to reach a desired altitude or orbit.
This helps aerospace engineers design better rockets, plan launches, and test different engine or fuel configurations before building or launching anything physically.

Optimizing flight path means:

-Using less fuel → cheaper launches

-Taking less time → faster missions

-Ensuring the rocket follows a safe and stable trajectory


Here's a quick guide to each file:

rocket.py: Simulates rocket physics and motion under thrust and gravity.

atmosphere.py: (Optional use for later) Returns air density by altitude.

optimizer.py: Uses SciPy to optimize thrust and ISP to minimize fuel per meter climbed.

plots.py: Plots altitude, velocity, and mass over time.

main.py: Brings it all together — runs the optimizer, simulates the rocket, and plots results.

Next Steps
Run main.py to see optimization in action.

Run gui.py to input values for desired simulation.


Output Explaination:
1. Altitude vs Time
What it shows:
How high the rocket has flown (in meters) at every point in time (seconds).

Why it matters:
This graph tells you the rocket’s vertical position and how quickly it’s climbing. The shape shows acceleration phases (steep slope means rapid climb) and if it reaches a stable altitude or falls back.

2. Velocity vs Time
What it shows:
How fast the rocket is moving upward (meters per second) over time.

Why it matters:
Velocity tells you how the rocket’s speed changes due to thrust, gravity, and drag. You can see when it accelerates, reaches max speed, or slows down if the engine stops.

3. Mass vs Time
What it shows:
How much mass the rocket has at each time instant (in kilograms).

Why it matters:
Rockets lose mass as fuel burns. This plot shows fuel consumption over time. The decreasing curve means the rocket is burning fuel to generate thrust.

How to interpret these graphs together:
-At the start, mass is maximum and velocity and altitude are zero.

-As fuel burns, mass decreases.

-The rocket’s velocity increases as thrust overcomes gravity.

-The altitude rises as velocity grows.

-When fuel runs out (mass stabilizes), velocity may peak and then decrease due to gravity and drag.

-These graphs let you evaluate how efficient the rocket is:

      ->Rapid altitude gain with minimal fuel loss is good.

      ->If mass drops quickly but altitude rises slowly, fuel efficiency might be poor.