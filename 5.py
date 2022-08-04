# Цель - вычисление значения функции
# Переменные:
# х - аргумент, изменяющийся от х0 c шагом hx до xn;
# y  - функция;
# Программист: Горбатова С.А.
from math import *
print("Введите начальное значение x0 с шагом hx и конечное значение xn:")
x0 = float(input("x0 = "))
hx = float(input("hx = "))
xn = float(input("хn = "))
x = x0
z = tan((x+1)/3)
while x < xn + hx / 2:
    if isinf(z) == True:
        print("Функция не существует при x= %.2f" % (x))
    elif x <= pi/2:
        y = 2*sin((3*x)/4)
        print("x = %.2f y = %.2f" % (x, y))
    else:
        y = x/2*tan((x+1)/3)
        print("x = %.2f y = %.2f" % (x, y))
    x += hx
