str = input("Введите строку:\n") # вводим строку
str = str.replace(',','')# Возвращаем копию строки в которой заменены все вхождения
list = str.split()#разбиваем строку на пробелы
#  из примера mam, 23, dead, 25, 5, son
a = 0 #счетчик
for i in list:#
    if i.isdigit(): # если в списке содержатся цифры то применяется метод ()
        a = a + int(i)# складываем все числа
print(a)# выводим
