# Задача 24:
import random
print("Введите количество кустов:")
numb = int(input())
branches = list()
max_result = 0
result = 0
for i in range(numb):
    branches.append(random.randint(1, 100))
print(branches)
branches.extend(branches[0:2])
print(branches)
for i in range(numb):
    result = sum(branches[i:i+3])
    if result >= max_result:
        max_result = result

print(max_result)
