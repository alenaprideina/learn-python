def minutes_from_hm(x, y):
    return x*60 + y


def minutes_to_hm(m):
    return m // 60, m % 60


def hm_plus_minutes_to_hm(x, h, m):
    return ((h * 60 + m) + x) // 60, ((h * 60 + m) + x) % 60


# if __name__ == '__main__':
#     print("Все в рамках одних суток")
#     print("Введите количество часов и минут. В ответ получите общее количество минут")
#     x = int(input())
#     y = int(input())
#     print(minutes_from_hm(x, y))
#
#     print("Введите количество минут. В ответ получите количество часов и минут")
#     m = int(input())
#     for x in minutes_to_hm(m):
#         print(x)
#
#     print("Введите количество минут, затем часы и минуты, к которым их нужно прибавить. Ответ - часы, минуты")
#     X = int(input())
#     H = int(input())
#     M = int(input())
#
#     for x in hm_plus_minutes_to_hm(X, H, M):
#         print(x)

