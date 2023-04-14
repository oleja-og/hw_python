# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие
# числа N.
#


print("Введите число :")
numb = int(input())
a = 2
for i in range(numb):
    if a ** i > numb:
        break
    print(a ** i, end=" ")
print()
