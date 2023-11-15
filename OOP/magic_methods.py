# magic methods (магические методы)
# dunder methods(double underscore) -> __init__
# служебные методы


# Магия заключается в том что эти меьоды запускаются без прямого обращения к ним определенные методы могут отвечат за определенные операторы

# class A(int):
#     def __init__(self) -> None:
#         pass

#     def func(self):
#         pass
# obj = A()
# print(dir(obj))

# ===========================================

# dunder methods сравнения

# __eq__(self, other) -> 5 == 8
#                         5.__eq__(8)
# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
# __ge__ -> >=

# __sub__(self, other) -> -
# __mul__ -> *
# __mod__ -> %
# __add__ -> +
# __div__ -> /
# __floordiv__ -> //
# __pow__ -> **

# class MyClass:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return self.string
    

#     def __add__(self, other):
#         print('add worked')
#         print(self, '***')
#         print(other, '---')
#         res = self.string + ' ' + other.string
#         return MyClass(res)

# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res, res.string)
# ========================================================================

# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, __value: str) -> bool:
#         print('gt worked')
#         print(self,'!!!!!')
#         print(__value,'*****')
#         return len(self) > len(__value)
    
# obj1 = Word('John')
# obj2 = Word('Hello world')
# print(obj1 > obj2)
# =====================================================================

# дандер методы строкового отображение объектов
# __str__ -> для отображение строки, которую будеть видет польз
# __repr__ -> строковую инфу о том как создать объект

# print(eval('6 + 6')) # 12

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'
    
#     def __repr__(self) -> str:
#         return 'Base("string")'
    
# user = Base('Hello John')
# print(user)
# a = eval(repr(user))
# print(a)
# =============================================================

# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# деструктор > __del__(self)



# class Cifra:
#     def __new__(cls, *args, **kwags):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
    
#     def __add__(self, other):
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} + {res}')
#         return Cifra(res)

# value1 = Cifra(-117)
# value2 = Cifra(54)
# value3 = Cifra(-7778)
# a = value1 + value2
# value3 + a
# ==========================================================


# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark')
        
# class Cat:
#     def sound(self):
#         print('Meow')

# class Parrot:
#     def sound(self):
#         print('Say')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Parrot])
#         instance = super().__new__(other)
#         print(f'I am {type(instance)}')
#         return instance
    
#     def __init__(self) -> None:
#         print('init was never closed')

# pet = Pet()
# pet.sound()

# ============================================================

# SINGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         print(cls)
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b = Singleton()
# c = Singleton()
# print(a)
# print(b)
# print(c)
# print(a is b)
# print(a is c)

# =======================================================================

# class A:
#     def __del__(self):
#         choice = input('Are you sure to delete(yes/no): ')
#         if choice.lower().split() == 'yes':
#             print('Deleted')
#             del self
#         else:
#             print('Operation denied')

# a = A()
# del a
# print(a)


# del a



# =======================================================================================================================


"""
1. Создайте класс Account и переопределите в нем методы init, repr, str и del.
Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
Метод init должен возвращать сообщение о создании счета, repr только имя держателя счета
и баланс, а str сообщение с приветствием и также информацией о держателе счета, 
балансе и филиале банка в котором зарегистрирован клиент, del в свою очередь сообщение об удаление 
и слово "Пока!"
"""
# class Account:
#     def __init__(self, name, balance, city) -> None:
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('Ваш счет открыт!')
        
#     def __repr__(self) -> str:
#         return f'Имя: {self.name}, Баланс: {self.balance}'
        
#     def __str__(self) -> str:
#         return f'Приветствую {self.name}, на вашем счету: {self.balance}, в банке СтройКапКатКотБанк'
        
#     def __del__(self):
#         return f'{self.name} Ваш счет удален. Сибастинос!'
    
# a = Account('John', 4555555, 'Kanoha')
# print(a.__repr__())
# print(a.__str__())
# print(a.__del__())


"""
2. Определите класс MyNumber который наследуется от класса int. 
У экземпляра класса должен быть обязательный атрибут value. 
Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
"""
# class MyNumber(int):
#     def __init__(self, value) -> None:
#         self.value = value
    
#     def __add__(self, __value: int) -> int:
#         self.__value = __value
#         return f'Это сложение и Ваш результат равен: {self.value + self.__value}'
#     def __sub__(self, __value: int) -> int:
#         return f'Это вычитание и Ваш результат равен: {self.value - self.__value}'
#     def __mul__(self, __value: int) -> int:
#         return f'Это умножене и Ваш результат равен: {self.value * self.__value}'
#     def __truediv__(self, __value: int) -> tuple[int, int]:
#         return f'Это деление и Ваш результат равен: {self.value / self.__value}'

    
# num = MyNumber(10)
# print(num + 5)
# print(num - 5)
# print(num * 5)
# print(num / 5)






"""
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""
# class MyList(list):
#     def __init__(self, num):
#         self.num = num

#     def __getitem__(self, key):
#         if key > 0:
#             return self.num[key -1]
#         elif key < 0:
#             return self.num[key]
#         else:
#             raise IndexError
        
# x = MyList([1,2,3,4,5])
# print(x[-1])


"""
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""
# class Student:
#     def __init__(self, name, last_name, clas, ocenki:{'math': 100, 'history': 89, 'literature': 88}) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.clas = clas
#         self.ocenki = ocenki

#     def 


        
        


"""
5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""

# class Word:


#     def __new__(cls):
#         res = cls.__delattr__(' ')

#     def __init__(self, num) -> None:
#         self.num = num

#     def __gt__(self, other):
#         self.other = other
#         return len(self.num) > len(self.other)
    
#     def __lt__(self, other):
#         self.other = other
#         return self.num < self.other

    
# a = Word('dfbdb')
# print(a.__gt__('ssdmgjgj'))
# print(a.__lt__(6))
