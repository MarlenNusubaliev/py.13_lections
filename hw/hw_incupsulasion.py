'''
Ниже представлены связанные задачи. Цель: создать симуляцию университета. Обратите внимание на методы add_department и add_student. Подумайте, как решить проблему перезаписи существующих в словаре данных.

Создайте класс University. В конструкторе создайте переменную экземпляра name, куда записывается переданный аргумент university_name.
Создайте переменную класса departments, у которого значение по умолчанию -- пустой словарь
Создайте метод add_department, у которого параметр название факультета. Метод должен записать в словарь departments название факультета, а в качестве значения -- пустой список
Создайте класс Student, в конструкторе которого записывается firstname, lastname студента. Т.е. при создании экземпляра должны быть переданы имя и фамилия студента.
Создайте метод add_student с параметрами название факультета и объект студент -- экземпляр класса Student. Метод должен записать в словарь departments студента в соответствующий факультет.
Создайте экземпляр университета. Создайте нескольких студентов. Добавьте факультеты. Добавьте студентов в факультеты.

'''

# class Student:
#     def __init__(self, first_name, last_name) -> None:
#         self.name = first_name + ' ' + last_name


# class University:
#     def __init__(self, name) -> None:
#         self.university_name = name
#         self.departments = {}
    
#     def add_department(self, facultet):
#         if facultet not in self.departments:
#             self.departments[facultet] = []
    
#     def add_student(self, facultet, student):
#         if isinstance(student, Student):
#             if facultet in self.departments:
#                 self.departments[facultet].append(student.name)
#             else:
#                 raise KeyError('Такого факултета нет!')
            

# a = Student('Марлен', 'Нусубалиев')

# codify = University('Codify')
# codify.add_department('Python')
# codify.add_student('js', a)
# print(codify.departments)





