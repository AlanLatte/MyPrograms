# -*- coding: utf-8 -*-
import random, math
massive = []
massive_absol=[]
# n = 5
n = int(input("Введите количество элементов массива: \n"))
result1=0
result2=1
for i in range(n):
    massive.append(random.randint(-5,5))
while True:
    # y = 5
    y = int(input("Введите y (элемент массива в диапазоне от [-5:5]): \n"))
    if -5 <= y  and y <= 5:
        if y not in massive:
            massive.remove(massive[random.randrange(n)])
            massive.append(y)
            break
        else:
            break
for i in massive:
    massive_absol.append(int(math.fabs(i)))
for i in massive_absol:
    if i < y:
        result1+=i
for i in massive_absol:
    if i > y:
        result2*=i
if result2 == 1:
    result2 = "None"
# print(massive)
# print(massive_absol)
print("сумма элементов меньше y: " + str(result1))
print("умножение элементов больше y: " + str(result2))
