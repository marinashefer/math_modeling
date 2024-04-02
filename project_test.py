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

alpha = np.array([206 ,200, 193, 183, 178, 165, 165, 183])/180*np.pi
delta =  np.array([49, 54, 55, 57, 53,56, 61, 57])/180*np.pi
x = np.cos(delta) * np.cos(alpha)
y = np.cos(delta) * np.sin(alpha)
plt.axis('equal')
plt.plot(x, y, 'o', color = 'b', label = 'star_name')
plt.plot(x, y, color='b', label='constellation', ms=1)

plt.savefig('star_name.png')

