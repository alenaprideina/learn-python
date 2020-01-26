def sleep_for_health(A, B, H):
    if A <= H <= B:
        return 'Это нормально'
    elif H < A:
        return 'Недосып'
    else:
        return 'Пересып'


def is_year_vis(Y):
    if Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0:
        return 'Високосный'
    return 'Обычный'


# if __name__ == '__main__':
    # A = int((input()))
    # B = int((input()))
    # H = int((input()))
    #
    # print(sleep_for_health(A, B, H))

    # print(is_year_vis(2000))
