#комплексные переменные(complex)
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)

print(z + w)

# строки
s = 'hello'
print(s[0])

# s[0] = 'H'

# tuple
t = (1, 4, 9)
print(t)
print(t[0])
# t[0] = 3

#словарь(dict)
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d['a1'])
print(d[4])
print(d['str'])

d['str'] = 'Goood'
print(d)