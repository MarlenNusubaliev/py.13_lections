# 'String - Строки'
# "Hello world, My name is Marlus"

# str = '''
# vb, vlxf z:CV 
# c vzv zdz ddfb bz
# dzf b dzf
# '''

# print(str)
# -------------------------------------------------------------------------------------------------------------------------------
# Строки это набор последовательных символов, которые мы исполбзуем для хранения и представления текстовой информации

# Индексация в строке
# name = 'John'
    # J = 0 = -4
    # o = 1 = -3
    # h = 2 = -2
    # n = 3 = -1

# print(name)
# print(name[-1])
# str = 'world'
# print(str[0], str[3])
# -------------------------------------------------------------------------------------------------------------------------------

# Срезы по индексам
# [start: end <step>]
# str1 = 'birthday'
# print(str1)

# print(str1[0:5])     
# print(str1[:5])  

# print(str1[5:8])
# print(str1[5:])

# text = 'Hello world! My name is Marlus! I\'m human'
# print(text[::2])
# print(text[::-1])
# -------------------------------------------------------------------------------------------------------------------------------

# Конкатенация строк (соединение строк) + 
# a = 'Hello'
# b = 'world'
# c = ' '
# res = a + c + b
# print(res)

# Умножение строк *
# a = 'abc'
# print(a * 5)
# -------------------------------------------------------------------------------------------------------------------------------

# экранрование
# \n -> перенос строки
# \t -> горизонтальная табуляция на 4 пробела
# str1 = "hello world!\n\tHello John"
# print(str1)
# -------------------------------------------------------------------------------------------------------------------------------

# Форматирование строк
# 1. с помощью %
# 2. с использованием .format()
# 3. интерполяция (пребразование строк) f - строки

# %
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# str1 = 'Hello mr/mrs %s %s!' %(name, last_name)
# print(str1)

# .format()
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# club = 'Kipish'
# print('welcome to the club {}, mr/mrs {} {}!' .format(club, name, last_name))

# f - строки
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# print(f'hello mr/mrs {name} {last_name}! welcome to the party!')
# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
# Методы строк - dir()

# print(dir(str))
# replace(old, new, [count]) - меняет в строке old на new, заменит count раз если передатите

# text = 'ha ha ha ha'
# res = text.replace('a', 'e', 2)
# print(text)
# print(f'result after replace: {res}')
# -------------------------------------------------------------------------------------------------------------------------------

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '    hello   '
# print(a)
# print(len(a))

# print(a.strip())
# -------------------------------------------------------------------------------------------------------------------------------

# isdigit     -        Проверяют
# isnumeric   -   состоит ли наша строка
# isdecimel   -     полностью из чисел

# a = '56'
# print(a.isdigit())

# num = input('Vvedite chislo: ')
# print(f'Vvedeno li chislo?: {num.isdigit()}')


# isalpha - Проверяют состоит ли наша строка полностью из алфавита
# txt = 'hello world'
# print(txt)
# print(txt.isalpha())
# res = txt.replace(' ', '')
# print(res)
# print(res.isalpha())
# -------------------------------------------------------------------------------------------------------------------------------

# index(value, [start], [end]) - выводит индекс значения value внутри строки
# find(value, [start], [end]) - делает то же самое что и index, но если не нашел то вернется -1

# text = 'hello John Snow'
# print(text.find('a'))
# print(text.index('a'))
# -------------------------------------------------------------------------------------------------------------------------------

# count(value, [start]) - считает количество символов value внутри строки

# text = 'hello oooo oo o hello'
# print(text.count('a'))
# print(text.count('o'))
# print(text.count('hello'))
# print(text.count('hills'))
# -------------------------------------------------------------------------------------------------------------------------------

# split(separator) - дробит(разделяет) строку на несколько частей по разделителю, все части сохраняются в типе list

# text = 'let me speak by my heart!'
# res = text.split('e')
# print(text)
# print(res)
# print(text.split())

# a = '#hello#hello#hello#hello#hello'
# print(a[1:].split('#'))
# -------------------------------------------------------------------------------------------------------------------------------

# 'connector'.join(list) - соединяет по connector строки которые были в list

# a = '#hello#life#love#bishkek#hiking'
# ls = (a[1:].split('#'))
# print(a)
# print(ls) # ['hello', 'life', 'love', 'bishkek', 'hiking']
# res = '-'.join(ls) # hello-life-love-bishkek-hiking
# print(res)
# -------------------------------------------------------------------------------------------------------------------------------

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

          # john.capitalize() -> John
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'jOHN edart snow'
# print(fio.title())
# print(fio.capitalize())

# -------------------------------------------------------------------------------------------------------------------------------
# Задачи

# 1
# text = 'Lorem'
# print(text[0])

# 2
# text = 'Lorem'
# print(text[-1])

# 3
# text = 'Lorem'
# print(text[-2:])

# 4
# text = 'Lorem one two'
# print(text[::-1])

# 5
# a = 'Hello'
# b = 'John'
# c = ' '
# res = a + c + b
# print(res)

# 6
# a = 'Hello '
# print(a * 4)

# 7
# text = 'Lorem one two'
# print(len(text))

# 8
# text = "The quick brown fox jumps over the lazy dog"
# print(text.replace('o', '*'))

# 9
# text = "The quick brown fox jumps over the lazy dog"
# print(text.upper())

# 10
# text = "The quick brown fox jumps over the lazy dog"
# print(text.lower())

# 11

# text = 'qwerty'
# text = list(text)
# text[0], text[-1] = text[-1], text[0]
# print(''.join(text))

# 12
# a = '#makers#bootcamp#программирование#it#курсы'
# print(a[1:].split('#'))

# 13
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu: ')
# age = input('Vvedite vozrast: ')
# city = input('Vvedite gorod: ')
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

# 14
# text =  'Makers bootcamp'
# print(text[1::2])

# 15
# text = "abracadabra"
# text = list(text)
# text[5] = 'K'
# print(''.join(text))