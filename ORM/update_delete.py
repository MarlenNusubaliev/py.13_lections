from models import Product, Category

# Обновление данных

# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()


# query = Product.update(price=(Product.price + Product.price * 0.5))
# # увеличиваем все товарам цену
# query.execute()

# ==============================================================================



# Удаленин данных
# удаление через запрос

# query = Product.delete().where(Product.id ==23 and Product.id ==24)
# query.execute()


# удаление через объект

# product = Product.get(id=22)
# print(product, product.title)
# product.delete_instance()


# удалить много данных

# query = Product.delete().where(Product.id >=20)
# print(query)
# query.execute()

# ============================================================================





