from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np 

star_names = ['Benetnash','Mizar', 'Aliot', 'Megrez', 'Phekda','Merak','Dubhe']

#прямое восхождение и склонение:
#star_coords = {
#    'Aliot':(193, 55),
#    'Dubhe':(165, 61),
#    'Benetnash':(206, 49),
#    'Mizar':(200, 54),
#    'Merak':(165, 56),
#    'Phekda':(178, 53)
#}

def animate(time):
    alpha = np.array([206+(-121)*10**(-3)*time, 200+121*10**(-3)*time, 193+97*10**(-3)*time, 183+102*10**(-3)*time, 178+107*10**(-3)*time, 165+79*10**(-3)*time, 165+(-134)*10**(-3)*time, 183+102*10**(-3)*time,])/180*np.pi
    delta = np.array([49, 54, 55, 57, 53,56, 61, 57])/180*np.pi
    x = np.cos(delta) * np.cos(alpha)
    y = np.cos(delta) * np.sin(alpha)
    anim_object.set(x, y)
    plt.set_title(f'{time}')
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

alpha = np.array([206 ,200, 193, 183, 178, 165, 165, 183])/180*np.pi
delta =  np.array([49, 54, 55, 57, 53,56, 61, 57])/180*np.pi
x = np.cos(delta) * np.cos(alpha)
y = np.cos(delta) * np.sin(alpha)
plt.axis('equal')
plt.plot(x, y, 'o', color = 'b', label = 'star_name')
plt.plot(x, y, color='b', label='constellation', ms=1)

plt.savefig('star_name.png')
