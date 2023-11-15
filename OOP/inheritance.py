# Принципы ООП 
# 1. наследование
# 2. Инкапсуляция
# 3. Полморфизм

# 4. Абстракции
# 5.Ассоциация

# =====================================================

# ## наследование

# Позволяет принимать родительские мотоды и атрибуты дочернему классу

# Родительский класс
# Дочурний класс

# =====================================================

# class Animal:
#     def print_info(self):
#         print('I\'m an Animal')

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# simba = Lion()
# simba.print_info()
# print(dir(simba))
# =====================================================

# class Animal:
#     def say(self):
#         print(f'This animal name is: {self.name}: {self.golos}')

#     def eat(self):
#         print(f'{self.name} eats: {self.meal}')


# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'home meat'

# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalit'

# rex = Dog()
# simba = Lion()
# maris = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# print()
# maris.say()
# maris.eat()

# console--------
# This animal name is: dog: bark
# dog eats: home meat

# This animal name is: lion: roar
# lion eats: meat

# This animal name is: koala: roar
# koala eats: efkalit
# ==============================================================

# class Person:
#     def info(self):
#         print('I\'m Pain ')


# class Student(Person):
#     def info(self):
#         super().info()
#         print('I student Itodori')


# class Adult(Person):
#     def info(self):
#         super().info()

#         print('I older then  Itodori Ichigo')


# obj1 = Student()
# obj2 = Adult()

# obj1.info()
# print()
# obj2.info()
# ============================================================

# class Laptop:
#     def __init__(self, brand, model, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.price = price


#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}
    

# class Aser(Laptop):
#     def __init__(self, model, price, year, videocard):
#         super().__init__('Aser', model, price)
#         self.year = year
#         self.video = videocard

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['videocard'] = self.video
#         return repr
    
# class Apple(Laptop):
#     def __init__(self, model, price, cpu, display):
#         super().__init__('MacBook', model, price)
#         self.cpu = cpu
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['display'] = self.display
#         repr['CPU'] = self.cpu
#         return repr


# acer = Aser('swift', 700, 2022, 'nvidia')
# print(acer.get_info())

# mac = Apple('Air', 1200, 'M2', 13.6)
# print(mac.get_info())

# console
# {'brand': 'Aser', 'model': 'swift', 'price': 700, 'year': 2022, 'videocard': 'nvidia'}
# {'brand': 'MacBook', 'model': 'Air', 'price': 1200, 'display': 13.6, 'CPU': 'M2'}
# =======================================================================================================================


"""
1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
"""
# class Class1:
#     def metod1(self):
#         print('metod1')

#     def metod2(self):
#         print('metod2')

# class Class2(Class1):
#     def metod1(self):
#         super().metod1()
#         print('metod3')

#     def metod2(self):
#         super().metod2()
#         print('metod4')

# class2 = Class2()
# class2.metod1()
# class2.metod2()




"""
2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
"""

# class A:
#     def metod1(self):
#         print('Основной функционал')
    
# class B(A):
#     def method1(self):
#         super().metod1() 
#         print('Дополнительный функционал')
    
# c = B()
# c.method1()



"""
3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'
"""
# class MyString(str):
#     def __init__(self, s):
#         self.s = s

#     def append(self, strr):
#         self.s = self.s + strr
#         return self.s
    
    
    
#     def __str__(self):
#         return self.s
    
  
# example = MyString('String')
# example.append('hello')
# # example.pop()
# print(example)        
        




"""
4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
"""
# писать код здесь
"""
5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""

# class Persone:

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'{self.name}\n {self.age}'


# class Student(Persone):

#     def __init__(self, name, age, grup) -> None:
#         super().__init__(name, age)
#         self.grup = grup
#     def display_student(self):
#         return f'{self.name}\n {self.age}\n {self.grup}'




# stud = Student('John', 20, 'matematic')
# print(stud.display_student())




"""
6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
"""

# class ContactList(list):

#     def search_by_name(self, name):
#         self.name = name
#         ls = []
#         for i in self:
#             if i == name:
#                 ls.append(i)
#         return ls
    
# all_contacts = ContactList(['Aibek', 'Altai', 'Marlus', 'John', 'John', 'Oppa'])
# print(all_contacts.search_by_name('John'))

