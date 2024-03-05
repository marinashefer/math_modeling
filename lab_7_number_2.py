from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

def circle_move(time):
    R = 0.02 * time 
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(time = i))

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color = 'r', label = 'Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=100, interval=30)

    ani.save('animation_4.gif')