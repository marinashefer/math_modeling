from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

star_names = ['Aliot', 'Dubhe', 'Benetnash',  'Mizar', 'Merak', 'Phekda']

#прямое восхождение и склонение:
#star_coords = {
#    'Aliot':(193, 55),
#    'Dubhe':(165, 61),
#    'Benetnash':(206, 49),
#    'Mizar':(200, 54),
#    'Merak':(165, 56),
#    'Phekda':(178, 53)
#}

def animate(i):
    alpha = [193, 165, 206, 200, 165, 178]
    betta = [55, 61, 49, 54, 56, 53]
    for angle1 in alpha:
        x = np.cos(betta) * np.cos(alpha)
    for angle2 in betta:
        y = np.cos(betta) * np.sin(alpha)
    anim_object.set(x, y)
    return anim_object,

if __name__ == "__main__":
    fig, ax = plt.subplots()
    anim_object, = plt.plot([], [], 'o', color = 'b', label = 'star_name')

    edge = 1
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=100, interval=20)

    ani.save('star_name.gif')