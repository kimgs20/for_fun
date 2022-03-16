import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81
vo_x = 10
vo_y = 50
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 200)
ax.set_ylim(-150, 150)

x, y = [], []
traj, = plt.plot([], [])

def update(t):
    x.append(vo_x * t)
    y.append(vo_y * t - (g * (t ** 2) / 2))
    traj.set_data(x, y)

ani = FuncAnimation(fig, update, frames=np.linspace(0, 12))
ani.save('ball_trajectory.gif')
# plt.show()