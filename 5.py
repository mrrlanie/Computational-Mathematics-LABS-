import math

a = 0.6
b = 1.1

count_1 = 10
count_2 = 20
count_3 = 40
count_4 = 80
count_5 = 80
h_1 = (b - a) / count_1
x_1 = []
f_1 = []
h_2 = (b - a) / count_2
x_2 = []
f_2 = []
h_3 = (b - a) / count_3
x_3 = []
f_3 = []
h_4 = (b - a) / count_4
x_4 = []
f_4 = []
h_5 = (b - a) / count_5
x_5 = []
f_5 = []


def function(x):
    return 0.5 * pow(x, 2) + math.cos(2 * x)


print("Для n:")
for i in range(count_1 + 1):
    x_1.append(a + h_1 * i)
    f_1.append(function(x_1[i]))

left_rectangles = 0
for i in range(0, count_1):
    left_rectangles += function(x_1[i])
left_rectangles *= (b - a) / count_1

print("Составная формула левых прямоугольников дает результат:", left_rectangles)
print(" ")
print(" ")

print("Для 2n:")
for i in range(count_2 + 1):
    x_2.append(a + h_2 * i)
    f_2.append(function(x_2[i]))

left_rectangles_2 = 0
for i in range(0, count_2):
    left_rectangles_2 += function(x_2[i])
left_rectangles_2 *= (b - a) / count_2

print("Составная формула левых прямоугольников c 2n дает результат:", left_rectangles_2)
print(" ")
print(" ")

print("Для 4n:")
for i in range(count_3+ 1):
    x_3.append(a + h_3 * i)
    f_3.append(function(x_3[i]))

left_rectangles_3 = 0
for i in range(0, count_3):
    left_rectangles_3 += function(x_3[i])
left_rectangles_3 *= (b - a) / count_3

print("Составная формула левых прямоугольников c 4n дает результат:", left_rectangles_3)
print(" ")
print(" ")

print("Для 8n:")
for i in range(count_4+ 1):
    x_4.append(a + h_4 * i)
    f_4.append(function(x_4[i]))

left_rectangles_4 = 0
for i in range(0, count_4):
    left_rectangles_4 += function(x_4[i])
left_rectangles_4 *= (b - a) / count_4

print("Составная формула левых прямоугольников c 8n дает результат:", left_rectangles_4)
print(" ")
print(" ")

print("Для 16n:")
for i in range(count_5 + 1):
    x_5.append(a + h_5 * i)
    f_5.append(function(x_5[i]))

left_rectangles_5 = 0
for i in range(0, count_5):
    left_rectangles_5 += function(x_5[i])
left_rectangles_5 *= (b - a) / count_5

print("Составная формула левых прямоугольников c 16n дает результат:", left_rectangles_5)
print(" ")
print(" ")




print(abs(left_rectangles_2 - left_rectangles))
print(abs(left_rectangles_3 - left_rectangles_2))
print(abs(left_rectangles_4 - left_rectangles_3))
print(abs(left_rectangles_5 - left_rectangles_4))


