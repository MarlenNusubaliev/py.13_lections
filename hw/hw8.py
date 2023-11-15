# # 1
# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, 
#           "nurlan", 1.5, 27.9]



# def get_str(a: list):
#     new_ls = []
#     for x in a:
#         if type(x) == str:
#             new_ls.append(x.title())
#     return sorted(new_ls)

# print(get_str(list_1))

# def get_int(a: int):
#     new_int = []
#     for x in a:
#         if type(x) == int:
#             new_int.append(x)
#     new_int.sort()
#     new_int.reverse()
#     return new_int


# print(get_int(list_1))

# def get_float(a: float):
#     new_int = []
#     for x in a:
#         if type(x) == float:
#             new_int.append(x)
#     # new_int.sort()
#     # new_int.reverse()
#     return sum(new_int)


# print(get_float(list_1))


# 2
# ls = ['Огурей', 'яблоко','сыр']


# def struc(a: str, b:list):
#     if a == 'Большой':
#         print('Большой сэндвич со следующими ингредиентами:', b)
#     elif a == 'Средний':
#         print('Средний сэндвич со следующими ингредиентами:', b)
#     elif a == 'Маленький':
#         print('Маленький сэндвич со следующими ингредиентами:', b)

# struc('Большой', ls)
# struc('Средний', ls)
# struc('Маленький', ls)

# 3
# def car(name: str, model: str, **kwargs):
#     z = ''
#     for k, v in kwargs.items():
#         z += ''.join(f'{k}  is {v}')
#     print(f'{name} {model}, {z}')
# car('Subaru', 'Outback', colour='blue, ', engine='V8', power = 300)


# 4
# def count_letters():
#     while True:
#         t_inp = input('Введите текст: ')

#         if t_inp == 'q':
#             break

#         num_inp = input('Какую цифру ищем? ')
#         letter_inp = input('Какую букву ищем? ')

#         num = 0
#         letter = 0
        
#         for x in t_inp:
#             if x == num_inp:
#                 num += 1
#             if x == letter_inp:
#                 letter += 1

#         print(f'Количество цифр {num_inp}: {num} \nКоличество букв {letter_inp}: {letter}')
            

# count_letters()


# 5

# dict_ = {'John': 'King.'}

# def dict_fn(a: dict):
#     i = ''
#     for k, v in a.items():
#         i += f'Работник {k}, занимает должность {v}'
#     return i[0:-1]
# print(dict_fn(dict_))



# 7

# def sumFn():
#     summa = 0

#     while True:
#         try:
#             user = int(input('Vvediye sum: '))
#             summa += user
#             print(summa)
#         except ValueError:
#             print('Ошибка, введите только числа')


# sumFn()
