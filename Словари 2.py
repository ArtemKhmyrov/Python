n = int(input("Введите количество человек: "))#dsdjl
prt = {} # словарь
for _ in range(n):# создаем цикл до н
    name, cl, count = input("Введите фамилию и баллы: ").split()#вводим
    cl = int(cl)#инициализируем как число
    sp = prt.get(cl, {})#кладем в словарь
    sp[name] = sp.get(name, 0) + int(count)#считаем голоса и имена
    prt[cl] = sp#кладем

for cl, sp in sorted(prt.items()): # cjplftv wbrk
    print(cl, ':', sep='') # вывод
    for name, count in sorted(sp.items(), key=lambda x: (x[1], x[0])):# сортируем словарь по ключу сначала в порядке возрастания потом в алфавитном порядке по имени
        
        print(name, count)# вывод
#--------------------------------------------------------------------

        #n = int(input())
        #prt = {}  # словарь
        # ключом будет имя кандидата
        # значением - количество голосов
        #for _ in range(n):
            #name, count = input().split()
            # считали имя кандидата и коичество голосов в некотором штате
           # prt[name] = prt.get(name, 0) + int(count)
            # обновили данные о кандидате
            # prt.get(name, 0) - возвращает кол-во голосов,
            # которое уже было записано в словарь за кандидата name
            # если кандидата в словаре не было, то возвращает 0
            # добавляем (+) новое количество голосов
       # sp = sorted(prt.items(), key=lambda x: (-x[1], x[0]))
        # сортируем словарь по ключу x - пара (имя кандидата, количество голосов)
        # сначала  по -x[1], т.е в порядке убывания голосов
        # потом (т.е. кол-во голосов совпадает) x[0] в алфавитном порядке по имени
      #  print()
        # выводим в нужном виде
       # for name, count in sp:
            #print(name, count)
