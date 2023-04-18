# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8


import random

print("Введите число N(количество чисел в массиве) :")
n = int(input())
numbers = list()
count = 0
while True:
    print("Введите число A(число которое ищем в массиве) :")
    a = int(input())
    if a < 0 or a > 9:
        print("Введите число от 0 до 9")
    else:
        break

for i in range(n):
    numbers.append(random.randint(0, 9))
active = True
while active:
    for i in numbers:
        if a - count == i or a + count == i:
            print(f"Число {i} ближе всего к {a}")
            active = False
            break
    count += 1

print(numbers)
