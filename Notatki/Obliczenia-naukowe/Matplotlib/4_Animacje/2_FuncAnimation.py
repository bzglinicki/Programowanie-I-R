import matplotlib.pyplot as plt
from math import sin, pi
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], "ro")

def init():
    ax.set_xlim(0, 2*pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame/10)
    ydata.append(sin(frame/10))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames = None,
                    init_func = init, blit = True)

plt.show(block = True)