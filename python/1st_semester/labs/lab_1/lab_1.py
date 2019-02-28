from math import log, tan, pi, sqrt
while True:
    try:
        a = float(input('Enter your A: '))
        b = float(input('Enter your B: '))
        z1 = a**(sqrt(log(a,b)))-b**(sqrt(log(b,a)))+tan(a*b+(3*pi/2))
        z2 = tan(a*b+(3*pi)/2)
        break
    except:
        print('ОДЗ!1')
print("Z1 = " + str(z1) + "\n" +"Z2 = " + str(z2))
