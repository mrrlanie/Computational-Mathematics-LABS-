import math

from sympy import *

a = 0.6
b = 1.1

x_dot = {
    2: 0.62,
    3: 1.07,
    4: 0.83
}

count = 10
h = (b - a) / count
x_ = []
f = []
differences = [[]]
remainders = []


# исходная функция
def function(x):
    return 0.5 * pow(x, 2) + cos(2 * x)


# 11-я производная
def eleven_derivative(x):
    return 2048 * sin(2 * x)


# получение конечных разностей высших порядков
def get_diff(array, step, count=0):
    if step == 0:
        return
    array.append([])
    for i in range(0, step):
        array[count + 1].append(array[count][i + 1] - array[count][i])
    step -= 1
    count += 1
    get_diff(array, step, count)


# нахождение остаточного члена
def remain(x):
    w = 1
    for i in range(0, len(x_)):
        if x_[i] != x:
            w *= (x - x_[i])
    return eleven_derivative(x) / math.factorial(count + 1) * w


def newton_forward(x):
    t = (x - a) / h
    L_n = f[0]
    t_product = t
    for i in range(0, count - 1):
        L_n += (differences[i][0] * t_product) / math.factorial(i + 1)
        t_product *= (t - (i + 1))
    return L_n


def newton_backward(x):
    t = (x - b) / h
    L_n = f[-1]
    t_product = t
    for i in range(0, count - 1):
        L_n += (differences[i][count - i - 1] * t_product) / math.factorial(i + 1)
        t_product *= (t + i + 1)
    return L_n


def gauss_forward(x):
    t = (x - x_[count // 2]) / h
    L_n = f[count // 2]
    t_product = t
    index = 1
    for i in range(0, count - 1):
        L_n += (differences[i][len(differences[i]) // 2] * t_product) / math.factorial(i + 1)
        if i % 2 == 0:
            t_product *= (t - index)
        else:
            t_product *= (t + index)
            index += 1
    return L_n


def main():
    # подсчет значений иксов и значений функции
    for i in range(count + 1):
        print("x: ", a + h * i)
        print("f(x): ", function(a + h * i))
        print(" ")
        x_.append(a + h * i)
        f.append(function(x_[i]))

    # разности первого порядка
    for i in range(0, count):
        differences[0].append(f[i + 1] - f[i])

    # получение разностей высших порядков
    get_diff(differences, count - 1)

    # вывод разностей
    for i in range(len(differences)):
        print(f'delta^{i + 1} {differences[i]}')

    # остаточный член для каждой точки
    for i in range(0, len(x_)):
        remainders.append(remain(x_[i]))

    # 11 производные
    for i in range(count + 1):
        print("f**10(x):", eleven_derivative(x_[i]))

    print(" ")
    print(" ")

    minR = min(remainders)
    maxR = max(remainders)

    print("max R_n: ", maxR)
    print("min R_n: ", minR)

    print(" ")
    print(" ")

    L_2 = newton_forward(x_dot[2])
    L_3 = newton_backward(x_dot[3])
    L_4 = gauss_forward(x_dot[4])

    print("L_2: ", L_2)
    print("L_3: ", L_3)
    print("L_4: ", L_4)

    print(" ")
    print(" ")

    print("f(x^**): ", function(x_dot[2]))
    print("f(x^***): ", function(x_dot[3]))
    print("f(x^****): ", function(x_dot[4]))

if __name__ == '__main__':
    main()