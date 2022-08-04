print("Введите исходные данные:")
x = float(input("x = "))
k = int(input("k = "))
p = 1
for i in range(1,(k+1)):
    p *= (2 * x + 1) / ((2 * i) ** 2 + 1)
print("Результат:")
print("p = %e" % p)