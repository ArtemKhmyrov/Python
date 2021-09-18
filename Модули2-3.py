import random#подключаем рандомайзер
import string#подключаем строки

def password (): #создаем функцию пароля
    cif = string.digits #генерируем строку из чисел
    letters = list(string.ascii_lowercase + string.ascii_uppercase) # генерируем строки всех регистров
    zn = string.punctuation  # строка из специальных символов
    pas = random.choice(cif) + random.choice(zn) # добавляем к паролю цифры и знаки
    for _ in range(4): # генерируем цикл из букв до четырех
        pas += random.choice(letters) # рандомим последовательность
    simb = list(cif + zn) #перемешиваем последовательность символов
    random.shuffle(simb)#перемешиваем наши символы
    for _ in range (6):#генерируем символы
        pas += random.choice(simb)# преобразуем строку в последовательность для перемешивания
    pas = list(pas)# закидываем в список наш пароль
    random.shuffle(pas)#перемешиваем
    return ''.join(pas) #возвращаем строку с паролем
for i in range(10): #цикл для пароля
    print(password())# вывод пароля
