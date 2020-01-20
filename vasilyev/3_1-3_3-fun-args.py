def input_name():
    """
    функция без аргументов
    если вызвать такую функцию с аргументом, то будет ошибка
    TypeError: input_name() takes 0 positional arguments but 1 was given
    :return:
    имя, которое введет пользователь
    """
    print("Добрый день!")
    name = input("Как вас зовут? ")
    return name


def say_hello(txt):
    """
    функция с одним обязательным аргументом
    если вызвать такую функцию без аргументов, то будет ошибка
    TypeError: say_hello() missing 1 required positional argument: 'txt'
    :param txt:
    имя, с которым здоровается программа
    :return:
    """
    print("Привет,", txt + "!")


def my_exp(x, n):
    s = 0
    q = 1
    for k in range(n+1):
        s += q
        q *= x/(k+1)
    return s


def print_text(txt="print_text: Значение аргумента по умолчанию"):
    print(txt)


def show_args(a, b="show_args: Второй аргумент со значением по умолчанию"):
    print(a, b)


def my_func(x="my_func: Значение по умолчанию для первого аргумента", y="my_func: Значение по умолчанию для второго аргумента"):
    print(x, y)


def get_sum(*nums):
    return sum(nums)


# say_hello(input_name())
for n in range(11):
    print("n = ", n, "->", my_exp(1, n))
print_text()
print_text("print_text: Текст задан")
show_args("show_args: 435", b="show_args: 1")
show_args("show_args: text", "show_args:text2")
show_args("show_args: text3")
my_func()
my_func("my_func: 1", "my_func: 2")
my_func(y="my_func: 4", x="my_func: 3")
print(get_sum(5, 6, 8, 200))
