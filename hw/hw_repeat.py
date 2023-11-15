# # 1

# import random

# def random_dect(random_fn):
#     def wrapper():
#         # print(r())
#         dict_ = {random_fn(): id(random_fn())}
#         res =  f'Функция {random_fn.__name__} была запущена успешно'
#         print(dict_)
#         return res
#     return wrapper



# @random_dect
# def random_fn():
#     return random.randint(1, 100)
    
# print(random_fn())


# 2

# def word():
#     a = input('Vvedite text: ').split()
#     res = ''.join([i[0].upper() for i in a])

#     return res

# print(word())






# 3
# def sum_dol(steps):
#     shagi = 0
#     for i in steps:
#         if i == 'U':
#             shagi += 1
#         if i == 'D':
#             shagi -= 1
#             if shagi == 0:
#                 continue
#         if shagi == 0:
#             shagi += 1
                
#     return shagi
# print(sum_dol('UDDDUDUU'))
    





