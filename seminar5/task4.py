# 4.Создайте список из случайных чисел. Найдите второй максимум.

# a = [1, 2, 3] # Первый максимум == 3, второй == 2

n = int(input("Введите количество случайных чисел: "))
some_list = list()
for i in range(n):
    some_list.append(int(input('введите число: ')))
print(some_list)

maxx_1 = some_list[0]
maxx_2 = 0
for i in range(n):
    if maxx_1 < some_list[i]:
        maxx_2 = maxx_1
        maxx_1 = some_list[i]
    elif maxx_2 < some_list[i] and maxx_1 > some_list[i]:
        maxx_2 = some_list[i]
    
print(f'Первый максимум {maxx_1}, второй максимум {maxx_2}')