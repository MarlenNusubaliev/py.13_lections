# while <условие>:
#     <body>

# i = 0
# while 1:
#     print(f'Srabotalo: {i} raz')
#     i += 1  # i = i + 1   increment


# i = 0

# while i < 10:
#     i +=1
#     print(f'Цикл сработал {i} раз')


# ls = list(range(1, 51))
# ls.reverse()
# print(ls)

# while ls:
#     print(ls.pop())

# 1
# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# print(user)

# i = 3
# password = None
# while password != user['password']:
#     password = input(f'{user["username"]} vvedite porol: ')
#     i -= 1
#     if i == 0:
#         print('Vy Zablokirovany')
#         break
# else:
#     print(f'Vy uspeshno zashli na sait {user["username"]}')
# ---------------------------------------------------------------------------------
# 1.2
# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# print(user)

# i = 3

# while password := input(f'{user["username"]} vvedite porol: ') != user['password']:
    
#     i -= 1
#     if i == 0:
#         print('Vy Zablokirovany')
#         break
# else:
#     print(f'Vy uspeshno zashli na sait {user["username"]}')


# i = 0
# while i < 15:
#     i += 1
#     print(i)

# -----------------------------------------------------------------------------------------------
# for <переменной> in <iterable object>:
    # <body>

# range(1, 5) => 1,2,3,4,5   #iterable
# 'string' -> s t r i n g 
# [1, None, 15, False] -> 1, None, 15, False
# 15 -> -------
# True -> ----------

# i = iter('string')
# print(i)                  Проверка итерация
# print(next(i))
# print(next(i))

# str1 = 'string'
# for x in str1:
#     if x == 'r':
#         continue
#     print(x)
# else:
#     print('End')


# ls = ['Tirion', 'JohnSnow', 'Sansa', 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Sansa':
#         continue
#     print(f'Hello Mr/Mrs {x}!')



# num = 100
# root = int(num ** 0.5)  # корень
# res = []

# for x in range(1, root + 1):
#     print(x)
#     if num % x == 0:
#         res.extend({x, num // x})
# res.sort()
# print(res)




# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Besh-Barmak']
# p = m = k = l = b = 0
# # print(p, m, k, l, b)

# for x in range(1000000):
#     meal = random.choice(ls)
#     if meal == 'Plov': p += 1
#     elif meal == 'Manty': m += 1
#     elif meal == 'Kuurdak': k += 1
#     elif meal == 'Lagman': l += 1
#     else: b += 1

# print('Результат голодных игр: ')
# dict_ = {'Plov': p, 'Besh-Barmak': b, 'Kuurdak': k, 'Manty': m, 'Lagman': l}
# print(dict_)
# =======================================================================================================


"""
1) Создайте список изпользуя циклы.
"""
# i = []
# for x in range(10):
#     print(x)
    
"""
2) Дан список из чисел, запишите чётные числа в один лист а нечётные в другой лист и выведите результат.
"""
# a = [1, 4, 5, 10, 12]
# chet = []
# neChet = []

# for i in a:
#     if i % 2 == 0:
#         chet.append(i)
#     else:
#         neChet.append(i)

# print(chet)
# print(neChet)

"""
3) Напишите программу, которая найдет факториал введенного числа.
"""
# num = int(input('chislo: '))
# f = num

# for i in range(1, num):
#     f *= i

# print(f)

"""
4) Напишите программу, которая будет находить наибольшую цифру натурального
числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

# """
# a = int(input('chislo: '))
# m = a % 10
# a = a // 10

# while a > 0:
#     if a % 10 > m:
#         m = a % 10
#     a = a // 10

# print(m)


"""
5) Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого
числа и записать в новый список.
"""
# import math
# ls = [1, 2, 3, 4, 5]
# a = []

# for i in ls:
#     a.append(math.factorial(i)) 
# print(a)

"""
6) Вам дан список из чисел. Напишите скрипт в котором она запишет в новый список.
"""
# ls = [1, 2, 3, 4, 5] 
# new_ls = []

# for i in ls:
#     new_ls.append(i)

# print(new_ls)

"""
7) Создайте пустой список. Напишите программу которая должна 
записывать в ваш список числа от 0 до 10 включительно.
"""

# ls = []

# for i in range(0, 10):
#     ls.append(i)

# print(ls)

"""
😍 Вам дан список целых чисел. Напишите программу
которая выводит все элементы которые меньше 7.
"""
# ls = [1, 2, 3, 4, 5]

# for i in ls:
#     if i < 7:
#         print(i)