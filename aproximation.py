import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = [1, 2 , 3]
y = [7, 9, 7]
ax.plot(x, y, '-',lw = 2, color = 'k')

t = np.linspace(np.pi/2 + np.pi/6,np.pi/2 - np.pi/6,100 )
x = 4 + 2*np.cos(t)
y = 5.25 + 2*np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

x = [5, 6 , 7]
y = [7, 9, 7]
ax.plot(x, y, '-',lw = 2, color = 'k')

t = np.linspace(2*np.pi,np.pi ,200 )
x = 4 + 3*np.cos(t)
y = 7 + 5*np.sin(t)
ax.plot(x, y, '-',lw = 2, color = 'k')

t = np.linspace(np.pi/2 + np.pi/6,np.pi/2 - np.pi/6,100 )
x = 3 + 1.25 *np.cos(t)
y = 4.28 + 2*np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

t = np.linspace(np.pi/2 + np.pi/6,np.pi/2 - np.pi/6,100 )
x = 5 + 1.25 *np.cos(t)
y = 4.28 + 2*np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

t = np.linspace(2*np.pi,np.pi,100  )
x = 3 + 0.65 *np.cos(t)
y = 6 + 0.6 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

t = np.linspace(2*np.pi,np.pi ,100 )
x = 5 + 0.65 *np.cos(t)
y = 6 + 0.6 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

x = [3.25, 4 , 4.8, 3.25]
y = [5, 4, 5, 5]
ax.plot(x, y, '-',lw = 2, color = 'k')

t = np.linspace(2*np.pi,np.pi ,100 )
x = 4 + 0.65 *np.cos(t)
y = 3.8 + 0.6 *np.sin(t)
ax.plot(x, y ,'-',lw = 2, color = 'k')

plt.axis('equal')
plt.savefig('KILL.png')