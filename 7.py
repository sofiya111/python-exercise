from math import *
print("Введите исходные данные:")
a = input("a = ")
b = input("b = ")
n = float(input("n = "))
h = (eval(b) - eval(a))/n
s = 0
x = eval(a) + h/2
z = (sin(x)+cos(2*x))/(2+cos(x))
while x < eval(b):
    s += z
    x += h
s *= h
print("S = ", s)