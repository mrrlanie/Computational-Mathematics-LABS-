import math

import sympy
from sympy import *
from sympy.abc import x

# исходные числа
m = 1
n = 3
k = 2

a = 0.6
b = 1.1
count = 10
h = (b - a) / count
x_ = []
f = []
remainders = []


# нахождение остаточного члена
def remain(x):
    w = 1
    for i in range(0, len(x_)):
        if x_[i] != x:
            w *= (x - x_[i])
    return derivative_func(x) / math.factorial(count + 1) * w


# производная полинома
def derivative_L(dot):
    return 7.7960349125533 * dot - 5.13652664206393


# производная функции
def derivative_func(dot):
    return 1 - 4 * cos(2 * dot)


# исходная функция
def function(dot):
    return 0.5 * pow(dot, 2) + cos(2 * dot)


print("Таблица точек и значений:")
print(" ")
for i in range(0, 11):
    print("№:", i)
    x_i = a + i * h
    print("x_i =", x_i)
    x_.append(x_i)
    print("f(x_i) =", function(x_i))
    f.append(function(x_i))
    x_i = 0

print(" ")
print(" ")

first = -723.1436726355641 * (x - 0.75) * (x - 0.7) * (x - 0.65)  # первое слагаемое для х_0
second = 1914.995314498351 * (x - 0.75) * (x - 0.7) * (x - 0.6)  # второе слагаемое для х_1
third = -1659.868571600965 * (x - 0.6) * (x - 0.65) * (x - 0.75)  # третье слагаемое для х_2
fourth = 469.3162688902701 * (x - 0.6) * (x - 0.65) * (x - 0.7)  # четвертое слагаемое для х_3

L_3 = first + second + third + fourth

print("Полином Лагранжа 3-его порядка:", L_3)

print(" ")
print(" ")

L_3_der = sympy.diff(sympy.diff(L_3))  # вторая производная полинома Лагранжа
func_der = sympy.diff(sympy.diff(0.5 * pow(x, 2) + cos(2 * x)))  # вторая производная исходной функции

print("Вторая производная полинома: ", L_3_der)
print("Значение в точке х_m: ", derivative_L(x_[1]))

print(" ")

print("Вторая производная исходной функции: ", func_der)
print("Значение в точке х_m: ", derivative_func(x_[1]))

print(" ")
print(" ")

# просчитываем остатки для каждой точки
for i in range(0, len(x_)):
    remainders.append(remain(x_[i]))

# находим минимум/максимум
max_R = max(remainders)
min_R = min(remainders)

# находим остаток дифференцирования
R_k = derivative_func(x_[1]) - derivative_L(x_[1])

print("Максимальный остаток ", max_R)
print("Остаток при дифференцировании ", R_k)
print("Минимальный остаток ", min_R)
