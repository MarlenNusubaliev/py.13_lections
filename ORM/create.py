import peewee
import random
from models import Category, Product


def add_category(name):
    try:
        name = name.lower().strip()
        data = Category(title=name)
        data.save()
        print(f'Сохрвнили категорю {name}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'Такя категория {name} уже существует')

# add_category('    платья    ')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Свитеры')
# add_category('Обувь')

def add_product(name, price, category_name):
    try:
        category_id = Category.get(title=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None


    if category_id:
        data = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'Сохранилм товар {name}')
    else:
        print(f'Категории {category_name} не существует')


# add_product('Zara t-shirt', 300, 'футболки')
# add_product('Polo t-shirt', 200, 'футболки')
# add_product('Suprime t-shirt', 400, 'футболки')
# add_product('Aygen 58', 100, 'платья')
# add_product('Platya 48', 1100, 'платья')
# add_product('Lewys', 100, 'джинсы')
# add_product('Nike Air Jordan', 1500, 'обувь')
# add_product('Polo', 2100, 'свитеры')
# add_product('Polo', 700, 'брюки')


# =============================================
# добавление новых данных

# add_category('cars')
# add_category('telefony')

with open('files/cars.txt', 'r') as file:
    ls = file.readlines()
    print(ls)
    for x in ls:
        name = x.strip()
        price = random.randint(5000, 200000)
        add_product(name, price, 'cars')


