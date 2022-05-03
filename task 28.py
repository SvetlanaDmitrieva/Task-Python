#Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
import math
print("Введите коэффициенты для уравнения ")
print("ax**2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a==0:
    if b!=0 :
        x1=-c/b
        print("Корень уравнеия x = %.2f " % x1)
    else:
        print('Решений нет')
else:       
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x1 = -b / (2 * a)
        print("Корень уравнеия x = %.2f" % x1)
    else:
        print("Корней нет")