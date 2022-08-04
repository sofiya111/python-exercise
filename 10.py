import math
print("Введите начальное значение x0 с шагом hx и конечное значение xn:")
x0 = float(input("x0 = "))
hx = float(input("hx = "))
xn = float(input("хn = "))
x = x0
if x > 1:
    a = math.pi
else:
    a = math.pi/4
while x < xn + hx/2:
    s = 0
    for k in range(0, 11):
        s += math.log(x)
        print("s =%f k =%.0f " %(s, k)) #контроль промежуточных зачений
    z = s*math.sin(k)*(x-a)
    print("x = %.1f z = %.3f" %(x,z))
    x += hx