from math import fabs,exp,tan,pow
x = float(input("Введите x:"))
y = float(input("Введите y:"))
z = float(input("Введите z:"))

h = ( (pow(x,y+1) + exp(y-1)) / (1+(x*(fabs(y-tan(z)))) ) * (1+(fabs(y-x))) + ((pow(fabs(y-x),2)) / 2) - (pow(fabs(y-x),3) / 3) )
print(f"Ответ искомого выражения:{h}")