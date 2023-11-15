# 1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
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

# 2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

# class A:
#     def metod1(self):
#         print('Основной функционал')
    
# class B(A):
#     def method1(self):
#         super().metod1() 
#         print('Дополнительный функционал')
    
# c = B()
# c.method1()


# 3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# # example = MyString('String')
# # example.append('hello')
# # print(example) -> 'Stringhello'
# # print(example.pop()) -> 'o'
# # print(example) -> 'Stringhell'

# class MyString:
#     def init(self,str1) -> None:
#         self.str1 = str1

#     def append(self,str2):
#         self.str1 = self.str1 + str2
#         return self.str1 
#     def pop(self):
#         last_str = self.str1 [-1:]
#         self.str1 = self.str1[:-1]
#         return last_str
    
#     def str(self) -> str:
#         return self.str1
    
# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop())
# print(example) 



# 4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

# class MyDict(dict):
#     def init_subclass(cls) -> None:
#         return super().init_subclass()

#     def get(self, k):
#         k = super().get(k)
#         if k is None:
#             return 'Are you kidding?'


# a = MyDict(one=1, two=2)
# print(a.get(' '))

# 5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
# Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
# Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

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



# 6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
#
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
#

# 7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию
# должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона. 
# У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

# Создайте два дочерних класса от Smartphone - Iphone и Samsung.
# У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.
# А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.
# Создайте объекты от данных классов и примените все методы.
# """
# ===============================

# from datetime import datetime

# class Smartphone:

#     def init(self, name, color, memory, battery=0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
#     def charge(self, vel):
#         self.battery = self.battery + vel

#     def str(self) -> str:
#         return f'Названия: {self.name} память: {self.memory} батарея: {self.battery}'



# class Iphone(Smartphone):
#     def init(self, name, color, memory, battery, ios) -> None:
#         super().init(name, color, memory, battery)
#         self.ios = ios
#     def send_imessage(self):
#         return 'Привет как твои дела?\nIphone 8+'



# class Samsung(Smartphone):
#     def init(self, name, color, memory, battery, android) -> None:
#         super().init(name, color, memory, battery)
#         self.android = android
#     def show_time(self):
#         return datetime.now()


# a51 = Samsung('a51', 'red', 128, 3500, 'SnapDragon 555')
# print(a51)
# print(a51.show_time())

# iphone = Iphone('Iphone 25', 'Dark Night', '15т', 100000000, 'Nokia JBL' )
# print(iphone)



# """

# 8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.
# У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.
# Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:
# Открытие замков: Alohomora
# позволяет магу попасть в любую комнату,
# способно открыть любую закрытую замочную скважину.
# Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы
# """
# class Spell:
#     def __init__(self, name, formula) -> None:
#         self.name = name
#         self.formula = formula

#     def get_description(self):
#         return {self.name}

#     def execute(self):
#         return f'{self.formula}!!!'

#     def __str__(self) -> str:
#         return f'{self.name} - Это заклинание Помогает читать мысли Любой женщины!\n{self.formula} - Это произношение заклинания'
        


# class First(Spell):
#     def __init__(self, name, formula):
#         super().__init__(name, formula)
    
#     def get_description(self):
#         return {self.name}
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self) -> str:
#         return f'{self.name} - Первая заклинание Атомная Отрыжка!\n{self.formula} - Это произношение заклинания'

# class Second(Spell):
#     def __init__(self, name, formula):
#         super().__init__(name, formula)
    
#     def get_description(self):
#         return {self.name}
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self) -> str:
#         return f'{self.name} - Вторая заклинание Падададах!\n{self.formula} - Это произношение заклинания'

# class Third(Spell):
#     def __init__(self, name, formula):
#         super().__init__(name, formula)
    
#     def get_description(self):
#         return {self.name}
    
#     def execute(self):
#         return f'{self.formula}!!!'
    
