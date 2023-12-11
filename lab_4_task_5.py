import numpy as np

a = int(input('Введите название фигуры:'))

def func(a, r = 1, h = 8, r = 5,c = 9,b = 6):
    if a == 'круг' :
        def square (r):
            s = 3.14 * r**2
            print(s)
        square(5)
    elif a == 'треугольник':
        def square (h, r):
            s = h*r/2
            print(s)
        square(8,84)
    else: 
        def square(c, b):
            s = c*b
            print(s)
        square(7, 8)