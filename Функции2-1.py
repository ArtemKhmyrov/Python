n = int(input("Введите факториал "))#ввод
def doublefactorial(n):#функция вызывающая n
    if (n == 0 or n == 1):#если четный или нечетный
        return 1#возвращаем 1
    return n * doublefactorial(n - 2)#применяем правило мол 1*3*5 или 2*4*6
print(doublefactorial(n))#вывод

