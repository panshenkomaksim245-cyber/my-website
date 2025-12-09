import math
a = float(input("a = "))
b = float(input("b = "))
x = a**4 + b**2
y = math.log(x**2) / (1 + math.sin(x)**2)
print("x =", x)
print("y =", y)
