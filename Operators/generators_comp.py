# generator

# print(x for x in range(1, 10))

# x, a, b = (x for x in range(1,4))
# print(x, a, b)

# list coprehentions - генераторы списков
# list coprehentions - упрощенный подхов к созданию списков, который задействует в себе цыкл for, а так же конструктор if для определение того, что в итого попадает в наш список

# list -> 0 - 200 -> четные числа
# 1
# ls = []
# for x in range(0, 200):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)

# # 2
# ls = [x for x in range(0, 200) if x % 2 == 0]
# print(ls)


# 2 условие
# ls = [x for x in range(0, 300) if x % 2 == 0 and x % 5 == 0]
# print(ls)



# # set coprehentions
# set = {x for x in range(0, 300) if x % 2 == 0 and x % 5 == 0}
# print(set)


# list - 0, 100 -> x 2 -> x ** 2 , 3 -> x ** 3

# ls = [x ** 2 if x % 2 == 0 else x ** 3 
#     for x in range(0, 100)
#     if x % 2 == 0 or x % 3 == 0]
# print(ls)


# ls = [[1,2,3], [4,5,6], [7,8,9]]
#        # [1,2,3,4,5,6,7,8,9]

# res = [item for x in ls for item in x]
# print(res)


# таймер 

# from datetime import datetime

# start = datetime.now()
# ls = [x for x in range(0, 100_000_000)] #5
# finish = datetime.now()
# print(finish - start)





# start = datetime.now()
# ls = []
# for x in range(0, 100_000_0000): #9
#     ls.append(x)
# finish = datetime.now()
# print(finish - start)

# --------------------------------------------------
# dict coprehentions

# dict_ = {x: x ** 2 for x in range(1, 11)}
# print(dict_)


# names = ['John', 'Tirion', 'Sansa', 'Eygan', 'Ramsi']
# res = {name: len(name) for name in names}
# print(names)
# print(res)





# example


"""
1) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.
Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
"""
# dict_ = {'Мурату': 24, 'Эржану': 21, 'Карине': 24, 'Алтынай': 17, 'Айбеку': 16}
# print(dict_)

# for k, v in dict_.items():
#     if v > 17:
#         print(f'{k} Вы проходите')
#     else:
#         print(f'{k} Приходи когда выростешь')



"""
Задание 
Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) 
и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), введенное пользователем. 
Ключом будет само число, а значением его квадрат.
"""

# n = int(input('Введите число от 1 до 10: '))
# 1 var 
# dict_ = {x: x ** 2 for x in range(1, 501) if x % n == 0}
# 2 var
# for x in range(1, 501):
#     if x % n == 0:
#         dict_[x] = x ** 2

# print(dict_)

        





"""
1) Создайте список из целых чисел от 1 до 100.
"""

# ls = [x for x in range(1, 100)]
# print(ls)

"""
2) Создайте список из нечётных целых чисел в промежутке от 1 до 50.
"""
# ls = [x for x in range(1, 50) if x % 2 != 0]
# print(ls)

"""
3) Создайте список используя int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4] и запишите в новый список только четные числа, 
    которые больше нуля.
"""
# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# new_ls = [x for x in int_list if x > 0]
# print(new_ls)

"""
4) Создайте список из квадратов всех чисел от 1 до 25 (включительно).
"""
# ls = [x ** 2 for x in range(1, 25)]
# print(ls)

"""
5) Объявите новый список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] и конвертируйте строковые данные 
    в целочисленные.
"""
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# print(str_list, type(str_list))
# a = [int(x) for x in str_list]
# print(a)

"""
6)  Пройдитесь по промежутку чисел от 1 до 10 (включительно), если число нечётное, запишите в список само число, если же чётное,
    то квадрат этого числа.
"""
# ls = [x ** 2 if x % 2 == 0 else x for x in range(1, 11)]
# print(ls)

"""
7) Пройдитесь по промежутку чисел от 1 до 10 и запишите в список True, если число чётное и False в противном случае.
"""
# ls = [True if x % 2 == 0 else False for x in range(1, 10)]
# print(ls)

"""
8) Создайте список из 10 произвольных имён, затем пройдитесь по данному списку и если имя состоит меньше чем из 4 букв 
    замените имя на 'shorter', а если больше на 'longer'.
"""
# ls = ['John', 'San', 'Tirion', 'Tom', 'Jerry', 'Naruto', 'Saske', 'Will', 'Kamikadze', 'Lufi']

# a = ['shorter' if len(x) <= 4 else 'longer' for x in ls]
# print(a)



"""
9) Дан словарь, в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам. 
Замените оценки названием предмета, по которому студент имеет высший балл. Например: 
a = {'John': {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature': 81}, 
'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
-Результат: {'John': 'math', 'Rose': 'math', 'Kelly': 'literature'}
"""

# a = {'John': {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}

# for k,v in a.items():
#     val = max(v.values())
#     for b, c in v.items():
#         if c == val:
#             a[k] = b
# print(a)


"""
10) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. 
    Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
"""

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# new_dict = {}
# print(my_dict.items())
# for k, v in my_dict.items():
#     for kk, vv in v.items():
#         new_dict[k] = vv
# print(new_dict)

    


