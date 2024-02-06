import matplotlib.pyplot as plt
import numpy as np

def logspiral(b=0.1):

    f = np.arange(.01, 10, 0.01)
    e = 2.718
    a = b * f
    r = e**a

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='my logspiral')
    plt.savefig('fig_8.png')

if __name__ == '__main__':
    logspiral(.2)