# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input('Введите количество монет: '))
count_0 = 0
count_1 = 0
for i in range(n):
    side = int(input('Введите сторону монеты(0 - решко, 1 - орёл): '))
    if side == 0:
        count_0 += 1
    else:
        count_1 +=1
if count_0 > count_1:
    print(f'Нужно перевернуть {count_0 - count_1} монеток')
else:
     print(f'Нужно перевернуть {count_1 - count_0} монеток')
