from math import pi
volume = float(input("Введите объем шара"))

radius = volume**(1/3) * 3 / (4 * pi)

print(f"Радиус шара равен:{radius}")
