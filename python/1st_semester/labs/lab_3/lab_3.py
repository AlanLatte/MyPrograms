# -*- coding: utf-8 -*-
from math import *
import random
import math
xBeg = float(input("xBeg = "))
xEnd = float(input("xEnd = "))
dx = float(input("dx = "))
print("xBeg={0: 7.2f} xEnd={1: 7.2f}".format(xBeg,xEnd))
print("  dx={0:7.2f}".format(dx))
xt=xBeg
print("+--------+--------+")
print("I    X   I    Y   I")
print("+--------+--------+")
while xt<=xEnd:
    if xt <=-2.5: y = -6/7*xt-36/7
    elif -2.5<xt and xt<2: y = xt**3 + 1.5*xt**2-2.5*xt-3
    elif 2<=xt: y = -2*xt + 10
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt,y))
    xt+=dx
print("+--------+--------+\n____________________\nЗадание№2\n")
def error():
    global f
    f+=1
    print('Мимо')
def true():
    global t
    t+=1
    print('Попал')
def two_four():
    if x>0 and y<0 and y<x-RADUIS:
        true()
    elif (x<0 and y>0) and y>x+RADUIS:
        true()
    else:
        error()
def one_three():
    if x<0 and y<0 and y<-x-RADUIS:
        true()
    elif x>0 and y>0 and y>-x-RADUIS:
        true()
    else:
        error()
t = int()
f = int()
for i in range(int(input("Введите количество выстрелов: \n"))):
    RADUIS = random.randrange(100)
    x = random.randrange(100)
    y = random.randrange(100)
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
        error()
print("Выстрелов попавших в цель: " + str(t))
print("Выстрелов не попавших в цель: " + str(f))
print("+--------+--------+\n____________________\nЗадание№3\n")
while True:
    while True:
        xBeg = float(input("xBeg[-1:1]= "))
        if abs(xBeg)<=1:
            break
    xEnd = float(input("xEnd[-1:1] = "))
    if abs(xEnd)<=1:
        break
dx = float(input("dx = "))
print("xBeg={0: 7.2f} xEnd={1: 7.2f}".format(xBeg,xEnd))
print("dx={0:7.2f}".format(dx))
xt=xBeg
print("+---------+----------+")
print("I    X    I     Y    I")
print("+---------+----------+")
while xt<=xEnd:
    result_1 = 0
    n=2
    for i in range(int(input("Укажите точность расчетов:\t"))):
        if i%2: result_1-= (n*(n+1)*xt**(n-1))
        else:   result_1+= (n*(n+1)*xt**(n-1))
        n+=1
    print("I{0: 7.2f}  I {1: 7.2f}  I".format(xt, (1-result_1/2)))
    xt+=dx
    result_1 = 0
print("+---------+----------+")
