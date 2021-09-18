P = int(input("Enter the P"))  # годовой процент
X = int(input("Enter the X"))  # рубли
Y = int(input("Enter the Y"))  # копейки

Contribution = X * 100 + Y  # переводим в копейки
PercentWhitContribution = Contribution + (Contribution * P / 100)  # наш вклад + процент годовых
Ruble = int(PercentWhitContribution // 100)  # результат в рублях
Kopeck = int(PercentWhitContribution % 100)  # результят в копейках

print(Ruble, Kopeck)