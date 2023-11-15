from bs4 import BeautifulSoup
import requests
import csv


url = 'https://auto312.kg/'

def parse_func():
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    all_cars = soup.find('div', class_='dj-items-rows')
    cars = all_cars.find_all('div', class_='item_row')
    # print(cars)
    result = []
    for car in cars:
        name = car.find('a', class_='title').text
        price = car.find('div', class_='item_price').text
        image = url+car.find('img').get('src')
        desc = car.find('div', class_='item_content_in').text
        data = {'name': name, 'price': price, 'image': image, 'desc':desc}
        result.append(data)


    write_to_csv(result)



def prepare_csv():
    with open('file_p.csv','w') as file:
        fieldnames = ['№', 'name', 'price', 'image', 'desc']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'price': 'Price:',
            'image': 'Image Url:',
            'desc': 'Desc'
        })


count = 1


def write_to_csv(data: list):
    with open('file_p.csv', 'a') as file:
        global count
        fieldnames = ['№', 'name', 'price', 'image', 'desc']
        writer = csv.DictWriter(file, fieldnames)
        for car in data:
            writer.writerow({
                '№': count,
                'name': car['name'],
                'price': car['price'],
                'image': car['image'],
                'desc': car['desc']
            })
            count += 1

prepare_csv()

parse_func()
