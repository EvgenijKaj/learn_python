# 2.Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

n = int(input("Введите количество символов строки: "))
some_list = list()
for i in range(n):
    some_list.append(input('введите символ: '))
print(some_list)

max = some_list[1]
count = 1
number = 1
while count < len(some_list)-1:
    if some_list[count] > some_list[count-1] and some_list[count] > some_list[count+1]:
        number = count
        max = some_list[count]
    count += 1
print(f'Номер последнего локального максимума равен {number}, max = {some_list[number]}')
