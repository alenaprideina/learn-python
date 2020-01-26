from math import sqrt


def task1():
    A = int(input())
    B = int(input())
    C = int(input())

    p = (A + B + C) / 2
    S = sqrt(p * (p - A) * (p - B) * (p - C))
    print(S)


def task2():
    X = int(input())
    print((-15 < X <= 12 or 14 < X < 17 or X >= 19))


def task3():
    X = float(input())
    Y = float(input())
    operation = input()

    try:
        if operation == 'mod':
            print(X % Y)
        elif operation == 'pow':
            print(X ** Y)
        elif operation == 'div':
            print(X // Y)
        else:
            print(eval(str(X) + operation + str(Y)))
    except ZeroDivisionError:
        print('Деление на 0!')

def task4():
    figure = input()
    if figure == 'треугольник':
        A = float(input())
        B = float(input())
        C = float(input())

        p = (A + B + C) / 2
        S = sqrt(p * (p - A) * (p - B) * (p - C))
    elif figure == 'прямоугольник':
        a = float(input())
        b = float(input())
        S = a * b
    else:
        # 'круг'
        r = float
        S = 3.14 * (r ** 2)

    print(S)

def task5():
    A = int(input())
    B = int(input())
    C = int(input())

    print(max(A, B, C))
    print(min(A, B, C))
    print(A + B + C - max(A, B, C) - min(A, B, C))


def task6():
    N = int(input())
    if N == 1:
        print(N, 'программист')
    elif 2 <= N <= 4:
        print(N, 'программиста')
    elif 11 <= N <= 20 or 11 <= N % 100 <= 20:
        print(N, 'программистов')
    elif N % 10 == 0 or 5 <= N % 10 <= 9:
        print(N, 'программистов')
    elif N % 10 == 1:
        print(N, 'программист')
    elif 2 <= N % 10 <= 4:
        print(N, 'программиста')


def task7():
    N = int(input())
    if (N // 100000 + (N // 10000 % 10) + (N // 1000 % 10)) == ((N // 100 % 10) + (N // 10 % 10) + N % 10):
        print('Счастливый')
    else:
        print('Обычный')

task6()
