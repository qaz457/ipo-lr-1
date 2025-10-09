import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

fabs = math.fabs(x - y)
num = (8 + fabs**2 + 1) ** (1/3)
den = x**2 + y**2 + 2
exp = math.exp(fabs)

u = num / den - exp

print(f"Значение u: {u}")
