
#Output from Google's Gemini.

import numpy as np
import matplotlib.pylab as plt

#Objective: simulate the motion of a ball bouncing on the ground.

gravity = 9.81
height = 10
bounce_factor = 0.8

time = np.arange(0, 3, 0.01)
# Remember, origin (inclusive), stop (not inclusive), and step
# Len(time) = 300
position = np.zeros_like(time)

#np.zeros_like() will copy the format of the given ndarray, and fill it with zeros.

current_height = height
for i in range(len(time)):
    position[i] = current_height
    current_height = current_height - 0.5 * gravity * time[i]**2
    if current_height < 0:
        current_height = current_height * -bounce_factor


plt.plot(time,position)
plt.xlabel("Time (milliseconds)")
plt.ylabel("Height (meters)")
plt.title("Bouncing Ball Simulation")
plt.show()

#What's wrong with the code?
"""
The ball is not "bouncing" properly. Once the height reaches zero, 
the if statement is fulfilled. The if statement references the current height
rather than the initial height, leading to this weird growth in height. 

"""