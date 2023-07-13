# 3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

n = int(input("Введите количество элементов списка: "))
some_list = list()
for i in range(n):
    some_list.append(input('введите элемент списка: '))
print(some_list)

dict1 = {}
count = 1
for i in range(n):
    if some_list[i] not in dict1:
        dict1[some_list[i]] = 1
for i in range(n):
    for j in range(n):
        if i != j and some_list[i] == some_list[j]:
            count +=1
            dict1[some_list[i]] = count
    count = 1
        
print(dict1)
maxx = max(dict1, key = dict1.get)
print(f'максимальное количество одинаковых элементов {dict1.get(maxx)}')