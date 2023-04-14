# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
import random

print("Введите количество монет")
sum = int(input())
numbers = list()
reshka = 0
orel = 0
for i in range(sum):
    numbers.append(random.randint(0, 1))
    if numbers[i] == 1:
        reshka += 1
    else:
        orel += 1
print("Монеты:")
print(numbers)
if reshka < orel:
    print(f"надо перевернуть {reshka} монеты c решкой")
else:
    print(f"надо перевернуть {orel} монеты c орлом")
