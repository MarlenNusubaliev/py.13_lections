# Работа с файлами

# Каретка - Указатель - Курсор
# 
# open(<путь до файла>)

# file = open('files.py') #Относительный путь
# ~working -> Desktop/bootcamp.05/files/lections/files.py
#  files -> lections/files.py

# base_dir = '/Users/marlen/Documents/bootcamp-Python/files'
# file = open(base_dir + 'lections/files.py')

# file = open('files.py')
# data = file.read()
# print(data, type(data))
# file.close()

# --------------------------------------------------------------
#  Режимы работы с файлами
# 1. r/r+/rb - read - для чтение файла
# 2.w/w+/wb - write - Для записи данных
# 3.a/a+  -> для добавление данных
# b, x

# file = open('test.txt')
# print(file.read())
# file.close()



# file = open('test.txt')
# print(file.readlines())   # ['John Snow in King of North!\n', 'You know nothing John Snow!\n']
# file.close()

# file = open('test.txt')
# print(file.readline())
# print(file.readline())
# file.close()


# file.tell() - Возвращает индекс где находится курсор
# file.seek() - Перемешает курсос на индекс который вы передaли



# file = open('test.txt', 'r')
# print(file.tell()) # 0
# data = file.read()
# print(data, '!!')
# print(file.tell()) # 254
# file.seek(0)
# print(file.tell()) # 0
# print(file.read())
# print(file.tell()) # 254
# file.close()

# -------------------------------------------------------
# Контексный менеджер
# with open('test.txt', 'w') as file: # file = open()
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file.read(), 'outside')

# with open('test.txt', 'w') as file:
#     file.write('Pervaya stroka')
#     file.write('\nHe is bastard of Ned Stark\n')
#     file.write('this lesson ok')
#     file.seek(0)
#     data = ['Test 1 stroka\n', 'Test 2 stroka']
#     file.writelines(data)

# with open('test.txt', 'a+') as f:
#     f.seek(0)
#     f.write('\nJohn Snow is King')
#     f.write('\nYou know nothing')
#     f.seek(0)
#     print(f.read())

# ======================================================
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# base_url = '/home/marlen/Documents/bootcamp-Python/files/lections/'


# def get_imei_code(image: str):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d:\s\d+', string)
#     print(list_of_imei)

#     with open('list_of_imei', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)
#             #   for x in list_of_imei:
#             #     file.write(f'{x}\n')

# image = base_url + 'imei.jpg'
# get_imei_code(image)




# ===================================================================================

"""
1) В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.
"""
# f = open('/home/marlen/Documents/bootcamp-Python/files/lections/testTG.txt')
# count = 0
# count_i = 0
# x = []
# y = []
# for line in f:
#     count += 1
#     for i in line:
#         count_i += 1

#     x.append(count_i)
#     count_i = 0
#     line = line.split()
#     y.append(len(line))


# f.close()
# print(count)
# print(x)
# print(y)


"""
2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
пробел. Напишите программу, которая подсчитывает и выводит на экран
общую сумму чисел, хранящихся в этом файле.
"""

# with open('nums.txt', 'r') as f:
#     n = f.read()
#     print(n)
#     n = n.split()
#     print(n)
#     n = sum([int(i) for i in n])
#     print(n)


"""
3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
записать их произведение в файл output.txt.
"""
# with open('input.txt', 'w') as f:
#     n = f.write('1 2 3 4 5 6 7 8 9 10')
    
#     print(n, type(n))
# import math
# with open('input.txt', 'r') as f:
#     n = f.read()
#     n = n.split()
#     n = [int(i) for i in n]
#     n = math.prod(n)

# with open('output.txt', 'w') as f:
#     f.write(str(n))
    
"""
6) В файле записаны в целые числа. Найти максимальное и минимальное
число и записать в другой файл.
"""
# with open('sum.txt', 'r') as f:
#     n = f.read()
#     print(n, type(n))
#     n = n.split()
#     print(n, type(n))
#     min = 0
#     n = [int(i) for i in n]



"""
7) В файле записаны в столбик целые числа. Отсортировать их по
возрастанию суммы цифр и записать в другой файл.
"""


# with open('to_do_list.txt', 'w') as f:
#     n = f.write(1,2,3,4,5)

# with open('to_do_list.txt', 'r') as f:
#     n = f.read()
#     print(n)

