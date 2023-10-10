first = int(input('Первый член:'))
second = int(input('Знаменатель :'))
third = int(input('Количество членов :'))

a = first * (second ** (third - 1))
print('Геометрическая прогрессия: ', a)
