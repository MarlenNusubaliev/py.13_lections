# Типы данных - Числа -> int, float

# = -> оператор присваивание
# variable(переменная)
# num = 5
# print(num)
# num = 79 
# print(num)


# PEP8 - правила написание кода на Python
# tomorrow_day = '27.09.2023' # Snake case
# tomorrowDay = '27.09.2023' # Camel case


# +
# num1 = 56
# num2 = 115
# print('Result:', num1, '+', num2, '=', num1 + num2)


#  -
# print(55-22)
# print(55.5-32)


# *
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# # num1 = int(num1)
# # num2 = int(num2)
# print('Result:', num1, '*', num2, '=', num1 * num2)


# / - обычное деление
# // - деление без остатка
# % - модульное деление (получаем остаток)

# num1 = 7
# num2 = 3
# print('/', num1 / num2) # 2.333333...
# print('//', num1 // num2) # 2
# print('%', num1 % num2) # 1


# **
# print(5 ** 2)
# print(5 ** 4)

# pow - возведение в степень
# pow(num1, num2, <mod>)
# print(pow(5, 3, 10))


# round() - округление числа с точкой
# num = 5.367
# print(round(num, 2))


# abs() - абсолютное значение -> |-67| -> 67
# a = abs(-16)
# b = abs(16)
# print(a, b)


# divmod(a, b) -> Она выводит два числа, первое число это a // b a второе число a % b
# print(divmod(5, 2)) # -> 5 // 2, 5 % 2


# множественное присваивание

# num1, num2, num3 = 4, 10, 7
# print(num1, num2, num3)


# num1, num2 = divmod(27, 5)
# print(num1, num2)


# import math

# res = math.sqrt(144)
# print(res)

# res = math.factorial(5)
# print(res)

"""Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал"""

# import math

# r = int(input('Vvedite radius: '))
# chislo_pi = math.pi

# res_P = 2 * r * chislo_pi
# res_S = chislo_pi * (r ** 2)
# print('S окружности: ', round(res_S, 2))
# print('P окружности: ', round(res_P, 2))



# 1.
# a = int(5)
# print(a, type(a))

# 2.
# a = 'str'
# print(a, type(a))

# 3.
# a = 5
# b = ' one'
# print(b * a)

# 4.
# a = 5
# b = 4
# print('Result:', a, '+', b, '=', a + b)

# 5.
# a = 10
# b = 3
# print(a / b)

# 6.
# a = abs(20)
# b = abs(-16)
# print(a, b)

# 7.
# num = 4
# print(pow(num, 3))

# 8.
# a = 10
# b = 3
# print(a % b)

# 9.

# num = 15; print(pow(num, 2, 5))

# 10.
# num1 = int(input('1 число: '))
# num2 = int(input('2 число: '))
# num3 = int(input('3 число: '))
# res = num1 * num2
# print('Result:', num1, '*', num2, '=', res)
# print('Result:', res, '%', num3, '=', res % num3, 'остаток')

# 11.
# num1 = int(input('1 число: '))
# num2 = int(input('2 число: '))
# num3 = float(input('3 число: '))

# res = num1 % num2
# print('Result:', num1, '%', num2, '=', res, 'остаток')
# print('Result:', res, '*', num3, '=', res * num3)

# 12.
# import math

# num = float(input('Vvedite chislo: '))
# kvad = num ** 2
# cube = num ** 3
# kvad_kor = math.sqrt(num)

# print('Квадрат', num, 'равен', kvad)
# print('Куб', num, 'равен', cube)
# print('Квадратный корень', num, 'равен', kvad_kor)

# 13.

# import math
# a = int(input('a: '))
# b = int(input('b: '))
# c = math.sqrt((a**2) + (b**2))
# print(c)

# 14.
# import math

# r = int(input('Vvedite radius: '))
# chislo_pi = math.pi

# res_P = 2 * r * chislo_pi
# print('P окружности: ', round(res_P, 2))

# 15.
# x = 5
# y = 6
# z = 7

# x, z, y = y, x, z
# print(x)
# print(z)
# print(y)


# 1.1
# import time


# time_local = time.asctime()
# print(time_local)


# sec = int(input('Введиде время: '))
# min = int(input('Введиде время: '))
# hour = int(input('Введиде время: '))
# day = int(input('Введиде время: '))
# print(sec + (min * 60) + (hour * 60 * 60) + (day * 60 * 60 * 24))


# fut = int(input('Введиде время: '))
# dum = int(input('Введиде время: '))
# yard = int(input('Введиде время: '))
# mill = int(input('Введиде время: '))
# print(fut * 12, yard * 3, mill / 5280)



