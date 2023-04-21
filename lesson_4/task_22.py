# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.
import random
print("Введите минимальное число массива :")
numb_min = int(input())

print("Введите максимальное  число массива :")
numb_max = int(input())

print("Введите количество чисел в массиве :")
number = int(input())

list_1 = list()
list_2 = list()

for i in range(number):
    list_1.append(random.randint(numb_min, numb_max))

for i in range(number):
    list_2.append(random.randint(numb_min, numb_max))


list_1 = set(list_1)
list_2 = set(list_2)

result = list_1.union(list_2)
print(result)


