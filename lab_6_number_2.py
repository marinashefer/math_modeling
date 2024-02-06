import matplotlib.pyplot as plt
import numpy as np

def giperbola(k):
    
    x = np.arange(.01, 10, 0.01)
    y = k/x

    plt.plot(x, y, label='my giperbola')
    plt.savefig('fig_6.png')

if __name__ == '__main__':
    giperbola(.2)