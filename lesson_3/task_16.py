# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
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
    if numbers[i] == a:
        count += 1
print(numbers)
print(f"Число {a} встречается {count} раз")
