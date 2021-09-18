Angle = float(input("Enter the angle = ")) # введите угол
Minute = int(Angle * 2) % 60 # берем остаток от этой штуки при вычитании 360
Result = (Minute * 6) # остаток умножаем
print(Result) # вывод