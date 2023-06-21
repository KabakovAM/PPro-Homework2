import math
import cmath

print('Введите коэффициенты для уравнения ax^2 + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
dis = b ** 2 - 4 * a * c
if dis > 0:
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print(f'x1 = {x1}\nx2 = {x2}')
elif dis == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + cmath.sqrt(dis)) / (2 * a)
    x2 = (-b - cmath.sqrt(dis)) / (2 * a)
    print(f'x1 = {x1}\nx2 = {x2}')
