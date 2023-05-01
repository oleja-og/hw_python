# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]


import random
print("Введите количествов элементов в массиве:")
numb = int(input())
print("Введите минимальное значение:")
min_numb = int(input())
print("Введите максимальное значение:")
max_numb = int(input())
numbers = list()
count_list = list()
for i in range(numb):
    numbers.append(random.randint(-10, 10))
print(numbers)
count = 0
for i in range(len(numbers)):
    if numbers[i] >= min_numb and numbers[i] <= max_numb:
        count_list.append(count)
    count += 1
print(count_list)

