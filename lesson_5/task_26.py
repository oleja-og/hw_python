# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число
# (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов


# def factor(n, a):
#     if n != 1:
#         a *= n
#         n -= 1
#     else:
#         return a
#     return factor(n,a)

def factor(n):
    if n == 1:
        return n
    return n*factor(n-1)

print("Введите число :")
n = int(input())
a = 1

print(factor(n))
