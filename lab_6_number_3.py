import matplotlib.pyplot as plt
import numpy as np

def allips(a=2, b=1):
    
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/a**2 + Y**2/b**2 - 1

    plt.contour(X, Y, fxy, levels=[0])

    plt.savefig('fig_7.png')

if __name__ == '__main__':
    allips()