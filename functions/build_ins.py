# zip(iterabbles) - она соединяет каждый элемент итериемых объектов между собой в тип tuple и возвращает итератор


# ls1 = [1,2,3]
# ls2 = [100, 200, 300]

# res = list(zip(ls1 , ls2))
# print(res)
# res = dict(zip(ls1 , ls2))
# print(res)

# -----------------------------------------------------------------------
# all(), any()
# all(iterable) - Возвращает True если все элементы итериркемого объекта истина иначе False


# ls = [[1,2], 'stroka', True, 1]  # True
# ls = [[1,2], 'stroka', True, 1, ''] # False
# print(all(ls))


# ip = '10.255.12.155'
# ip2 = '10.255.1y.155'

# result = all(x.isdigit() for x in ip.split('.')) # True
# result2 = all(x .isdigit() for x in ip2.split('.')) # False
# print(result)
# print(result2)



# any- Возвращает True если хотябы один элемент истина

# ls = [0, 0, 0, 0] # False
# print(any(ls))
# ls2 = [0, 0, 0, 1] # False
# print(any(ls2)) # True


# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']

# command = input('Vvedite commandu: ')
# if any(x in command for x in ignore):
#     raise Exception('You do not have permision')

# print('OK')

# ============================================================================================

# Аноонимные функции - lambda(такие же функции только без названия)
# lambda функции могут принимать сколько угодно аргументов но всегда возвращает одно выражение

# def sum_of_args(a, b):
#     res = a + b
#     return res

# print(sum_of_args(5, 15))



# func = lambda a, b:a + b  
# print(func(15,15))



# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(123))
# print(myDoubler(7))

# print(myTripler(55))



# dict_ = {'John': 50_000, 'Jamie': 100_000_000, 'Aibek': 1_000_000, 'Aigerim': 15}

# res = sorted(dict_.items(), key=lambda x: x[1])
# print(res)
# ---------------------------------------------------------------------------------------------



# map(function, iterable) -> применяет ко всем элементам iterable функциям которым мы передаем

# ls = ['one', 'two', 'three', 'four', 'five']
# res = list(map(str.upper, ls))
# print(res)

# for i in range(len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)



# names = ['John', 'Sultan', 'Jamie', 'Aibek']
# -------------
# res = list(map(lambda name:f'Hello mr/mrs {name}', names))
# print(res)

# ------------

# def func(name):
#     return f'Hello mr/mrs {name}'

# res = []
# for name in names:
#     res.append(func(name))

# print(names)
# print(res)
# -----------------------------


# dict_ = {1: 2, 3: 4, 5: 6}
#         #{1: '2', 3: '4', 5: '6'}

# res = dict(map(
#     lambda x: (x[0], str(x[1])),
#     dict_.items()))

# print(res)



# TODO filter, reduce, enumarate, repeat 



'''
filter(function, iterable) - применяется ко всем элем iterable функ которую мы передали и возвращает 
итераьор с теми элем для котор функ вернула True

'''

# ls = ['one', 'two', '', 'list', '100', '1' , 'john']

# res = []

# for x in ls:
#     if x.isdigit():
#         res.append(x)

# print(res)


# res = list(filter(str.isdigit, ls))
# print(res)
# ---------

# ls = ['john', 'codify', 'Aibek', 'bootcamp', 'ono', 'Kyrgyzstan', 'mountains']

# res = list(filter(lambda x: len(x) > 5, ls))
# print(res)
# ==========


# ls = [
#     {'name': 'Pthon', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'Js', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 0},
#     ]

# res = list(filter(lambda dict_: dict_['point'] > 7, ls))
# print(res)
# ----------------

# users = [
#  {"username": 'John', "comments": ["I love this content", "Realy Good"]},
#  {"username": 'Raychel', "comments": []},
#  {"username ": 'Steven', "comments": ["Bishkek", "Python"]},
#  {"username ": 'Hello', "comments": []},
#  {"username ": 'Kira', "comments": ["The best"]},
# ]
# res = list(filter(lambda x: x['comments'], users))
# print(res)

# res2 = list(filter(lambda x:not x['comments'], users))
# print(res2)
# ======================================================

