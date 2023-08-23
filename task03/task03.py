# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числавида 2k), не превосходящие числа N.
# input: 10 -> output: 1 2 4 8

n = int(input("Введите число: "))

count = 1
num = 1

while num < n:
    print(num, end=" ")
    num = 2**count
    count += 1