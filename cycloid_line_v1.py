"""
cycloid

x = r * (\theta - sin(\theta))
y = r * (1- cos(\theta))
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1, 2 * np.pi + 1)
ax.set_ylim(-0.5, 2.5)

r = 1
x, y = [], []
traj, = plt.plot([], [])
ax.add_artist(plt.Circle((0, 1), 1, fill=False))
ax.add_artist(plt.Circle((np.pi, 1), 1, fill=False))
ax.add_artist(plt.Circle((2 * np.pi, 1), 1, fill=False))

def update(t):
    x.append(r * (t - np.sin(t)))
    y.append(r * (1 - np.cos(t)))
    traj.set_data(x, y)
    if t > 6.28:
        sys.exit()

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi))
# ani.save('cycloid_line.gif')
plt.show()