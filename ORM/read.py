import peewee
from models import Product, Category


def get_all_categories():
    return Category.select()

def get_all_products():
    return Product.select() 


# categories = get_all_categories()
# print(dir(categories))
# print('Категории в БД')

# for x in categories:
#     print(x)
#     print(x.title.title())
#     print(x.created_at.strftime('%Y-%m-%d --->> %H:%M:%S'))

#     print()


# products = get_all_products()
# print('Категории в БД')
# sum_price = 0
# for x in products:
#     print(f'{x.title} --->> {x.price} --->> {x.category_id.title}')
#     print()
#     sum_price += x.price

# print(f'AVG price: {sum_price / len(products)}')



# products = get_all_products()
# category = int(input('Vvedite category (6-платья, 7-джинсы, 8-футболки, 9-свитер, 10-обувь): '))
# for x in products:
#     if x.category_id.category_id == category:
#         print(f'{x.title} --->> {x.price} --->> {x.category_id.title}')
        
# ==============================================================================
# ==============================================================================

# category_name = input('Vvedite title: ').lower().strip()

# try:
#     category = Category.get(title=category_name)
#     print(category, category.title)
# except peewee.DoesNotExist:
#     print('Такой категории нет')
# else:
#     for product in category.products: # related name
#         print(f'Title: {product.title}, price: {product.price}, category: {product.category_id.title}')

# ==============================================================================
# ==============================================================================







