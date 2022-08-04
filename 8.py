from math import *
kmax = 1e5
print("Введите исходные данные:")
z = float(input("z = "))
eps = float(input("eps = "))
t = z
p = 1
k = 1
while (fabs(t) > eps) and (k < kmax):
    t = 1 - (z/(k*pi))**2
    p *= t
    k += 1
s = p*z
print("sin(z) = %.5f" % s)
print("Проверка: sin(0.3) = %.5f" % sin(z))
