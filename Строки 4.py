str = input("Введите строку:\n")# вводим новую строку
# из примера 1234567890
list = '' # пустой список

a = len(str) # возвращаем количество символов из str в
for i in range(a):# цикл
    if (i + 1) % 3 != 0:  # если каждый третий символ при делении на три не равно нулю то
        list = list + str[i] # заносим в пустой список нашу строку
print(list) # выводим
