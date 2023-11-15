# области видимости и пространство имен ()
# технология которая определяет контекст имени в рамках которого мы можем использовать

# build-int (Встроенная область видимости) -> print, len
# global - область одного файла
# enclosed - (не лок)
# local


# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a

# myFunc()
# print(a)


# a = 10 #global
# print # built-in

# def hello(): # global
#     a = 'hello' #local in
#     print(a, 'local inside in func')

# hello()
# print(a, 'global')

#
# LEGB = local enclosed global built-in
# ---->------>------>------->-------->

# ---------------------------------------------------------------

# enclosed 
# локальная пространство имен - локальная пространство, у еоторого есть 
# внутреннее(вложение) локальное пространсво


# x = 'global'
# print(x, '1') # global

# def enclosed(): # global
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3') # local

#     print(x, '2') # encloser
#     local()
#     print(x, '4') # encloser

# enclosed()
# print(x, '5') # global



# global -> позволяет изменят значение глобальной переменной
# nonlocal -> позволяет изменитьзначение не локальной (замкнутой) переменной находяс внутри  
# локальной области

# var = 0  # 1

# def increment():# LEGB
#     global var
#     var += 1 #var = var + 1
#     print(var)

# increment() #1
# increment() #2
# increment() #3
# increment() #4
# increment() #5      


# def func():
#     print('John Snow')

# a = func()
# print(a())



# ==========================
# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_steps = counter()
# c_squats = counter()
# # print(c_steps)
# print(c_steps())  #1
# print(c_steps()) #2
# print(c_steps()) #3
# print(c_steps()) #4
# print(c_steps()) #5
# print(c_squats()) #1
# print(c_squats()) #2
# print(c_steps()) #6
# print(c_steps()) #7

# =============================

# game 
# # =======================================================================
# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, walkesr):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes}\n\tбелых ходоков: {walkesr}')
#     print()

# counter_heroes = counter()
# counter_walkers = counter()

# heroes = 0
# walkers = 0

# print('Приветствую вас Король севера John Snow, в игре престолов')

# while True:
#     print('Тебе доступны след действие: ')
#     print('1=убить героя, 2-убить ходока 3-статистика, 4-выйти из игры')
#     choise = input('Введите что хотите сделать: ').strip()
#     if choise == '1':
#         heroes = counter_heroes()
#         print('Вы убили Ланистера')
#     elif choise == '2':
#         walkers = counter_walkers()
#         print('Вы убили белого ходока')
#     elif choise == '3':
#         showStats(heroes, walkers)
#     elif choise == '4':
#         print('Bye Bye')
#         break
# =========================================================================




