from decimal import Decimal
import math
data = 0
while data > 1000 or data < 1:
    data = int(input('Введите диаметр окружности: '))
result = Decimal(math.pi * (data / 2) ** 2)
print(result)