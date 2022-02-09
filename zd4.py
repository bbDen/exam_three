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
    equal_list = []
    for i in list1:
        if i in list2:
            equal_list.append(i)

    return equal_list


print(check_lists(a, b))
