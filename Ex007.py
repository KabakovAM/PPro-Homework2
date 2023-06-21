data = int(input('Введите число: '))
result_list = []
num_dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
print(hex(data))
while data != 0:
    temp = data - (data // 16) * 16
    if temp > 9:
        result_list.insert(0, num_dic[temp])
    else:
        result_list.insert(0, temp)
    data = data // 16
print(*result_list)
