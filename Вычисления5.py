H = int(input("Enter the H = ")) # ввод
A = int(input("Enter the A = ")) # ввод
B = int(input("Enter the B = ")) # ввод

Step = A - B # чистых шагов с учетом опущения
H0 = H - A # чистых без опущения
Result = (1 + H0 // Step + (H0 % Step + Step - 1) // Step) # подсчитываем сколько она будет страдать

print(Result) # вывод

