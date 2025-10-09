number_8 = input("Введите число из 8 разрядов")
sum = 0
if len(number_8) == 8:
    for i in number_8:
        sum += int(i)
    print(f"Сумма цифр числа:{sum}")
else:
    print("Неккоркетный ввод числа")