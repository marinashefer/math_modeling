import numpy as np

def func(massive):
    a = 1
    for i in massive:
        a = a * i
    return a 

mass1 = [2, 8, 40, 60]
mass2 = np.array(mass1)
print(func(mass2))