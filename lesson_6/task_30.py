# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print("Введите  число a :")
a = int(input())

print("Введите  число n :")
n = int(input())

print("Введите  число d :")
d = int(input())

numbers = list()
a_n = 0
for i in range(1,n+1):
    numbers.append(a+(i-1)*d)
print(numbers)
