
#1
# password = input('''
# Введите пароль подходящий следующим требованиям:
# 1. Длина пароля должна быть не менее 8 символов.
# 2. Пароль должен содержать хотя бы одну заглавную букву (A-Z).
# 3. Пароль должен содержать хотя бы одну строчную букву (a-z).
# 4. Пароль должен содержать хотя бы одну цифру (0-9).
# 5. Пароль должен содержать хотя бы один специальный символ из множества:\n!@#$%^&*()_-+=<>?/
#                                         ''')
# ls = '!@#$%^&*()_-+=<>?/1234567890'
# check = {'Длина': False, 'Специальный символ': False, 'Верхний регистр': False, 'Нижний регистр': False, 'Цифра': False}

# try:
#     for c in password:
#         if len(password) >= 8:
#             check['Длина'] = True

#         if c.isupper():
#             check['Верхний регистр'] = True
        
#         if c.islower():
#             check['Нижний регистр'] = True

#         for c in ls:
#             if c in password:
#                 check['Специальный символ'] = True
#             if c in password:
#                 check['Цифра'] = True
#     raise

# except:
#     for k, v in check.items():
#         if v == False:
#             print(k, 'x')
#         else:
#             print(k, '✓')









# 2.

# ls = [0,1,2,3,4,5]

# try:
#     a = int(input('Vvedi pervyi index: '))
#     b = int(input('Vvedi vtoroi index: '))
#     print(ls[a] / ls[b])
# except IndexError:
#     print('Vy vyshli za predely spiska!')
# except ValueError:
#     print('Vvedite index!')
# except ZeroDivisionError:
#     print('Delenie na nol nelzya!')



# 3
# dict_ = {'John': 35, 'Tom': 22, 'Pain': 19}
# user = input('Vvedite name: ')
# try:
   
#     print(dict_[user])
# except KeyError:
#     print('Key is undefind')


