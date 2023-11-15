# Полиморфизм - способность метода(функции) использоваться в разных типах(классах)
# Широко распрастраненное определение: 'Один интнрфейс - много реализации'


# list.pop
# dict.pop
# set.pop


# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It is a cat. Cat name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Meow, meow')


# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It is a dog. Dog name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Bark, bark')


# obj1 = Cat('Garfild', 5)
# obj1.info()
# obj1.make_sound()

# obj1 = Dog('Pluto', 7)
# obj1.info()
# obj1.make_sound()
# ==============================================================================

# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name

#     def ares(self):
#         pass

#     def info(self):
#         print('Я геметрическая фигура')


# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.len = length

#     def area(self):
#         return self.len ** 2
    
#     def info(self):
#         super().info()
#         print('Все стороны равны и углы все 90 градусов')


# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.r = radius

#     def area(self):
#         from math import pi
#         return round(pi * self.r ** 2, 2)
    
#     def info(self):
#         return super().info()
#     print('Диаметр окружности равен радиусу')


# a = Square(8)
# b = Circle(4)


# a.info()
# print(a.area())

# b.info()
# print(b.area())


# =======================================================================================================


"""
1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.
"""
# писать код здесь
"""
2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:
#     def __init__(self, name) -> None:
#         self.name = name

#     def to_pet(self):
#         print(f'Dog name is {self.name}:Gaf gaf')

# class Cat:
#     def __init__(self, name) -> None:
#         self.name = name

#     def to_pet(self):
#         print(f'Cat name is {self.name}: Meow, Meow')
    

# dog = Dog('Pluti')
# cat = Cat('Tom')

# dog.to_pet()
# cat.to_pet()



"""
3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
классов переопределите метод, который отвечает за работу с оператором “+”.
Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
потом идти логика сложения 2 чисел, и выдача результата.
При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
конкатенация”, а затем логика конкатенации из базового класса и выдача результата.
"""
class MyInt(int):
    def sum(self, int1, int2):
        self.int1 = int1
        self.int2 = int2

    def add_objects(self):
        print(f'{self.int1 + self.int2}: Это сложение')



class MyString(str):
    def sum(self, int1, int2):
        self.int1 = int1
        self.int2 = int2

    def add_objects(self):
        print(f'{self.int1 + self.int2}: Это конкатенация')

intt = MyInt(5, 6)
strr = MyString('John', 'Snow')

intt.add_objects()
strr.add_objects()







"""
4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
-для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
-для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
-для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""
# писать код здесь
"""
5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем наследуйте от Shape три класса: Triangle, Square и Circle.
-треугольник создаётся с заданными основанием и высотой
-квадрат создаётся с заданной длиной стороны
-круг создаётся с заданным радиусом
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
"""


