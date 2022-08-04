print('Hello World!')
print(40 + 2)
print("┌" + "─" * 10 + "┐")
for i in range(1, 9 + 1):
    print("│" + "░" * (i - 1), i, "░" * (9 - i) + "│")
    if i < 9:
        print("├" + "─" * 10 + "┤")
print("└" + "─" * 10 + "┘")
x = 1
y = 2
z = x + y
print("z =", z)
d = float(input("Введите d: "))
b = 4.2
c = b ** d
print("c =", c, "\n")
text = "(x + 2*y - d**2) / 0.5"
print(text)
print("result = ", eval(text))
