import datetime
# Выводится сообщение
print("Давай познакомимся")
# Считываем введенное пользователем значение.
# Результат записывается в переменную name
name = input("Как тебя зовут?")
# Выводится новое сообщение
print("Добрый день,", name+"!")

year_input = int(input("Какой сейчас год?"))
y = "Верно!" if year_input == datetime.date.today().year else "Неверно! А теперь проснись и запусти меня снова"
print(y)
