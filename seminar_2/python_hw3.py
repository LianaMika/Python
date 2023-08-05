# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# def generate_arithmetic_progression(a1, d, n):
#     progression = []
#     for i in range(n):
#         progression.append(a1 + i * d)
#     return progression

# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов: "))

# progression = generate_arithmetic_progression(a1, d, n)

# print("Арифметическая прогрессия:")
# for element in progression:
#     print(element)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# def find_elements_in_range(lst, min_value, max_value):
#     indices = []
#     for index, value in enumerate(lst):
#         if min_value <= value <= max_value:
#             indices.append(index)
#     return indices

# lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# min_value = int(input("Введите минимальное значение: "))
# max_value = int(input("Введите максимальное значение: "))

# indices = find_elements_in_range(lst, min_value, max_value)

# if indices:
#     print("Индексы элементов в заданном диапазоне:")
#     for index in indices:
#         print(index)
# else:
#     print("Нет элементов в заданном диапазоне.")
