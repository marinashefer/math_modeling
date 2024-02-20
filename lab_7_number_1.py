import matplotlib.pyplot as plt
import numpy as np

def cirloida(a=1,t=3):
    t = np.arange(0, 8, 0.01)

    x = a*(t - np.sin(t))
    y = a*(1 - np.cos(t))

    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('cicloida.png')

if __name__ == '__main__':
    cirloida()