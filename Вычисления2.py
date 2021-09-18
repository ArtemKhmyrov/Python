Hour=float(input('H=')) # вводим час
Minute=float(input('M=')) # вводим минуты
Second=float(input('S=')) # вводим секунды
Result = (30*Hour+Minute/2+Second/120) # вычисляем кол-во градусов
print(Result) # выводим результат