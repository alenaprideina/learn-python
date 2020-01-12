def minutes_from_hm(x, y):
    return x*60 + y


def minutes_to_hm(m):
    return m // 60, m % 60


def hm_plus_minutes_to_hm(x, h, m):
    return ((h * 60 + m) + x) // 60, ((h * 60 + m) + x) % 60
