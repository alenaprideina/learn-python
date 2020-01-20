def my_pow(n):
    """
    функция в качестве результата возвращает функцию
    :param n:
    :return:
    """
    return lambda x: x**n


for i in range(1, 4):
    for j in range(1, 5):
        print(j, "в степени", i, "=", my_pow(i)(j))
    print()
