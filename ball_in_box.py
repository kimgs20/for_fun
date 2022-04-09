import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')

x, y = 0, 0
vel_x, vel_y = 5, 2.5

def pos_upd():
    dt = 0.5
    if x > 10 or x < -10:
        vel_x = -vel_x
    if y > 10 or y < -10:
        vel_y = -vel_y
    
    x = vel_x * dt
    y = vel_y * dt
    return x, y

def update(i):
    ax.cla()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    x, y = pos_upd()
    ax.plot(x, y, 'bo')

ani = FuncAnimation(fig, update, frames=np.linspace(0, 12))
plt.show()
"""
UnboundLocalError: local variable 'x' referenced before assignment
"""