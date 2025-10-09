amount_apple = int(input("Введите количество яблок"))
amount_students = int(input("Введите количество уеников"))

quantity_for_each = amount_apple // amount_students
remainder = amount_apple % amount_students

print (f"Каждый ученик получит по {quantity_for_each} яблок(а) и в корзине останеться {remainder} яблок(а)")