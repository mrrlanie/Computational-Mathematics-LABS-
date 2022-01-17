import math
from sympy import *
import matplotlib.pyplot as plt


def run(n, bottom, center, upper, right_part):
    m = 0
    x = [0 for i in range(n)]
    for i in range(1, n):
        m = bottom[i] / center[i - 1]
        center[i] = center[i] - m * upper[i - 1]
        right_part[i] = right_part[i] - m * right_part[i - 1]

    x[n - 1] = right_part[n - 1] / center[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (right_part[i] - upper[i] * x[i + 1]) / center[i]

    return x


def splains(x, i):
    a1 = 6 / h
    a2 = (f_i[i + 1] - f_i[i]) / h
    a3 = (matrix_run[i + 1] + 2 * matrix_run[i]) / 3
    a4 = 12 * (x - x_i[i]) / (h ** 2)
    a5 = (matrix_run[i + 1] + matrix_run[i]) / 2
    a6 = (f_i[i + 1] - f_i[i]) / h
    result = a1 * (a2 - a3) + a4 * (a5 - a6)
    return result


def myfunction(x):
    return 0.5 * pow(x, 2) + cos(2 * x)


def second_der(x):
    return 1 - 4 * cos(2 * x)


a = 0.6
b = 1.1
n = 11
h = (b - a) / (n - 1)
x_i = [a + h * i for i in range(n)]
f_i = [myfunction(i) for i in x_i]
der_i = [second_der(i) for i in x_i]
right_part_matix = []

diag_1 = [0.5 if i != 9 else 1 for i in range(n - 1)]
diag_1.insert(0, 0)
diag_2 = [2 for _ in range(n)]
diag_3 = [0.5 if i != 0 else 1 for i in range(n - 1)]
diag_3.append(0)

for i in range(n):
    if i == 0:
        right_part_matix.append((3 / h) * (f_i[i + 1] - f_i[i]) - (h / 2) * second_der(x_i[i]))
    elif i == n - 1:
        right_part_matix.append((h * second_der(x_i[i]) / 2) + 3 * ((f_i[i] - f_i[i - 1]) / h))
    else:
        right_part_matix.append(30 * (f_i[i + 1] - f_i[i - 1]))

print("Нижняя диагональ матрицы: ", diag_1)
print(" ")
print("Главная диагональ матрицы: ", diag_2)
print(" ")
print("Верхняя диагональ матрицы: ", diag_3)
print(" ")
print("Правая часть матрицы: ", right_part_matix)
print(" ")

matrix_run = run(n, diag_1, diag_2, diag_3, right_part_matix)
print("Метод прогонки: ", matrix_run)

for i in range(n - 1):
    splain_i = [splains(x, i) for x in x_i]
    plt.plot(x_i, splain_i)
    plt.plot(x_i, der_i)
    plt.show()