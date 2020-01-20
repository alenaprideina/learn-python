# при объявлении функции создается объект типа function
# ссылка на объект записывается в переменную, которая указана после инструкции def


def my_func(txt):
    print("Функция my_func:", txt)


new_func = my_func
new_func("вызов через new_func")

print(my_func is new_func)  # True
