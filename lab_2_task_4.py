stop = int(input('Введите число:'))
a = 1
b = 1
for _ in range(0, stop, 1):
    c = a + b
    a = b
    b = c
    print(c)