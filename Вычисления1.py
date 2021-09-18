LessonNumber = int(input("lessonNumber = ")) # Ввод номера урока
minutes = LessonNumber * 45 + LessonNumber // 2 * 5 + (LessonNumber - 1) // 2 * 15 # находим общее кол-во в минутах
TimeInHours = minutes // 60 + 9  # целое число добавляем в часы
TimeInMinutes = minutes % 60 # остаток добавляем в минуты
print (TimeInHours, TimeInMinutes) # вывод
