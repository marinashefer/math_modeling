import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('Snake_Nebula.jpg')
fig, ax = plt.subplots()
ax.imshow(img)
x = [550, 440]
y = [2000, 620]

t = np.linspace(np.pi/2 + np.pi/6, np.pi/2 - np.pi/6, 100)
x = 340 + 85*np.cos(t)
y = 300 + 80*np.sin(t)
ax.plot(x,y,lw = 2, color = 'r')

t = np.linspace(np.pi/2 + np.pi/6, np.pi/2 - np.pi/6, 100)
x = 460 + 35*np.cos(t)
y = 1 + 320*np.sin(t)
ax.plot(x,y,lw = 2, color = 'r')

t = np.linspace(2*np.pi,np.pi ,100 )
x = 410 + 35 *np.cos(t)
y = 300 + 70 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'r')

t = np.linspace(2*np.pi,np.pi ,100 )
x = 410 + 35 *np.cos(t)
y = 300 + 70 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'r')

t = np.linspace(2*np.pi,np.pi ,100 )
x = 410 + 65 *np.cos(t)
y = 273 + 75 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'r')


t = np.linspace(2*np.pi,np.pi ,100 )
x = 234 + 65 *np.cos(t)
y = 365 + 70 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'r')



x = [380, 385, 385, 375, 378]
y = [370, 350, 345, 320, 300]

plt.plot(x,y,lw = 2, color = 'r')
plt.ylim()
plt.savefig('snake.png')