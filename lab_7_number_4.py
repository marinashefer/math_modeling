from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

d = 0.33
c = 0.3
x0 = 0.01
y0 = 0.01

xdata, ydata = [], []
xdata.append(x0)
ydata.append(y0)

def animate(i):
    xdata.append(xdata[i-1]**2 - ydata[i-1]**2 + c)
    ydata.append(2 * xdata[i-1] * ydata[i-1] + d)
    anim_object.set_data(xdata, ydata)
    return anim_object,

if __name__ == "__main__":
    fig, ax = plt.subplots()
    anim_object, = plt.plot([], [], 'o', color = 'g', label = 'Ball')

    edge = 1
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=range(1, 100), interval=50)

ani.save('animation_6.gif')