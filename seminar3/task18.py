# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

number_array = int(input('Введите количество элементов массива: '))
list_1 = list()
for i in range(number_array):
    x = int(input('Введите элемент массива - '))
    list_1.append(x)
number_x = int(input('Введите некоторое число - '))
k = 0
min = abs(list_1[0] - number_x)
for i in range(number_array):
    if abs(list_1[i] - number_x) < min:
        min = abs(list_1[i] - number_x)
        k = i
print(list_1, number_x, list_1[k])