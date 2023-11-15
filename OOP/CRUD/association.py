# Ассоциация - означает что внутри одного объекта будет существовать другой объект в качестве аргумента
# 1. Композиция - сильная связь 
# 2. Агрегация - слабая связь

# Композиция - это когда стена не существует отдельно от комнаты.
# ================================================================================
# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

#     @property
#     def power(self):
#         return self._power
    

#     @power.setter
#     def power(self, value):
#         self._power = value



# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем внутри класса объекта от другого класса - композиция

# a = Iphone('Silver')
# a.battery.power = 50
# print(a.battery.power)
# a.battery.charge()
# print(a.battery.power)
# del a
# # При удалении Iphone вместе с ним удаляется батарейка


# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
#         # когда объект создается из вне класса и передается внутрь - агрегация


# battery = Battery()
# nokia = Nokia('Red', battery)
# nokia.battery.power = 50
# print(nokia.battery.power)
# nokia.battery.charge()
# print(nokia.battery.power)
# del nokia
# # при удалении объекта Nokia батарейка остается
# nokia2 = Nokia('Black', battery)
# print(nokia2.battery.power)
# nokia2.battery.charge()
# print(nokia2.battery.power)

# ===================================================================================

# from datetime import datetime, timedelta
# from time import sleep


# class Phone:
#     def __init__(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery = 100

#     @property
#     def battery(self):
#         if self.__battery < 0.5:
#             raise Exception('Телефон разряжен')
#         print(f'Уровень заряда: {self.__battery}')
#         self.__battery -= 0.5

#     @property
#     def get_info(self):
#         if self.__battery < 0.5:
#             raise Exception('Телефон разряжен')
#         print(f'OS: {self.__os}, IMEI: {self.__imei}')
#         self.__battery -= 0.5


#     def play_music(self):
#         if self.__battery < 5:
#             raise Exception('Телефон разряжен')
#         print('Слушаем Мирбека Атабекова')
#         self.__battery -= 5


#     def play_video(self):
#         if self.__battery < 10:
#             raise Exception('Недопустимый уровень заряда')
#         print('Смотрим Топлес и прокачиваем мозги')
#         self.__battery -= 7

    
#     def charge_battery(self, sec):
#         now = datetime.now  # 11:57:20
#         end = (now() + timedelta(seconds=sec)).strftime('%H:%M:%S')
#         # print(now().strftime('%H:%M:%S'))
#         # print(end)
#         while now().strftime('%H:%M:%S') != end:
#             # print(now().strftime('%H:%M:%S'))
#             sleep(1)
#             if self.__battery < 100:
#                 self.__battery += 1
#                 if self.__battery > 100:
#                     self.__battery = 100


#             print(f'Идет зарядка батареи! Ваш уровень баты :{self.__battery}')


        
        


# phone = Phone('777', 'iOS 16')
# phone.battery
# phone.battery
# phone.get_info
# phone.battery
# phone.play_music()
# phone.play_music()
# phone.battery
# phone.play_video()
# phone.battery

# phone.charge_battery(20)


'''
Создайте класс, сохраняющий каждый экземпляр в переменную класса all_contacts = [ ]. В инициализаторе класса должны быть параметры name, lastname, phone_number. Подсказка: подумайте о self.

Создайте субкласс Friend, у которого должен быть метод play_football_with_me()

Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя, и возвращать список всех совпадений. Замените all_contacts = [ ] на all_contacts = ContactList(). Создайте несколько контактов, используйте метод search_by_name.
'''

# class Peson:
#     all_contacts = []

#     def __init__(self, name, lastname, phone_number) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.phone_number = phone_number
#         self.all_contacts.append()


'''
Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type

Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’

Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’

Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’

В классе Publication создайте метод get_code_in_library() который будет возвращать первые_2_буквы_библиотеки_тип_первые_2_буквы_названия_количество_страниц_дата_без_точек

'''
class Publication:
    def __init__(self, name, date, pages, library, type) -> None:
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type = type


class Book(Publication):
    def get_book(self):
        self.type = 'book'


class Magazine(Publication):
    def get_magazine(self):
        self.type = 'magazine'


class Newspaper(Publication):
    def get_newspaper(self):
        self.type = 'newspaper'






