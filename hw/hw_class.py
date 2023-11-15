
'''
Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .

Добавьте атрибут horsepower, который равен 85.

Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.
'''



# class Car:
#     def __init__(self, brand, year, color) -> None:
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85

#     def get_auto(self):
#         return f'Марка: {self.brand}, {self.year} года, Цвет: {self.color}'
    
#     def get_year(self, this_y) -> int:
#         return f'Этой малышке {this_y - int(self.year)} год'
    
#     def add_horsepower(self):
#         if self.brand in ['Mers', 'Bmw', 'Poshe']:
#             self.horsepower += 40
#         else:
#             self.horsepower += 20
#         return f'{self.horsepower} л/c'
        



# bmw = Car('Mers', '1999', 'Red')
# poshe = Car('Poshe', '2022', 'Purpur')
# toyota = Car('Toyota', '1985', 'Yellow')
# print(bmw.get_auto())
# print(poshe.get_auto())
# print(toyota.get_auto())
# print(bmw.get_year(2023))
# print(bmw.add_horsepower())
# print()
# print(bmw.brand)
# print(bmw.year)
# print(bmw.color)


# class Student:


#     def __init__(self, name, age, course) -> None:
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_student(self):
#         return f'Name: {self.name}, Age: {self.age}, Hobby:{self.course}'
    
#     def get_birth_year(self, n_y=2023):
#         return f'{n_y - self.age} года рождения'

# res = Student('John', 33, 'Killer')
# res2 = Student('Aktan', 21, 'Singer')

# print(res.get_student())
# print(res.get_birth_year())
# print()
# print(res2.get_student())
# print(res2.get_birth_year())
    