# names = ['Aigerim', 'Sultan', 'John', 'Kira', 'Bob']
# new_names = list(map(lambda x: f'Hello mr/mrs {x}', filter(lambda x: len(x) > 5, names)))
                 
# print(new_names)


# ================================================================================
# enumerate - она пронумеровывает каждый элем внутри iterable ее собственным индексом

# ls = ['one', 'two', 'three', 'four', 'five']

# res = list(enumerate(ls))
# print(res)     # [(0, 'one'), (1, 'two'), (2, 'three'), (3, 'four'), (4, 'five')]

# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}')

'''
Index: 0, Element: one
Index: 1, Element: two
Index: 2, Element: three
Index: 3, Element: four
Index: 4, Element: five
'''
# --------------------------------------------------------------
'''
reduce - Функция Reduce () принимает функцию и последовательность и возвращает одно значение, 
рассчитанное следующим образом:
1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и 
результат возвращается.
2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим 
значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности 
не появятся элементы.

'''
# from functools import reduce

# ls = [1,2,3,4,5]
# sum_ = reduce(lambda a, b: a + b, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(sum_, res)
# ---------------------------------------------------------------------------------
# repeat

# for x in repeat(lambda x: x * 5, 5):
#     print(x)
# ========================================================================================
# Генератор паролей
from itertools import repeat
from random import choices
from string import ascii_letters, digits
from statistics import mean

symbols = '_()$!%+-@#'

q_pass = int(input('Vvedite kolichestvo poroley: '))

result = {
    f(choices(ascii_letters, k=10), 
      choices(digits, k=5),
      choices(symbols, k=2))
    for f in repeat(lambda a,d,s: ''.join(set(a+d+s)),
     q_pass)
}

print(result)
print(f'Quantity of passwords: {len(result)}')
dlina = [len(x) for x in result]
print(f'Average len: {mean(dlina)}')




























# ==================================================================================================

"""
1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
"""
# import functools

# list_ = [1, 2, 3, 4]

# sum = functools.reduce(lambda x, y: x + y, list_)
# print(sum)




"""
2) Дан списка из чисел. Проверьте, что все числа больше трёх.
"""
# list_ = [1, 2, 3, 4]

# res = list(map(lambda x: x > 3, list_))
# print(res)



"""
3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
"""
# list_ = [1, 2, 3, 4]

# res = list(map(lambda x: x < 0, list_))
# print(res)



"""
4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
"""
# list_ = [1, 2, 3, 4]
# kvad_sum = list(map(lambda x: x ** 2, list_))
# print(kvad_sum)



"""
5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
"""
# list_ = [1, 2, 3, 4]reduc
# res = list(filter(lambda x: x % 2 == 0, list_))
# print(res)


"""
6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
"""
# list_ = ['55555', '666666', '999999999', '88888888']
# res = list(filter(lambda x: len(x) > 7, list_))
# print(res)



"""
7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
"""
# from functools import reduce 
# list_ = [5, 6, 7, 8]
# res = reduce(lambda x, y: x*y, list_)
# print(res)


"""
😍 Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
"""
# list_ = [1, 2, 3, 4, 5, 6]
# print(filter(lambda x: 'Chet:'+1 if x%2==0 else 'Ne_chet:'+1, list_))

"""
9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .
"""
# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# res = list(map(lambda x: False if x < 0 else True, list_))
# print(res)



"""
10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
# from functools import reduce

# list_ = ['John', 'Ali', 'Aibek', 'Pain']

# res = reduce(lambda a, b: a if (a < b) else b, list_)

# print(res)

# 11 
# digits = '123456789'
# intt = int(digits)
# print(intt, type(intt))
# print(sum(intt))

# 12
# sum = int(input('sum: '))
# res = lambda sum: sum ** 2
# print(res(sum))


# 13
# sum = int(input('sum: '))
# sum2 = int(input('sum2: '))

# res = lambda x, y: sum ** sum2
# print(res(sum, sum2))


# 14

# names = input('name: ')

# res = list(map(lambda name: f'Hello {names}', names))
# print(res)

# 15

# num = [1,2,3,4,5,6,7,8,9,10,15,20]

# res = list(filter(lambda x: x % 5 == 0, num))
# print(res)
