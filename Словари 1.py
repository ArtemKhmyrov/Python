n = int(input("Введите количество строк: "))#ввод количества строк
a = {}#создаем пустой словарь
for _ in range(n):#генерируем количество строк
    str = input("Введите строку: ").split()#вводим строки и разбиваем их на подстроки
    for word in str:#формируем цикл
        a[word] = a.get(word, 0) + 1#заносим слова в словарь

A = sorted(a.items(), key=lambda x: (-x[1], x[0]))#сортируем, возвращаем пары для каждого значения, создаем встроенную функцию lambda
print("Вывод: \n")#вывод
for word in A:#цикл вывода
    print(word[0])#вывод всех слов

