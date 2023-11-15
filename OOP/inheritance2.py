# Множественное наследование это когда класс наследуется от двух или более классов, порядок наследование определяется при помощи MRO

# class Plane:
#     def play_music(self):
#         print('Music is plaing')

#     def fly(self):
#         print('we are flying')

# class Car:
#     def play_music(self):
#         print('Music is plaing on radio')

# class Auto(Car):
    
#     def ride(self):
#         print('we are fading on the ground')


# class Boat:
#     def play_music(self):
#         print('Music is plaing on karaoke')

#     def swim(self):
#         print('we are swiming on the sea')



# class FutureAuto(Auto, Boat, Plane):
#     pass

# obj = FutureAuto()
# obj.fly()
# obj.swim()
# obj.ride()
# obj.play_music()

# =======================================================


# object
# print(object)
# print(dir(object))

# class A:
#     pass

# print(issubclass(A, object))

# ========================================================================================================


# Проблема ромба - когда поиск шел в родительский класс прежде чем искать у соседнего общего потомка. (Решена при помощи MRO)

# MRO - Method resolution Order - мехонизм для корректного поиска родителький методов . Поис идет таким образом что если у родительских классов есть предок то поиск идет в ширину, другими словами сначало у потомков а потом у общего предка


# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(First, Second):
#     pass

# obj = MyClass()
# obj.say()
# print(MyClass.mro())

# ======================================================================================

# Проблема перекреснего наследование

# class X:
#     pass

# class Y:
#     pass


# class A(X, Y):
#     pass

# class B(Y, X):
#     pass


# class MyMro(type):
#     def mro(cls):
#         return[cls, A, B, X, Y, object]





# class MyClass(A, B, meteclass=MyMro):
#     pass

# print(MyClass.mro())

# ============================================================================================================


"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()


"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""

# class RadioMixin:
#     def play_music(self, name):
#         self.name = name
#         return name
    
# class Auto:
    




"""Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""

"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""