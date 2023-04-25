# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи


print("Введите число a:")
n = int(input())

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(n))