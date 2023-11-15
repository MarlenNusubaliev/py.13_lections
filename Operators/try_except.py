# обработка исключений
# операторы try...except

# Ошибки Error -> Связаны с кодом 
    # SyntaxError
    # TabError
    # IndentationError

# a = 5
# b = 6)

# Исключение Exception -> связаны с неправильным вводом данных которые передаются в коде

# ValueError
# TypeError
# NameError
# ZeroDivisionError
# IndexError
# KeyError
# ImportError
# BaseException # прородитель всех ошибок




# try:
#     num1 = int(input('Enter num1: '))
#     num2 = int(input('Enter num2: '))
#     print(num1 / num2)
# except ValueError:
#     print('Invalid values for num')
# except ZeroDivisionError:
#     print('Cant divide by zero')

# try: 
#     <body> # код с вероятным исключением
# except:
#     <body except> # сработает тоько если ошибка в try
# else:
#     <body> # сработает только если нет ошибки в try
# finally:
#     <body> # сработает в любом случае                                                           


# dict_ = {1: 'one', 2: 'two', 3: 'three'}
# print(dict_)
# try:
#     key = int(input('Vvedite key: '))
#     print(dict_[key])
# except ValueError:
#     print('Invalid value for key')
# except KeyError:
#     print('Key does not exists')
# else:
#     print('No errors')
# finally:
#     print('The end')

# ==============================================================================

# отбражение ошибок
# 1. import sys

# ls = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index: '))
#     print(ls[index])
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error!')


# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'oops, we catched {e.__class__} error!')


# ===================================================================================

# flag = True
# symbols = '0123456789' + '-' + '.'

# while flag:
#     print()
#     num1 = input('chislo1: ')
#     num2 = input('chislo2: ')
#     try:

#         num1 = (float(num1) if '.' in num1 else int(num1))
#         num2 = (float(num2) if '.' in num2 else int(num2))
#     except ValueError:
#         print('Вы ввели некорректное число')
#         continue

#     operator = input('vvedite operaciu(+,-,*,/): ').strip()

#     if operator == '+':
#         print(f'res:  {num1 + num2}')
#     elif operator == '-':
#         print(f'res:  {num1 - num2}')
#     elif operator == '*':
#         print(f'res:  {num1 * num2}')
#     elif operator == '/':
#         print(f'res:  {num1 / num2}' if num2 != 0 else 'na 0 ne dilitsa')
#     else:
#         print('Nevernyi operator')

#     choice = input('Hotitte prodoljit?(yes/no): ')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print('buy')

"""
1) Опишите полный синтаксис конструкции try-except:
"""

#  try: 
#     <body> # код с вероятным исключением
# except:
#     <body except> # сработает тоько если ошибка в try
# else:
#     <body> # сработает только если нет ошибки в try
# finally:
#     <body> # сработает в любом случае



# 2. Обработайте ошибку, которая может возникнуть.
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Name error')

"""
3) Напишите программу которая будет получать два числа через input и делить одно на другое. 
Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.
"""

# try:
#     num1 = int(input('num1: '))
#     num2 = int(input('num1: '))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print('Cant delite na NOLLLL')


"""
4) Напишите программу, которая будет получать через инпут 2 числа и будет печатать их сумму. 
Обработайте ошибку, которая возникнет, если пользователь введёт не числовое значение и выведите 
сообщение.
"""

# try:
#     num1 = int(input('num1: '))
#     num2 = int(input('num1: '))
#     print(num1 + num2)
# except ValueError:
#     print('TypeErroRRRRR')


"""
5) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, 
если запрашиваемый ключ не существует.
"""

# dict_ = {1: 'one', 2: 'two', 3: 'three'}
# print(dict_)
# try:
#     key = int(input('vvedite key: '))
#     print(dict_[key])
# except KeyError:
#     print('keyERRRORRRRR')

"""
6)  Дан список. Обработайте исключение при попытке обращения к несуществующему элементу.
"""

# ls = [1,2,3,4,5]
# print(ls)
# try:
#     user = int(input('vvedite el: '))
#     print(ls.index(user))
# except ValueError:
#     print('NOOOOOOO nEEEEEET ErrrrOOOOOOr')

"""
7) Попытайтесь в блоке try принять 2 числа и разделить одно на другое. 
В блоке except обработайте сразу 2 возможных исключения.
"""
# try:
#     num1 = int(input('num1: '))
#     num2 = int(input('num1: '))
#     print(num1 / num2)
# except ValueError:
#     print('Value Errrrroooorrrr')
# except ZeroDivisionError:
#     print('Na 0 / nelzyia')


"""
😍 Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, 
меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
"""

# sum = int(input('sum: '))
# if sum < 0:
#     raise ValueError("Сумма не может быть отрицательной!")



"""
9)  В блоке try запросите у пользователя ввод его возраста. Затем в том же блоке проверьте 
его возраст на совершеннолетие. Если пользователь несовершеннолетний, выбросите исключение с 
текстом "Доступ запрещён". Обработайте также исключение если пользователь вводит текст вместо числа 
с сообщением 'Введен некорректный возраст'. Если ошибок не возникло, то распечатайте сообщение
 "Спасибо!", а затем "До свидания", вне зависимости от того, произошла ошибка или нет.
"""
# try:
#     num1 = int(input('age: '))
#     if num1 < 16:
#         print('Доступ запрещён')
   
    
    
# except Exception:
#     print('Введен некорректный возраст')
# print("До свидания")



