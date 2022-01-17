from sympy import *
import math
from sympy.abc import x

y = sin(x - 2) + pow(x, 2)  # исходная функция

differentials = {  # значения d^i/dx^i
    0: 0,
    1: 2 * x,
    2: 12 * pow(x, 2) - 4
}


def p_i(f):  # полиномы Лежандра
    return (1 / (pow(2, f) * math.factorial(f))) * differentials[f]


integrals = {   # интегралы для коэффициентов
    0: 0,
    1: -0.250661,  # -cos(1) - sin(1) + sin(3) - cos(3)
    2: 0.379483  # 2 * cos(1) - 3 * sin(1) + 4 / 15 - 2 * cos(3) - 3 * sin(3)
}


def c_i(z): # коэффициенты полиномов Лежандра
    return (2 * z + 1) / 2 * integrals[z]


g = 0

for i in range(0, 3):   # суммирование
    g += c_i(i) * p_i(i)


print("y = ", y)     # вывод исходной ф-ии
print("y_a =", g)    # вывод аппроксимированной ф-ии
