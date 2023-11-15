# 1.
# Вам дан список со словарями, сериализуйте этот список в json-строку
# import json

# ls = [{'name': 'ali', 'rating': 1},
#       {'name': 'bella', 'rating': 5}
#       ]

# with open('db.json', 'w') as file:
#     json.dump(ls, file, indent=4)


# 2.
# Вам дана json-строка, десериализуйте ее. 
# Выведите названия тех продуктов, рейтинг которых больше 4
# import json

# with open('new.json', 'r') as file:
#     data = json.load(file)
# print(data)
# print()



# for i in data:
#     if i['rating'] > 4:
#         print(i['name'])

# 3.
# Вам дан файл db.json. Десериализуйте данные с него. 
# Добавьте в каждый продукт новую пару ("description":"..."). 
# Запишите измененные данные в файл new_db.json

# import json


# with open('db.json', 'r') as file:
#     json_data = json.load(file)

# for i in json_data:
#     i['description'] = '...'

# with open('new_db.json', 'w') as file:
#     json.dump(json_data, file, indent=4)





# 4.
# Удалите из файла new-db.json продукт с id 3.
# import json

# with open('new_db.json', 'r') as file:
#     data = json.load(file)

# for i in data:
#     if i['id'] == 3:
#         data.remove(i)

# with open('new_db.json', 'w') as file:
#     json.dump(data, file, indent=4)



# 5.
# Напишите функцию, которая будет запрашивать id, title, description, price, rating и добавлять этот продукт в new_db.json



# import json
# from bs4 import BeautifulSoup
# import requests
# url = 'https://auto312.kg/'
# def parsing_data():
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     container = soup.find('div', class_ = 'dj-items-rows')
#     cars = container.find_all('div', class_ = 'item_row')
#     result = []
#     c_id = 0
#     for i in cars:
#         c_id += 1
#         title = i.find('a', class_ = 'title').text
#         price = i.find('div', class_ = 'item_price').text
#         rating = i.find('div', class_ = 'item_display').text
#         desc = i.find('div', class_ = 'item_content_in').text.strip().replace('\n', '')
#         data = {'id': int(c_id), 'title': title, 'price': price, 'rating':int(rating), 'desc':(desc)}
#         result.append(data)
#     return result
# with open('car_db.json', 'w') as file:
#     json.dump(parsing_data(), file, indent=4)

# with open('car_db.json', 'r') as f:
#     data = json.load(f)

# def add_car(id, title, description, price, rating):
#     car = {'id': id, 'title': title, 'description': description, 'price': price, 'rating': rating}
#     data.append(car)
#     with open('new_car_db.json', 'w') as file:
#         json.dump(data, file, indent=4)
    
# add_car(11111, 'OSMON', 'TOP1MIRA', 'MNOGO', 10)

# 6.
# Напишите функцию, которая будет принимать id продукта
# если такого продукта нет в new_db.json, функция выводит ошибку
# если такой продукт есть, то запрашивается id, title, description, price, rating и продукт должен обновиться в new_db.json



# 7.
# Напишите функцию, которая будет вытаскивать все продукты из new_db.json и выводить отсортированный список с продуктами по рейтингу (в порядке убывания)


# 8.
# Напишите функцию, которая принимает часть названия и выводит список из всех продуктов из new_db.json в названиях которых будет находится эта часть названия


# 9.
# Напишите функцию, которая принимает цену и выводит список из всех продуктов из new_db.json цена которых больше или равна заданной



# 10.
# Напишите функцию, которая принимает список из продуктов
# эти продукты должны будут добавиться в new_db.json
# если продукт с таким же id уже есть в new_db.json, то он не добавляется