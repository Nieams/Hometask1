"""
ax^2+bx+c=0
"""
print("Введите коэффициенты квадратного уравнения a, b, c")
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
x1 = (-b+D**0.5)/(2*a)
x2 = (-b-D**0.5)/(2*a)
if x1 == x2:
    print("Единственный корень", x1)
else:
    print("Корни квадратного уравнения (возможно комплексные):", x1, x2)

