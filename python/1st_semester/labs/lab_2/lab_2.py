# -*- coding: utf-8 -*-
from math import *
import math
try:
    x = int(input("Введите значние X: \n"))
    if x <=-2.5: y = -6/7*x-36/7
    elif -2.5<x and x<2: y = x**3 + 1.5*x**2-2.5*x-3
    elif 2<=x: y = -2*x + 10
    print("X={0:.2f}   Y={1:.2f}".format(x,y))
except:
    print('Ошибка ввода.')
print("\n____________________\nЗадание№2\n")
def two_four():
    if x>0 and y<0 and y<x-RADUIS:
        true()
    elif (x<0 and y>0) and y>x+RADUIS:
        true()
    else:
        error()
def error():
    print('Точка не принадлежит области')
def true():
    print('Точка принадлежит области')
def one_three():
    if x<0 and y<0 and y<-x-RADUIS:
        true()
    elif x>0 and y>0 and y>-x-RADUIS:
        true()
    else:
        error()
try:
    RADUIS = int(input('Введите радиус: \n'))
    x = int(input('Введите значение X: \n'))
    y = int(input('Введите значение Y: \n'))
    po_r = sqrt(x**2+y**2)  # point_radius
    if math.fabs(x)<=RADUIS and math.fabs(y)<=RADUIS:
        if po_r<=RADUIS:
            if (x<0 and y>0) or (y<0 and x>0): #первая и четвертая четверть
                two_four()
            else:
                error()
        elif po_r>=RADUIS:
            if (y>0 and x>0) or (x<0 and y<0):
                one_three()
            else:
                error()
        else:
            error()
    else:
        print('Точка находится вне графика')
except:
    print('404!')
