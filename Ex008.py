import fractions
data = input('Введите первую дробь: ')
data_2 = input('Введите вторую дробь: ')
list = data.split('/')
list_2 = data_2.split('/')
sum_list = (int(list[0]) * int(list_2[1]) + int(list_2[0]) * int(list[1]), '/', int(list[1]) * int(list_2[1]))
mult_list = (int(list[0]) * int(list_2[0]), '/', int(list[1]) * int(list_2[1]))
sum_list_check = fractions.Fraction(data) + fractions.Fraction(data_2)
mult_list_check = fractions.Fraction(data) * fractions.Fraction(data_2)
print(*sum_list)
print(sum_list_check)
print(*mult_list)
print(mult_list_check)




