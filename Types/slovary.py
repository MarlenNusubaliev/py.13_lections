# dict() - Словарь -> упорядоченная коллекция элементов (3.7 -> ordered). Каждый элемент внутри словаря хранится в виде паря -> {ключ: значение}
    # ассоциативный массив, hash table, object(js) ==dictionary(python)

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967,
# }

# print(thisdict, type(thisdict))
# print(thisdict['brand'], thisdict['model'])
# print(thisdict['year'])

# thisdict['motor'] = 'B12 Turbo'
# print(thisdict['motor'])

# thisdict['color'] = 'Grey'
# print(thisdict)
# ---------------------------------------------------------------------------
# Методы Словарей
# print(dir(dict))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnSnow@gmail.com',
#     'role': 'admin',
#     'age': 35,

# }
# print(user_info, type(user_info))

# kluchi = user_info.keys()
# print(kluchi, type(kluchi))
# ls = list(kluchi)
# print(ls, ls[0], ls[3:])



# ls = list(user_info.values())
# print(ls, type(ls))
# print(ls, ls[0], ls[3:])



# elementy = user_info.items()
# print(user_info)
# print(elementy)

# for k, v in user_info.items():
#     print(k, v)
# ---------------------------------------------------------------------------

# изменение можно по ключу, update
# dict_ = {'name': 'Jack', 'age': 24}
# print(dict_)   #{'name': 'Jack', 'age': 24}
# dict_['name'] = 'John'
# dict_['age'] = 55
# print(dict_)   #{'name': 'John', 'age': 55}

# dict_.update({'name': 'Tirion', 'address': 'Westeros'})
# print(dict_)   #{'name': 'Tirion', 'age': 55, 'address': 'Westeros'}
# ---------------------------------------------------------------------------

# получение данных со словаря
# get
# dict_ = {1: 'pizza', 2: 'burger', 3: 'steak',}
# print(dict_[3],  '!!!')
# print(dict_.get(3)) #Favorit

# setdefault - работает также как get, но если нет такого ключа то создает новую пару из этого ключа
# dict_ = {1: 'pizza', 2: 'burger', 3: 'steak',}
# print(dict_)
# print(dict_.setdefault(5, 'Manty')) # {1: 'pizza', 2: 'burger', 3: 'steak', 5: 'Manty'}
# print(dict_)

# fromkeys
# ls = list(range(1, 100))
# print(ls)
# new_dict = dict.fromkeys('12345', 'value')
# print(new_dict)
# ---------------------------------------------------------------------------
# удаление элементов 
# pop, popitem

# pop(<key>) - удаляет пару по ключу
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('name')
# print(removed)
# print(dict_)

# popitem - удаляет и возврашает последную пару в виде tuple
# print('\n\n')
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.popitem()
# print(removed)
# print(dict_)
# ---------------------------------------------------------------------------



# exemple
# roles = {
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
#  }


# product = {
#     'id': 31,
#     'title': 'MacBook Air M1',
#     'description': 'lorem Ipsum',
#     'price': 900
# }

# users = {
#     16: {'username': 'johnsnow_12', 'password': 'bastard123', 'role': roles[1]},
#     34: {'username': 'tirion_small', 'password': 'short123', 'role': roles[3]},
#     54: {'username': 'serseya_terminator', 'password': 'termitor123', 'role': roles[2]},
# }
# print(users)
# print(product)

# username = input('Vvedite svoi username: ').lower()

# user_exists = False
# for key, dict_ in users.items():
#     if username == dict_['username']:
#         id = key
#         user_exists = True
        

# if not user_exists:
#     raise ValueError('Username Not Found')


# password = input('Vvedite svoi password: ').lower()

# if users[id] ['password'] != password:
#     raise ValueError('Password did not match')

# if users[id] ['role'] == roles[1]:
#     product['description'] = input('Vvedite novoe opisanie: ')
# else:
#     raise Exception('You do not have permition!')
# print(product)

