# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("введите длину шоколадки: "))
m = int(input("введите ширину шоколадки: "))
k = int(input("введите количество необходимых долей: "))
if (k % n == 0 or k % m == 0) and k < m*n:
    print("такое количество долей можно отломить")
else:
    print("так нельзя")
