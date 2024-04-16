from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

star_names = ['Benetnash','Mizar', 'Aliot', 'Megrez', 'Phekda','Merak','Dubhe']

def animate(time):
    alpha = np.array([206+(-121)*10**(-3)*time, 200+121*10**(-3)*time])/180*np.pi
    delta = np.array([49, 54])/180*np.pi
    print(alpha)
    print(delta)
    x = np.cos(delta) * np.cos(alpha)
    y = np.cos(delta) * np.sin(alpha)
    print(x)
    print(y)
    anim_object.set_data(x, y)
    # plt.set_title(f'{time}')


if __name__ == "__main__":
    fig, ax = plt.subplots()
    anim_object, = plt.plot([], [], 'o', color = 'b')

    edge = 1
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=10, interval=20)

    ani.save('star_name.gif')

