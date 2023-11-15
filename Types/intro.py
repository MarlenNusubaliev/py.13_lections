# print("Hello World")
# print('marlus')
# print("my name is John Snow")
# print(5+12)
# print(5>10)
# var = 5+5
# print(var)
# print(var * 15)


# Типы данных в Питоне

# 1. NoneType - ничего, пустота - None
# void = None
# stakan = 'water'
# stakan = None
# print(stakan)

# 2. Boolen - True/False

# 3. String (str) - строки  'dfvsdvASFVLAMDC'
# '''
# dvcsv 
# sdfvDSV
# '''

# 4. Числовые типы данных 
#     a) integer   1, 2, 555
#     b) float     1.5, 25.1615, 45.12
#     c) complex   большие числа

# 5. Списковые типы данных (коллекции)
#     a) list (массив/список) -> [5, 7, 10, true, "hello"]
#     b) tuple (кортеж) -> (1, 2, 3) нельзя изменить значение
#     c) range (последовательность) 

# 6. set() - множество -> {1,2,3,4,5}

# 7. dict() - словари: данные хранятся в виде пар ключ и значение -> {1: 'one', 2: 'two'}

# ------------------------------------------------------------------------


# Mutable(изменяемые типы данных)
# 1. list
# 2. set
# 3. dict

# Immutable(неизменяемые типы данных)
# 1. None
# 2. bool
# 3. int, float, complex
# 4. str
# 5. tuple, range
# 6. frozenset

#---------------------------------------------------------------------------

# Переменные - именованные ячейка памяти, предназначенная для хранения данных. С ее помощью мы можем проводить различные операции с даанными

# num = 5
# str1 = 'Hello world'
# print(num, type(num))
# print(str1, type(str1))

'''
Стандартный вывод данных в терминале
'''
# в питоне для вывода данных в терминале используется функция print()

# stroka = 'hello Marlus'

# print(stroka)

'''
стандартный ввод данных 
используется функция input()
'''

# name = input('your name:')
# print(name, type(name))


# num1 = input('your mum1: ')
# num2 = input('your mum2: ')
# print('Result: ', int(num2) - int(num1))


# 1 задание
# num1 = int(input('first num:'))
# num2 = int(input('second num:'))
# print('Result: ', num1 + num2)
# print('Result: ', num1 - num2)
# print('Result: ', num1 * num2)
# print('Result: ', num1 / num2)
# print('Result: ', num1 ** num2)
# print('Result: ', num1 % num2)
# print('Result: ', num1 // num2)

# 2 задание

# num1 = int(4)
# print('Result: ', num1 + num1 + num1)
# print('Result: ', num1 * num1 * num1)
# print('Result: ', num1 ** num1 ** num1)

# 3 задание 

# print('''
# имя:   Марлен
# email: marlen@gmail.com
# ''')

# 4 задание 

# name = input('Ваше имя: ')
# print('Здравствуйте', name)

# 5 задание

# hight = float(input('hight: '))
# width = float(input('width: '))
# print('S = ', hight * width, 'м.кв')


# not finish
# sum = float(input('Сумма заказа: '))
# tax = 0.08 + sum
# chai = 0.18 + sum
# print('итог: ', sum + tax + chai, '      !      ', 'итог: ', tax, 'чай: ', chai)


# 6 задание
# num = int(input('Ваш номер: '))
# if num % 2 == 0: print('четное')
# else: print('не четное')
