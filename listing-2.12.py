# решаем уравление ax = b
print("Решаем уравнение ax = b")
try:
    a = float(input("Введите a:"))
    b = float(input("Введите b:"))
    x = b/a
    print("Решение уравнения: x =", x)
except ValueError:
    print("except ValueError: Нужно было ввести число!")
except ZeroDivisionError:
    print("except ZeroDivisionError: На ноль делить нельзя")
else:
    print("В блоке else - код, который отработает, только если ошибки не было")
finally:
    print("В блоке finally - код, который отработает всегда")
