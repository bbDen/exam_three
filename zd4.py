"""Заполните 2 списка а и b случайными целыми
числами и верните 3 список общих для а и b элементов
"""

import random

a = []
b = []


def full_list(mas):
    for i in range(10):
        mas.append(random.randint(0, 20))
    return mas


full_list(a)
full_list(b)


def check_lists(list1, list2):
    equal_list = [list1[i] for i in range(len(a)) if list1[i] in list2]

    return equal_list


print(check_lists(a, b))
