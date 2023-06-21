data = int(input('Введите число: '))
data_2 = data
result_list = []
result_list_2 = []
print(bin(data))
print(oct(data_2))
while data != 0:
    result_list.insert(0, data - (data // 2) * 2)
    data = data // 2
while data_2 != 0:
    result_list_2.insert(0, data_2 - (data_2 // 8) * 8)
    data_2 = data_2 // 8
print(*result_list)
print(*result_list_2)
