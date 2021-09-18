# суть в том что мы заполняем нулями весь массив потом по возрастанию идем по четным столбцам и выставляем числа
# а потом выставляем числа по нечетным столбцам


import sys

n = int(input("Введите размерность массива NxN: "))

a = []

for i in range(n):
    b = []
    for j in range(n):
        b.append(0)
    a.append(b)

x = 0

for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        for j in range(n):
            a[j][i] = x
            x += 1
    else:
        for j in range(n - 1, -1, -1):
            a[j][i] = x
            x += 1

print("\n")

for i in range(n):
    s = ""
    for j in range(n):
        s += str(a[i][j]) + " "
    print(s)

print("\n")