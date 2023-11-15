# найти квадрат и куб результат деление на 100 любого числа

# num1 = 5
# ->{'num': 5, '2': 25, '3': 125, '100': 0.05}


# num1 = 5
# res = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100}
# print(res)

# num2 = 75
# res = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100}
# print(res)

# num3 = 1154
# res = {'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100}
# print(res)


# DRY - Don't repeat yourself

# def do_operations(num: int):
#     res = {'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100}
#     print(res)

# do_operations(16)
# do_operations(4356)
# do_operations(31)
# do_operations(1298)
# do_operations(567)

# ===========================================================
'''
Фукнция - это именованная часть программы, которая содержит в себе определенный набор инструкции , 
и может вызываться в других частях программы столька раз сколько угодно
'''

# def name_of_func(<a, b> #параметры функции):
    # <body> # код какая то логика которое будет давать конечный результат
    #   <return> оператор который помогает сохранить результат

    #name_of_func(5, 6 аргументы)

# параметры функ - переменные в которых мы временно сохр данные которые передаем 
# при вызове в функ, доступно только внутри функ


# аргументы функ - данные которы е мы передаем при вызове функ они попадают в параметры по очереди


# print(len('string'))
# from typing import Iterable


# def our_len(obj: Iterable) -> str:
#     '''Возврашает длину итерируемого объекта'''
#     print(obj)
#     i = 0
#     for _ in obj:
#         i += 1
#     return f'result: {i}'

# ls = [1,2,3,4,5]
# str1 = 'Hello world s vami John Snow!'

# print(our_len(ls))
# print(our_len(str1))

# def isEven(num):
#     return True if num % 2 == 0 else False

# result = isEven(15)
# print(result)

# def isEven(num: int) -> bool:
#     '''Return True or False while after checking number for even'''
#     return True if num % 2 == 0 else False
# result = isEven(456)
# print(result)

# ------------------------------------------------------------------------

# default параметры

# def sum_of_args(a: int, b: int, c: int=0) -> int:
#     '''returns sum of given arguments'''
#     return a + b + c


# print(sum_of_args(5, 6, 7))
# print(sum_of_args(9, 123))

# ----------------------------------------------------------------------------

# позиционные и именованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(5, 10, 15) позиционные арг
# (arguments)
# print()
# printParams(b=5, a=10, c=15)  именованные арг
# (keyword arguments)
# print()
# printParams(5, c=10, b=15)

# -----------------------------------------------------------------------
# оператор *
# a = [1,2,3]
# b = [4,5,6]

# c = [*a, *b]
# print(c)

# ---------------------------------------------------------------------

# *args, **kwargs

# def get_some_dat(a, b, *args, **kwargs): 
#     print('parametry a и b:', a, b)
#     print('аргументы', args)
#     print('именованные аргументы', kwargs)

# get_some_dat(1,2,3,4,5, x=5, car='BMW')

# def printScores(student: str, *scores)-> None:
#     '''prints info about student to terminal'''
#     print(f'Name of student: {student}')
#     print(f'AVG: {round(sum(scores) / len(scores), 1)}')
#     print(scores, type(scores), '!!!!')
#     for x in scores:
#         print('Scores:', x)

# printScores('John Snow', 5, 5, 5, 5, 4, 4, 2)


# def printPetNames(owner: str, **pets):
#     print(f'owner name {owner}')
#     print(pets, type(pets), '!!!!!!!!!!!!!!!!!!')
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}', *name,)
#         else:
#             print(f'{pet}: {name}')
#         # print(f'{key}: {pets[key]}' if type(pets[key]) != list else f'{key}')

# printPetNames('John Snow', dog='Pluto', cat='Barsik', fish=['Nemo', 'Dori', 'Golden'], turtle='Leonardo')


# -------------------------------------------------------------------------------------------

# from random import choice, shuffle
# from string import ascii_letters, digits, punctuation

# symbols = ascii_letters + digits
# # print(symbols)

# def generate_password(len_: int=8) -> str:
#     '''Function generate random string for password parameter len needs to give lenghts of password,
#     if blank len_ = 8'''

#     res = [choice(symbols) for _ in range(len_ -2)] + [choice(punctuation) for _ in range(2)]
#     shuffle(res)
#     return ''.join(res)

# print(generate_password())
# print(generate_password(12))
# print(generate_password(16))
# print(generate_password(9))


# ================================================================================================

"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def myFn(a: int, b: int):
#     res = a + b
#     print(res)
# myFn(5, 10)

"""
2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой 
строки(не использовать функцию len).
"""
# def myFn(obj: str):
#     print(obj)
#     i = 0
#     for _ in obj:
#         i += 1
#     return f'Dlina str: {i}'

# a = 'John Snow'
# print(myFn(a))

"""
3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции 
выводить тип принятых аргументов.
"""
# def myFn(a, b):
#     print(type(a))
#     print(type(b))
# myFn(15, 'ppp')


"""
4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def myFn(a: int, b: int):
#     res = a / b
#     print(res)
# myFn(15, 3)

"""
5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте
 все его ключи
"""
# def myFn(a: dict):
#     for k in a.keys():
#         print(k)

# b = {'1': 111, '2': 2222}
# myFn(b)

"""
6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и
 "It's even number" в противном случае.
"""

# def myFn(a):
#     if a % 2 == 0:
#         print("It's odd number") 
#     else:
#         print("It's even number")
# myFn(11)

"""
7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом.
 Пробелы и регистр учитывать не нужно.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в
 обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
"""
# def myFn(a: str):
#     if a == a[::-1]:
#         print('палиндром')
#     else:
#         print('не палиндром')
# myFn('marlen')


"""
😍 Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа
 между собой и вывести максимальное значение.
"""
# def myFn(z: int, x:int):
#     if z > x:
#         print(z)
#     else:
#         print(x)  

# a = int(input('1: '))
# b = int(input('2: '))

# myFn(a, b)

"""
9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def f(a):
# 	b = 1
# 	i = 0
# 	while i < len(a):
# 		b = int(a[i]) * b
# 		i += 1
# 	return b
		

# a = list(input('num: '))
# print(f(a))

"""
10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр.
 Например, число 123 --> 6
"""


# def f(a):
# 	b = 0
# 	i = 0
# 	while i < len(a):
# 		b = int(a[i]) + b
# 		i += 1
# 	return b



# a = input('num: ')
# print(f(a))




# chat bot