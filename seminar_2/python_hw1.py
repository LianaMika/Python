# # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# # Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# # Выведите минимальное количество монет, которые нужно перевернуть

# massiv = [0, 1, 0, 1]
# count_zero = 0
# count_one = 0
# for element in massiv:
#   if element == 0:
#     count_zero +=1
#   elif element == 1:
#     count_one +=1
# if count_zero > count_one:
#   print(count_one)
# else:
#   print(count_zero)


# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# # Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# # Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# def find_numbers(S, P):
#     for x in range(1, 1001):
#         y = S - x
#         if 1 <= y <= 1000 and x * y == P:
#             return x, y
#     return None, None

# sum_hint = int(input("Enter the sum (S): "))
# product_hint = int(input("Enter the product (P): "))

# X, Y = find_numbers(sum_hint, product_hint)

# if X is not None and Y is not None:
#     print(f"The two numbers are: {X} and {Y}")
# else:
#     print("No valid solution found within the constraints.")
  
  
# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# def powers_of_two(N):
#     k = 0
#     power_of_two = 1
#     while power_of_two <= N:
#         print(power_of_two)
#         k += 1
#         power_of_two = 2 ** k

# # Test the function with a sample value of N
# N = int(input("Enter the value of N: "))
# powers_of_two(N)

