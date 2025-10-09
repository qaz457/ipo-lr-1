class_1 = int(input("введите количество учеников в 1 классе"))
class_2 = int(input("введите количество учеников во 2 классе"))
class_3 = int(input("введите количество учеников в 3 классе"))

class_all = class_1 + class_2 + class_3

parta = class_all // 2 + class_all % 2

print(f"Нужное количество пар равно - {parta}")