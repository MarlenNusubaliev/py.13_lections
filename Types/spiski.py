# list() -> (списки, массивы) - изменяемый тип данных, который представляет коллекцию каких либо объктов

# my_list = [1, 'string', False, None, [1, 2, 3, 4]]
# print(my_list, type(my_list))
# print(my_list[0])
# print(my_list[-1] [2])
# print(my_list[2:4])

# -----------------------------------------------------------------------------------------------------------------

# range() - возврашает последовательность чисел
# ls = range(1, 10)
# spisok = list(ls)
# print(spisok, type(spisok))
# -----------------------------------------------------------------------------------------------------------------

# tuple() - не изменяюшие типы данных
# tuple_ = (5, 'dfkl', True)
# print(tuple_, type(tuple_))
# a = (5, 7, 9)
# num1, num2, num3 = a
# print(num1, num2, num3)
# b = 5, 6, 4, 8, 9
# print(b, type(b))

# -----------------------------------------------------------------------------------------------------------------
# while
# ls = [1, 2, 3, 4, 5, 6, 'string', False]

# i = 0
# while i < len(ls):
#     # print(i)
#     print(ls[i])
#     i = i + 1 # increment

# for
# ls = [1, 2, 3, 4, 5, 6, 'string', False]
# for x in ls:
#     print(x)

# ls = ['John', 'Sansa', 'Tirion', 'Eddart', 'Jamie', 'Serseya']
# print(ls, len(ls))
# black_list = ['Serseya', 'Jamie']

# for name in ls:
#     if name not in black_list:
#         print(f'We\'re calling to {name}!')
#     else:
#         print(f'{name} is black listed')


# ls -> 1, 21 -> четные числа -> квадрат числа -> нечетные числа -> куб числа

# ls = list(range(1, 21))
# print(ls)

# for num in ls:
#     if num % 2 == 0:
#         print(f'число {num} четное ------> квадат: {num ** 2}')
#     else:
#         print(f'число {num} нечетное ------> куб: {num ** 3}')

# -----------------------------------------------------------------------------------------------------------------

# методы списков 
# print(dir([]))

# append(element) - добавляет елемент в конец списка
# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# print(ls)
# ls.append([True, False, True])
# print(ls)


# extend(object) - расширяет список элементами из objact
# ls = [1, 2, 3]
# print(ls)
# ls.append('Hello')
# ls.append([4, 5, 6])
# print(ls)

# ls = [1, 2, 3]
# print(ls)
# ls.extend('Hello')
# ls.extend([4, 5, 6])
# print(ls)


# insert(index, element) - добавляет элемент по индексу
# ls = ['string', 2, 3, False]
# print(ls)
# ls.insert(2, None)
# print(ls)


# remove(element) - удаляет элемент из списка, если нет такого будет ошибка
# pop([index]) - удаляет или возврашает по index, если нет index то удалит последний элемент

# ls = [5, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# print(ls)
# # ls.remove(5)
# # print(ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [5, 1, 2, 3, 4]
# print(ls)
# deleted = ls.pop()
# print(ls)
# print(deleted)



# update
# ls = [1, 'h', 3, 4, 5, None, 7]
# i = ls.index(None)
# ls[i] = 6
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# ls = ls[::-1]
# print(ls)


# sort() - сортирует список, если передать reverse = True, то список отсортируется в убывающем порядке

# from random import randint
# ls = []
# for x in range(0, 50):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort()
# print('AFTER SORTING')
# print(ls)


# ls = ['John', 'Deyneris', 'Tirion', 'Ocmon', 'Aibek', 'ayjan']
# print(ls)
# ls.sort(key=len)
# print()
# print(ls)



# ---------------------------------------------------------------------------------------


# 1
# ls = range(1, 10)
# spisok = list(ls)
# print(spisok)

# 2
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# p1 = list_.count(333)
# p2 = list_.count(3.1432)
# p3 = list_.count('n')
# print(f"333 встречается:  {p1} раз  \n3.1432 встречается:  {p2} раз  \nn встречается:  {p3} раз")

# 3
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# print(list_.index(86))
# a = list_.pop(6)
# print(list_)

# 4
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333]
# print(sorted(list_))
# print(sorted(list_, reverse=True))

# 5
# ls = [86, 35, 154]
# ls.insert(1, True)
# print(ls)
# ls.extend('dog')
# print(ls)
# ls.append(555)
# print(ls)

# 6
# my_tuple = ("red")
# print(my_tuple, type(my_tuple))

#7
# a = tuple('1',)
# print(a, type(a))

# 8
# tuple_ = ('a', 1, 'Hello', True, ['1', 'b'])
# res = list(tuple_)
# print(res, type(res))
# res.remove('Hello')
# print(res)

# 9
# tuple_ = ('b', 1, 'Hello', True, ['False', 'b'], None, ('tuple'))
# res = list(tuple_)
# print(res, type(res))
# for x in res:
#     if res.index / 2:
#         print(x)