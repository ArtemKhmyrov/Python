import datetime#подключаем библиотеку
 
day = datetime.datetime.strptime(input('Введите дату: '), "%d.%m.%Y")#вводим дату с определением через точку
n = int(input('Количество дней: '))#вводим количество дней
diff = datetime.timedelta(days=n)#вычисляем сумму или разницу в днях
first = day - diff#вычисляем первый день
second = day + diff#вычисляем второй
s = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]#список дней недель
print(first.strftime("%d.%m.%Y"), " - ", s[first.weekday()])#ыводим первую дату и день
print(second.strftime("%d.%m.%Y"), " - ", s[second.weekday()])#выводим вторую дату и день
