from math import *
x= float(input("Введите x:"))
print("x=",x)
y=-(2**x)/(x**3)*sin(x)
y+=sqrt(fabs((2*x**2)/(x+2)-cos(x)))
print("y=",y)