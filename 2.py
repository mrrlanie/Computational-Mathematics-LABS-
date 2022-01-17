from sympy import *


# x_i = 0.85
# x_i_1 = 0.9
# x__1 = 0.8


def myfunc(x):
    return 0.5 * pow(x, 2) + cos(2 * x)


def seconder(y):
    return 1 - (4 * cos(2 * y))


def third(z):
    return 8 * sin(2 * z)


def omega(x):
    return (x - 0.85) * (x - 0.9)


def we(m):
    return (m - 0.8) * (m - 0.85) * (m - 0.9)


a = 0.6
b = 1.1

x1 = 0.84
x2 = 0.62
x3 = 1.07
x4 = 0.83

h = (b - a) / 10
print("h =", h)

for i in range(0, 11):
    print(i)
    x_i = a + i * h
    print("x_i =", x_i)
    print("f(x_i) =", myfunc(x_i))
    x_i = 0

print(" ")
print(" ")

L_2 = myfunc(0.8) * (((0.84 - 0.85) * (0.84 - 0.9)) / ((0.8 - 0.85) * (0.8 - 0.9))) + myfunc(0.85) * (
        ((0.84 - 0.8) * (0.84 - 0.9)) / ((0.85 - 0.8) * (0.85 - 0.9))) + myfunc(0.9) * (
              ((0.84 - 0.8) * (0.84 - 0.85)) / ((0.9 - 0.8) * (0.9 - 0.85)))
print("L_2 =", L_2)

print(" ")
print(" ")

L_1 = myfunc(0.85) * ((0.84 - 0.9) / (0.85 - 0.9)) + myfunc(0.9) * (
        (0.84 - 0.85) / (0.9 - 0.85))
print("L_1 =", L_1)

print(" ")
print(" ")

R_1_min = seconder(0.85) * omega(0.84) / 2
R_1 = myfunc(0.84) - L_1
R_1_max = seconder(0.9) * omega(0.84) / 2

print("R_min =", R_1_min)
print("R_1 =", R_1)
print("R_max =", R_1_max)

print("R_min < R_1 < R_max")

print(" ")
print(" ")

R_2_min = third(0.85) * we(0.84) / 6
R_2 = myfunc(0.84) - L_2
R_2_max = third(0.9) * we(0.84) / 6

print("R_min =", R_2_min)
print("R_2 =", R_2)
print("R_max =", R_2_max)

print("")
print("")

f_1 = (myfunc(0.85) - myfunc(0.9))/(0.85-0.9)
f_2 = (myfunc(0.8) - myfunc(0.85))/(0.8 - 0.85)
f_3 = (f_2 - f_1)/(0.9-0.8)

print("f_1", f_1)
print("f_2", f_2)
print("f_3", f_3)

print("")
print("")

L_1_i = myfunc(0.85) + f_1*(0.84 - 0.85)
L_2_i = myfunc(0.8) + f_2*(0.84-0.8) + f_3*(0.84 - 0.8)*(0.84 - 0.85)

print("L_1_* = ", L_1_i)
print("L_1 = ", L_1)
print("L_2_* = ", L_2_i)
print("L_2 = ", L_2)

print("Difference L_1", abs(L_1 - L_1_i))
print("Difference L_2", abs(L_2 - L_2_i))
