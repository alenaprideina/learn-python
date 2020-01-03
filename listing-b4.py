import builtins
import math

print("Начинаем вычисления!")
# переменные не хранят значения, а ссылаются на них
a = 4
print("Значение переменной a=", a)
print("Тип переменной a", type(a))

# узнать, какие идентификаторы задействованы в работе интерпретатора в данный момент (определены в программе)
# в этот список не будут входить названия встроенных функций и других встроенных идентификаторов
print(dir())
del a
print(dir())

#  доступ к встроенным функциям и идентификаторам
print(dir(builtins))
print(dir(math))

# типы данных: int, float, str, complex, bool, list - списки
# set - множества, frozenset - неизменяемое множество
# tuple - кортежи, dict - словари
# bytes - неизменная последовательность байт, bytearray - изменяемая последовательность байт
# function, module, type - класс,

b = "6-5/2"
print(b + " =", eval(b))

a = True
b = not a
print(a, b)  # True False
c = a and b
d = a or b
print(c, d, b ^ a)  # False True True

x = 10
y = 20
z = x and y
print(z)  # 20
z = x or y
print(z)  # 10

# поменять местами значения двух переменных можно так:
print("x , y =", x, ",", y)
x, y = y, x
print("x , y =", x, ",", y)
