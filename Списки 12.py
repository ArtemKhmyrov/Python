str = input("Введите список: ", ) #ввод
str = str.split() # пробелы

for i in range(len(str)):#цикл от первого до последнего
    str[i] = int(str[i])# переводим в интовые
def plus(x):# функция
    if x > 0:# если положительное
        return True #выполняем
    else:#иначе
        return False #не выполняем
list = list(filter(plus, str)) #фильтруем только положительные
print(list)#вывод
