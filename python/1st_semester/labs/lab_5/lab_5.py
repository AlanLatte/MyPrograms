# -*- coding: utf-8 -*-
import numpy as np
import random, math
try:
    sum_or_subtraction = None
    m = int ( input( 'Укажите количество столбцов: \n'))
    n = int ( input( 'Укажите количество строк: \n'))
    matrix_a = np.random.randint(100, size=(n,m))
    matrix_b = np.random.randint(100, size=(n,m))
    print('Задание№1\n________________\nСложение или вычитание матриц?')
    output = str(input('\n1)+\n2)-\n'))
    if output == "1" or output == "+":
        matrix_c = matrix_a + matrix_b
        sum_or_subtraction = " \n+\n "
    elif output == "2" or output == "-":
        matrix_c = matrix_a - matrix_b
        sum_or_subtraction = " \n-\n"
    print("________________\n"+ str(matrix_a) + "\n"+ sum_or_subtraction + "\n" + str(matrix_b) + "\n=\n" + str(matrix_c) + "\n________________\nЗадание№2")
    transpose_matrix_a = np.transpose(matrix_a)
    print(str(matrix_a) + "\n\n" + str(transpose_matrix_a))
except:
    print('Ты не прав.')
