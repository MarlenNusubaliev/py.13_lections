# 1111111111111=================================================================
# from bs4 import BeautifulSoup
# import requests
# import csv



# url = 'https://www.kivano.kg/mobilnye-telefony'


# def parse_name_tel():
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, 'html.parser')
#     sex = soup.find('div', class_='list-view')
#     phones = sex.find_all('div', class_='item')
#     result = []
#     for phone in phones:
#         name = phone.find('div', class_='listbox_title').text
#         price = phone.find('div', class_='listbox_price text-center').text
#         sssylka_foto = phone.find('img').get('src')
#         data = {'name': name,'price': price, 'image': f'https://www.kivano.kg{sssylka_foto}'}
#         result.append(data)
    
#     write_to_csv(result)


# def prepare_csv():
#     with open('file.csv','w') as file:
#         fieldnames = ['№', 'name', 'price', 'image']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'image': 'Image Url:',
#         })


# count = 1


# def write_to_csv(data: list):
#     with open('file.csv', 'a') as file:
#         global count
#         fieldnames = ['№', 'name', 'price', 'image']
#         writer = csv.DictWriter(file, fieldnames)
#         for car in data:
#             writer.writerow({
#                 '№': count,
#                 'name': car['name'],
#                 'price': car['price'],
#                 'image': car['image'],
#             })
#             count += 1

# prepare_csv()

  
# parse_name_tel()






# 22222222222222====================================================================================
# from bs4 import BeautifulSoup
# import requests
# import csv


# url = 'https://auto312.kg/'

# def parse_func():
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, 'lxml')
#     all_cars = soup.find('div', class_='dj-items-rows')
#     cars = all_cars.find_all('div', class_='item_row')
#     # print(cars)
#     result = []
#     for car in cars:
#         name = car.find('a', class_='title').text
#         price = car.find('div', class_='item_price').text
#         image = url+car.find('img').get('src')
#         desc = car.find('div', class_='item_content_in').text
#         data = {'name': name, 'price': price, 'image': image, 'desc':desc}
#         result.append(data)


#     write_to_csv(result)



# def prepare_csv():
#     with open('file_p.csv','w') as file:
#         fieldnames = ['№', 'name', 'price', 'image', 'desc']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '№': '№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'image': 'Image Url:',
#             'desc': 'Desc'
#         })


# count = 1


# def write_to_csv(data: list):
#     with open('file_p.csv', 'a') as file:
#         global count
#         fieldnames = ['№', 'name', 'price', 'image', 'desc']
#         writer = csv.DictWriter(file, fieldnames)
#         for car in data:
#             writer.writerow({
#                 '№': count,
#                 'name': car['name'],
#                 'price': car['price'],
#                 'image': car['image'],
#                 'desc': car['desc']
#             })
#             count += 1

# prepare_csv()

# parse_func()
