# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
rand_A = []
n = (int(input("Введите кол-во элементов списка А: ")))
for i in range(n):
    rand_A.append(random.randint(0,9))
print (*rand_A)
X = int(input("Введите число для поиска: "))
m = abs(X - rand_A[0])
index = 0
for i in range(0, n):
    count = abs(X - rand_A[i])
    if count < m:
        m = count
        index = i
print (rand_A[index])
