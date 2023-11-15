# OOP - object oriented programming

# целью создания было связать данные с функциями которые управляют этими данными


# класс - это описание того как должен выглядеть объект, то есть в классах мы записываем какими данными и 
# функциями будет область объект

# объект - сущность которую мы создаем от класса у каждого объекта есть собственные данные

# атрибуты - обычные переменные внутри класса

#  методы - функции внутри класса

# ====================================================================================

# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship): 
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizenship: {self.citizen}'
    
# john = Human('John', 'Snow', 'King of North', 'Northener')
# james = Human('James', 'Kirk', 'programmer', 'USA')

# print(john.show_info())
# print(james.show_info())
# john.age = 24
# james.age = 19
# john.job = 'King of Westeros'
# print()
# print(john.show_info())
# print(james.show_info())
# ----------------------------------------------------------------


# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         '''Инициализатор именно здесь создаются атрибуты объекта'''
#         # self - ссылка на объект который только что создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')
        

# rex = Dog('Rex', 'Black')
# pluto = Dog(color='brown', name='Pluto')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()
# print()

# rex.age = 2
# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False


# rex.bark()
# pluto.bark()
# aktosh.bark()
# print()

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()


# =============================================================================

# class Human:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.golod = 100

#     def walk(self):
#         print(f'{self.name} walking around')
#         self.golod += 30

#     def work(self):
#         print(f'{self.name} rabota rabotaem')
#         self.golod += 50

#     def eat(self, meal, finish=True):
#         print(f'{self.name} pokushala {meal}') 
#         self.golod -= 60 if finish else 30

#     def info(self):
#         print(f'{self.name} ------> {self.golod}')

# obj = Human('John')
# obj.info()
# obj.eat('Manty')
# obj.eat('Kuurdak', finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('Burger')
# obj.eat('Pizza', finish=False)
# obj.info()

# res console
# # John ------> 100
# # John pokushala Manty
# # John pokushala Kuurdak
# # John ------> 10
# # John walking around
# # John rabota rabotaem
# # John ------> 90
# # John pokushala Burger
# # John pokushala Pizza
# # John ------> 0

# --------------------------------------------------

# class Car:
#     def __init__(self, brand, model, color) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def show_info(self):
#         return f'{self.brand} {self.model} ---> {self.color}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} ---> {self.color}'   # FAVORITE
    
# obj = Car('Chevrolet', 'Impala', "Black")
# obj2 = Car('Kia', 'K8', "Purpur")
# obj3 = Car('Tayota', 'Crawn', "Gold")
# print(obj.show_info())
# print(obj2.show_info())
# print(obj3.show_info())
# print()
# print(obj)   # str
# print(obj2)  # str
# print(obj3)  #str
# -----------------------------------------------------

# import random



# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self, other: 'Sniper'):
#         other.health -= 20
#         print(f'Атаковал {self}, у {other} осталось {other.health}')

#     def __str__(self) -> str:
#         return f'{self.name}'
    
# sniper = Sniper('John Wick')
# sniper2 = Sniper('James Bond')
# sniper.shoot(sniper2)


# while sniper.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper.shoot(sniper2) if choice == 1 else sniper2.shoot(sniper)

# print(f'{sniper if sniper.health else sniper2} won the game')

# ==============================================================================================================

"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#     color = 'Blue'
#     pi = 3.14

#     def __init__(self, rad, color) -> None:
#         self.rad = rad
#         self.color = color

#     def sum(self):
#         print(f'{self.rad ** 2 * self.pi} \nЦвет: {self.color}')

# res = Circle(6, color='red')
# res.sum()
        



"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""
# class Song:
#     def __init__(self, song_name, autor, year) -> None:
#         self.song_name = song_name
#         self.autor = autor
#         self.year = year

#     def show_author(self):
#         print(f'Автор песни: {self.autor}')

#     def show_title(self):
#         print(f'Название песни: {self.song_name}')

#     def show_year(self):
#         print(f'Год выпуска: {self.year}')

# res = Song('Не моя','Мирбек Атабеков', '2000')
# res.show_author()
# res.show_title()
# res.show_year()


"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# class Taxi:
#     def __init__(self, name_c, price, price_km) -> None:
#         self.name_c = name_c
#         self.price = price
#         self.price_km = price_km

#     def sum(self):
#         return f'{self.name_c}: {self.price + self.price_km}'
    
#     def __str__(self) -> str:
#         return f'{self.name_c}: {self.price + self.price_km}'
    
#     def summa(self, km):
#         self.km = km
#         return f'{self.name_c}: {self.km * self.price_km + self.price}'
    
# namba = Taxi('Namba', 50, 20)
# print(namba.summa(2))

# yandex = Taxi('Yandex', 100, 50)
# print(namba.summa(10))

# jorgo = Taxi('Jorgo', 75, 20)
# print(namba.summa(5))




"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# class Book:

#     def __init__(self, name, last_name, number) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.number = number

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.number}'
    
# contact = Book('Иван', 'Петров', +996555777888)
# print(contact.get_info())




"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     zp_nal = 0.08

#     def __init__(self, zp: int, staj: int) -> None:
#         self.zp = zp
#         self.staj = staj

#     def sum_nal(self):
#         return f'{self.zp * self.staj * 12 * self.zp_nal}'

# nalog = Salary(10000, 1)
# print(nalog.sum_nal())