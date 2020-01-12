# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Задача 2: вернуть список, который состоит из элементов, общих для этих двух списков
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ans_list = []

# моя версия решения
for el in list1:
    if el in list2 and not (el in ans_list):
        ans_list.append(el)
print(ans_list)

# ответы с сайта:
print(list(filter(lambda elem: elem in list1, list2)))
print([elem for elem in list1 if elem in list2])
print(list(set(list1) & set(list2)))