#     def __str__(self) -> str:
#         return f'{self.name} - Третья заклинание Вечная Цукоёми!\n{self.formula} - Это произношение заклинания'
    

# a = Spell('Мыслечитатель', 'furmmultus myslis')
# print(a)
# print()
# f = First('Рыгатель', 'Rygapus')
# print(f.__str__())
# print()
# s = Second('Экспулиармус', 'BannnKai')
# print(s.__str__())
# print()
# t = Third('Пикачу', 'Rasengan')
# print(t.__str__())




# """

# 9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом
# чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.
# Создайте исключение от этого класса с сообщением:
# "ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"
# Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:
 
# Traceback (most recent call last):
#   File "inheritance.py", line 121, in <module>
#     check_letters(a)
#   File "inheritance.py", line 117, in check_letters
#     raise capitals_error
# main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ
# """

# class CustomError(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)

# b = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def fn1(s):
#     if s != s.upper():
#         raise b
    
# fn1('dkkdkdkdkdkdkdk')






# """
# 10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:
# power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
# Класс должен иметь методы:
# give_weapon - выбирает случайное оружие из списка
# give_role - выбирает случайную роль из списка, к примеру:
# ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
# give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:
# char1.give_powers('ловкость', 5)
# увеличит ловкость вашего героя.
# Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,
# дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

# """

# from random import choice
# class Character:
#     role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#     weapon_list = ['Пистолет', 'Автомат', 'Меч', 'Гранотамет', 'Граната', 'Бита', 'Танк', 'Копье', 'Снайпер', 'Лук', 'Базука - РПГ']
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     def __init__(self, name):
#         self.name = name
#     def give_weapon(self):
#         weapon = choice(self.weapon_list)
#         return weapon
#     def give_role(self):
#         role = choice(self.role_list)
#         return role
#     def give_powers(self, power, val):
#         self.power_list[power] = val



# class Elf(Character):
#     magic_skill = ['поза 69', 'Читать мысли психологи женщин', 'Регенерация после кекса', 'Управление свои достоенством', 'Управление рукой', 'читать мысль ', 'Управление огнем', 'Целительство']
#     def init(self, name):
#         super().__init__(name)
        


#     def skill_(self):
#         skill = choice(self.magic_skill)
#         return skill
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nУникальный скилл: {self.skill_()}'
    
    
# elf = Elf('lusui iz brazzersa')
# elf.give_powers('мудрость', 95)
# elf.give_powers('харизма', 55)
# elf.give_powers('интелект', 69)
# elf.give_powers('сила', 85)
# elf.give_powers('ловкость', 'какта как')
# print(elf)
# print()


# class Orc(Character):
#     location = ['красныхх фонарей', 'Мордор', 'Шир', 'Драндуил', 'Темный лес', 'Гондор', 'Мериадок', 'Вонючий носок']
#     def __init__(self, name):
#         super().__init__(name)

#     def local(self):
#         local_ = choice(self.location)
#         return local_

#     def __str__(self):
#             return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nМесто жительства: {self.local()}'
    
# orc = Orc('Halk')
# orc.give_powers('мудрость', 40)
# orc.give_powers('харизма', 90)
# orc.give_powers('интеллект', 2)
# orc.give_powers('сила', 100)
# orc.give_powers('ловкость', 5)
# print(orc)
# print()
    


# class DragonBorn(Character):
#     duty = ['Мыть посуду', 'Смотреть за детьми', 'Пылесосить', 'Жена на час', 'Боди массаж']
#     def __init__(self, name):
#         super().__init__(name)
#     def choice_duty(self):
#         duty_ = choice(self.duty)
#         return duty_
#     def __str__(self):
#         return f'Имя: {self.name}\nОружие: {self.give_weapon()}\nПрофессия: {self.give_role()}\nХарактеристика: {self.power_list}\nОбязанность: {self.choice_duty()}'

# gohan = DragonBorn('Кейран Ли')

# print(gohan)