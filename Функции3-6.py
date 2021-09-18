from math import sqrt#подключаем библиотеку
n = int(input())#вводим
s = []#создаем пустой список
def fum(s):
    s = list(map(lambda x: (((sqrt(x[0]+x[1]))*(x[2]*x[2]*x[2]))/(x[0]*x[2])), s))#тут формула вот эта из 6 варианта
    print(s)#выводим

for _ in range(n):#
    x, y, z = input().split()#вводим переменныу
    s.append(((float(x), float(y), float(z))))#заносим три элемента
fum(s)#вызываем функцию



#n = int(input())
#s = []
#           for _ in range(n):
  #          x, y = input().split()
   #        s.append((int(x), int(y)))
#           print("Список:", s)
#           s = list(map(lambda x: x[0]+x[1], s))
#           print("Измененный список:", s)