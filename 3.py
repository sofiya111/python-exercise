print("Введите x1,x2,x3,x4")
x1 = float(input("x1="))
x2 = float(input("x2="))
x3 = float(input("x3="))
x4 = float(input("x4="))
if x1 > x2:
    y = x1
else:
    y = x2

if x3 > y:
    y = x3
if x4 > y:
    y = x4
print("y =", y)