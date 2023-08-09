# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# def count_vowels(word):
#     vowels = "аоуыэеёиюяАОУЫЭЕЁИЮЯ"
#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count

# def check_rhythm(poem):
#     lines = poem.split()
#     syllable_counts = []

#     for line in lines:
#         words = line.split("-")
#         syllable_count = sum(count_vowels(word) for word in words)
#         syllable_counts.append(syllable_count)

#     if all(count == syllable_counts[0] for count in syllable_counts):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# poem = input("Введите стихотворение Винни-Пуха: ")

# result = check_rhythm(poem)
# print(result)



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)