import numpy as np

g = 10

def func(m, h, v):
    first = m*g*h
    second = m*v**2/2
    energy = first + second
    print(energy)
    
func(20, 60, 85)