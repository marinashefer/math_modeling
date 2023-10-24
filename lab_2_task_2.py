first = int(input('Первый член:'))
second = int(input('Знаменатель :'))
third = int(input('Количество членов :'))

for n in range(0, third, 1):
    a = first * (second ** (n - 1))
    print(a)
