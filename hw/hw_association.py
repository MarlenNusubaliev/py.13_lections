'''
Создайте класс Person

Создайте метод __init__ () и определите внутри него два динамических атрибута: name и birth_year (год рождения). Свои начальные значения они получают из параметров метода __init__ ()

Создайте класс Student (студент), который наследуется от класса Person

Добавьте ему 3 динамических поля (атрибут)

Первое поле course (курс на котором он обучается) должно быть public так как такая информация как должность сотрудника она открытая и не является тайной,

Второе поле notebook (его ноутбук) должно быть экземпляром класса Notebook

Третье поле private называется payments (сумма оплат студента за курсы) и по умолчанию при создании равен пустому списку.

Создать метод do_payment, которое принимает в качестве параметра сумму платежа и добавляет его в payments

Создать метод get_all_payments, которое возвращает сумму всех платежей, сделанных студентом.

Создать метод check_pc которая проверяет ноутбук на соответствие требованиям к программированию. Минимальные требования к ноутбуку должны быть:

Оперативная память 4ГБ и более

Память 120 ГБ и более

Процессор 2 ядра и более

Если ноутбук не подходит хотя бы по одному параметру, то метод должен выдать False, если все три параметра сходятся, то True
'''
class Notebook:
    def __init__(self,ram,memery,cpu) -> None:
        self.ram = ram
        self.memery = memery
        self.cpu = cpu

    def info(self):
        return f'Ноутбук с {self.ram} ГБ оперативной памяти, {self.memery} ГБ внутренней памяти и с {self.cpu} ядрами процессора'
    
    @classmethod
    def add_notebook(cls,notebook_dict):
         return cls(notebook_dict['ram'], notebook_dict['memory'], notebook_dict['cpu'])
    
notebook_dict = {

    'ram': 12,

    'memory': 500,

    'cpu': 4

}
obj = Notebook(4, 110, 8)
# -------------------------------------------------------------------------------------------


class Person:
    def __init__(self, name, birth_year) -> None:
        self.name = name
        self.birth_year = birth_year

class Student(Person):
    def __init__(self, name, birth_year, course, notebook) -> None:
        super().__init__(name, birth_year)
        self.course = course
        self.__paymants = []
        if isinstance(notebook, Notebook):
            self.notebook = notebook

    def do_payment(self, pay):
        self.__paymants.append(pay)

    def get_all_payments(self):
        return self.__paymants 
    
    def check_pc(self):
        if self.notebook.ram >= 4 and self.notebook.memery >= 120 and self.notebook.cpu >= 2:
            return True
        else:
            return False
        

obj2 = Student('Dell', 2018, 'PPP', obj)
print(obj2.check_pc())
print(obj2.get_all_payments())
obj2.do_payment(50)
print(obj2.get_all_payments())