# -------------------------------------------------------------------------------------------------------



"""
1) Создайте словарь тремя возможными способами.
"""
# d = {}
# a = dict()

"""
2) Объявите словарь, удалите один из элементов и распечатайте удалённый элемент.
"""
# dict_ = {1: 'name', 2: 'last_name', 3: 'number'}
# print(dict_)
# deleted = dict_.pop(2)
# print(deleted)

"""
3) Объявите словарь, добавьте в него новую пару - "ключ: значение" и распечатайте.
"""
# dict_ = {1: 'name', 2: 'last_name', 3: 'number'}
# dict_[4] = 'adress'
# print(dict_)

"""
4) Объявите словарь, удалите всего его элементы и распечатайте.
"""
# dict_ = {1: 'name', 2: 'last_name', 3: 'number'}
# dict_ = {}
# print(dict_)

"""
5) Дан словарь, выведите все его ключи.
"""
# dict_ = {1: 'name', 2: 'last_name', 3: 'number'}
# print(dict_.keys())

"""
6)  Объявите словарь, сделайте его копию и распечатайте 
"""
# dict_ = {1: 'name', 2: 'last_name', 3: 'number'}
# print('not copy', dict_)
# copy = dict_.copy()
# print('new copy', copy)

"""
7) Это меню вашего ресторана (ключ -- название блюда, значение -- стоимость):
• menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
• Добавьте в меню новое блюдо 'Fried Rice' и установите стоимость 150
• Вы решили, что 'Tom Yam' слишком дешевый. Установите новую цену для него: 195
• Ваш повар отвратительно готовит 'Pad Thai', поэтому хотите удалить это блюдо.
• Самостоятельно найдите оператор, который удаляет пару “ключ”:”значение”, и удалите 'Pad Thai' из меню.
• Выведите оставшиеся блюда
"""
# menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
# print(menu)
# menu['Fried Rice'] = 150
# menu['Tom Yam'] = 195
# del menu['Pad Thai']
# print(menu)

"""
😍 Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре различны. Выведите синоним для последнего слова.
Пример : {‘hello’: ‘hi’, ‘good’: ‘nice’, ‘price’: ‘cost’} --> cost
"""
# a = {'hello': 'hi', 'good': 'nice', 'price': 'cost'}
# print(a['price'])

"""
9) Создайте три словаря где будут собраны характеристики некоторых животных, затем выведите краткое описание животных.
Пример : dog = {‘name’: ‘Lucky’, ‘age’: 5, 'eyes': 'blue' } --> This is a dog. His name is Lucky. It has blue eyes. Lucky is 2 years old. 
"""
# dog = {'name': 'Lucky', 'age': 5, 'eyes': 'blue' }
# cat = {'name': 'Barsik', 'age': 2, 'eyes': 'red' }
# elefant = {'name': 'Bamby', 'age': 45, 'eyes': 'yellow' }
# print('This is a dog. His name is', dog['name'], 'It has', dog['eyes'], 'eyes. Lucky is', dog['age'], 'years old.')
# print('This is a cat. His name is', cat['name'], 'It has', cat['eyes'], 'eyes.', cat['name'], 'is', cat['age'], 'years old.')
# print('This is a elefant. His name is', elefant['name'], 'It has', elefant['eyes'], 'eyes.', elefant['name'], 'is', elefant['age'], 'years old.')

"""
10) Создайте словарь в котором будет содержаться информация о факультетах и учениках, ключом будет факультет, а значением список с несколькими учениками. 
Используйте одно имя из списка, который является значением у словаря, для выведения утверждения об этом ученике.
Пример : {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}
--> This is Franklin. He studies Civil Engineering. 
"""
# student = {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}

# a = input('s: ')
# for k, v in student.items():
#     if a in v:
#         print(f'This is {a} He studies {k}')
    







