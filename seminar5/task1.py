# 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, 
# состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
# Строка разбивается на минимальное количество подстрок, состоящих из одинаковых 
# символов. Например, abbcaaa превращается в строки a, bb, c, aaa.
# Каждая из полученных строк превращается в строку, состоящую из числа и буквы. 
# Числом является количество повторений символа в этой строке, буква берётся из 
# первого символа обрабатываемой строки. Число не добавляется, если количество 
# символов в строке равно единице. Из предыдущего массива строк мы получаем a, 2b, c, 3a.
# Затем полученные строки конкатенируются в исходном порядке. В рассмотренном 
# примере в итоге получим a2bc3a. Вводится строка, нужно сжать ее по алгоритму, описанному выше.

# n = int(input("Введите количество символов строки: "))
# some_list1 = list()
# for i in range(n):
#     some_list1.append(input('введите символ: '))
# print(some_list1)
some_string = input("Введите строку символов: ")
some_list2 = list()
count = 1
for i in range(len(some_string)-1):
    if some_string[i] == some_string[i+1]:
        count += 1
    elif count == 1:
        some_list2.append(some_string[i])
    elif count > 1:
        some_list2.append(some_string[i])
        some_list2.append(count)
        count = 1
some_list2.append(some_string[i+1])
if count != 1: some_list2.append(count)
print("".join(map(str, some_list2)))

# some_string = input("Введите строку символов: ")
# for i in range(len(some_string)-1):
#     if some_string[i] != some_string[i+1]:
#         some_string = some_string[:i] + ' ' + some_string[i+1:]
#         print(some_string)
# some_string.split()
# print(some_string)