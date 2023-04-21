# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств

#Решение 1:
firstnumb = {1, 2, 3, 5, 8}
secondnumb = {2, 5, 8, 13, 21}
result = sorted(firstnumb.intersection(secondnumb)) 
print (result)

#Решение 2:
from random import randint
firstnumb = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(firstnumb)
secondnumb = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(secondnumb)
result = sorted(firstnumb.intersection(secondnumb))
print(*result)