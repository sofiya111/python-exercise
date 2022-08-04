from math import *
def f(x):
    return 0.9*x**2 - cos(2*x) - 1
def f2(x):
    return 1.8 + 4*cos(2*x)
def f1(x):
    return 1.8*x + 2*sin(2*x)
print("Введите исходные данные:")
a = float(input("a = "))
b = float(input("b = "))
eps = float(input("eps = "))
n = 0
error = False
if f(a)*f2(a) > 0:
    x = a
elif f(b)*f2(b) > 0:
    x = b
else:
    error = True
    print("Ошибка")

if not error:
    while True:
        h = f(x) / f1(x)
        x -= h
        n +=1
        if fabs(h) < eps:
            break
    print("x = %f  f(x) = %i " % (x, f(x)))
    print("n = ", n)

