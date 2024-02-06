import matplotlib.pyplot as plt
import numpy as np

def logspiral(a=0.1):

    f = np.arange(.01, 10, 0.01)
    p = 3.14
    r = a/2*p * f

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='my logspiral')
    plt.savefig('fig_9.png')

if __name__ == '__main__':
    logspiral(.1)