from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

star_names = ['Aliot', 'Dubhe', 'Benetnash',  'Mizar', 'Merak', 'Phekda']

star_coords = {
    'Aliot'(97, -2),
    'Dubhe'(-134, -35),
    'Benetnash'(-121, 15),
    'Mizar'(121, -22),
    'Merak'(79, 32),
    'Phekda'(107, 11)
}

def animate(i):
    alpha = [97, -134, -121, 121, 79, 107]
    betta = [-2, -35, 15, -22, 32, 11]
    for angle1 in alpha:
        x = np.cos(betta) * np.cos(alpha)
    for angle2 in alpha:
        y = np.cos(betta)  * np.sin(alpha)
    anim_object.set(x, y)
    return anim_object,

if name == "main":
    plt.figure(figsize=(10, 6))
    anim_object, = plt.plot([], [], 'o', color = 'b', label = star_name)

    edge = 1
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=50)

ani.save('star_name.gif')
