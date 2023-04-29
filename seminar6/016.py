import random
rand_A = []
n = (int(input("Введите кол-во элементов списка: ")))
for i in range(n):
    rand_A.append(random.randint(-5,10))
print (*rand_A)

min = int(input("min: "))
max = int(input("max: "))    
    
for i in range(len(rand_A)):
    if min <= rand_A[i] <= max:
        print (i)

