import numpy as np
import matplotlib.pyplot as plt

# Constants
gravity = -9.81   # m/s^2
initial_height = 10      # Initial height (meters)
initial_velocity = 0     # Starting at rest
bounce_factor = 0.8  # Energy retained after each bounce

# Time setup
time = np.arange(0, 3, 0.01)  # Time array

# Displacement calculation
height_values = np.zeros_like(time)
velocity_values = np.zeros_like(time)
kinetic_energies = np.zeros_like(time)
current_velocity = initial_velocity

for i in range(len(time)):
    # displacement = 0.5*gravity**time[i]
    velocity = gravity*time[i]
    velocity_values[i] = velocity
    kinetic_energies[i] = 0.5*(velocity**2)
    # height_values[i] = initial_height-displacement

print(velocity_values)
print(kinetic_energies)
plt.plot(time, velocity_values)
plt.show()
# Plotting
# plt.plot(time, displacement)
# plt.xlabel("Time (seconds)")
# plt.ylabel("Displacement (meters)")
# plt.title("Bouncing Ball Simulation")
# plt.show()

