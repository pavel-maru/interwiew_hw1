# 3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число
# генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи
# словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое
# созданных списка и словаря.

import random


# Словарь и список заполняются в общем цикле
def rand(num_1, num_2):
    N = 10
    list_rand = []
    dict_rand = {}
    for i in range(N):
        elem_ = random.randint(num_1, num_2)
        list_rand.append(elem_)
        dict_rand.update({f'elem_{i}': elem_})

    return list_rand, dict_rand


# Словарь и список заполняются в генераторах
def rand2(num_1, num_2):
    N = 10
    list_rand = [random.randint(num_1, num_2) for _ in range(N)]
    dict_rand = {f'elem_{i}': list_rand[i] for i in range(N)}

    return list_rand, dict_rand


lst, dct = rand(1, 100)
print(lst)
print(dct)

print(100 * '*')

lst, dct = rand2(1, 100)
print(lst)
print(dct)
