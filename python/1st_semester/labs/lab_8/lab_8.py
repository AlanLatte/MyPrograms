import numpy as np
import matplotlib.pyplot as plt
while True:
    while True:
        xBeg = float(input("xBeg(-"+u"\u221E"+":-1)= "))
        if xBeg<-1:
            break
    xEnd = float(input("xEnd(-"+u"\u221E"+":-1) = "))
    if xEnd<-1:
        break
dx = float(input("dx = "))
xt=xBeg
coo_x, coo_y = [], []
while xt>=xEnd:
    n=0
    result_1 = 0
    result_1 = ((-1)**(n+1))/(((2*n)+1)*(xt**((2*n)+1)))
    coo_x.append(xt)
    coo_y.append(-np.pi/2+result_1)
    xt-=abs(dx)
    result_1 = 0
b = int(input("B = "))
x = np.linspace(xBeg, xEnd, num=100, endpoint=False)
plt.plot(coo_x,coo_y,color = "#0349e8")
plt.plot(x, np.arctan(x)+b, color = "green")
plt.axis('tight')
plt.ylabel('Y')
plt.title('X')
plt.show()
