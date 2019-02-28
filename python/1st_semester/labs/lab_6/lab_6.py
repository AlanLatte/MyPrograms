# -*- coding: utf-8 -*-
import numpy as np
import random, shutil, math
from math import log, tan, pi, sqrt
def apend(result):
    with open(r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_6/result.txt','a') as apended_text:
        apended_text.write(result)
def lab_1():
    try:
        z1 = a**(sqrt(log(a,b)))-b**(sqrt(log(b,a)))+tan(a*b+(3*pi/2))
        z2 = tan(a*b+(3*pi)/2)
        apend(result=("Z1 = " + str(z1) + "\n" +"Z2 = " + str(z2)))
    except:
        print('ОДЗ!')
def lab_5():
    sum_or_subtraction = None
    matrix_a = np.random.randint(100, size=(n,m))
    matrix_b = np.random.randint(100, size=(n,m))
    try:
        if output == "1" or output == "+":
            matrix_c = matrix_a + matrix_b
            sum_or_subtraction = " \n+\n "
        elif output == "2" or output == "-":
            matrix_c = matrix_a - matrix_b
            sum_or_subtraction = " \n-\n"
        apend(result=("\n________________\n"+ str(matrix_a) + "\n"+ sum_or_subtraction + "\n" + str(matrix_b) + "\n\n=\n\n" + str(matrix_c) + "\n________________\n\nЗадание№2\n________________\n"))
        transpose_matrix_a = np.transpose(matrix_a)
        apend(result=(str(matrix_a) + "\n\n" + str(transpose_matrix_a)))
    except:
        apend(result='\nОшибка ввода.')
def lab_4():
    massive = []
    massive_absol=[]
    result1=0
    result2=1
    try:
        if y > math.fabs(5):
            123
        else:
            for i in range(massive_quantity):
                massive.append(random.randint(-5,5))
            if y not in massive:
                massive.remove(massive[random.randrange(massive_quantity)])
                massive.append(y)
            for i in massive:
                massive_absol.append(int(math.fabs(i)))
            for i in massive_absol:
                if i < y:
                    result1+=i
            for i in massive_absol:
                if i > y:
                    result2*=i
            if result2 == 1:
                result2 = "Max."
            apend(result=("\n________________\n\nЗадание№3\n________________\nсумма элементов меньше y: " + str(result1) + "\nумножение элементов больше y: " + str(result2)))
    except:
        print('Некроектность ввода')
def create_new_file():
    with open (r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_6/inputs.txt','w') as new_file, open (r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_6/result.txt','w') as result_txt:
        new_file.write('Введите значение А: \nВведите значение В: \nУкажите количество столбцов: \nУкажите количество строк: \nСложение или вычитание матриц? \n1) Сложение \n2) Вычитание \nОтвет: \nВведите количество элементов массива: \nВведите Y [-5:5]\nОтвет: ')
with open (r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_6/inputs.txt','r') as inputs:
    a = inputs.readline()
    a = int(''.join(a for a in a if a.isdigit()))
    b = inputs.readline()
    b = int(''.join(b for b in b if b.isdigit()))
    m = inputs.readline()
    m = int(''.join(m for m in m if m.isdigit()))
    n = inputs.readline()
    n = int(''.join(n for n in n if n.isdigit()))
    for i in range(3):
        inputs.readline()
    output = inputs.readline()
    output = ''.join(output for output in output if output.isdigit())
    massive_quantity = inputs.readline()
    massive_quantity = int(''.join(massive_quantity for massive_quantity in massive_quantity if massive_quantity.isdigit()))
    inputs.readline()
    y = inputs.readline()
    y = int(''.join(y for y in y if y.isdigit()))
create_new_file()
lab_1()
lab_5()
lab_4()
