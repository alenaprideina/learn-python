res = eval(input("Введите что-нибудь"))
try:
    if type(res) == int:
        print("Вы ввели целое число")
    elif type(res) == float:
        print("Вы ввели число с плавающей точкой")
    else:
        print("Скорее всего вы ввели текст!")
except NameError:
    print("Если вводите текст, возьмите его в кавычки")

cond = True
i = 0
while cond:
    i += 1
    if i == 4:
        continue
    elif i == 8:
        cond = False
        # break
    print("i =", i)
# опциональная инструкция
else:
    print("Если в while есть break - это сообщение не выведется")
