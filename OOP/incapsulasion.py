# Инкапсуляция

# 1. Языковая конструкция которая помогает связать данные с методами для их обработки и управление (связь между данными и методами которые пользуются им) (класс - капсуда)

# 2. Механизм сокрытия при помощи которого можно ограничить доступ одного компонента программы к другим компонентам


# Инкапсуляция как механизм сокрытие
# 3 уровня сокрытие данных:
    # 1. Публичный(public) - number, print_number
    #   2. Защищенный(_protected) - _number
    #   3. Приватный(_p_rivate) - __number


# class Car:
#     _country = 'Germany'
#     __motor = 'Turbo diesel'

#     def __init__(self) -> None:
#         self.marka = 'Mersedes-Benz' # public
#         self._model = 'w140' # protected
#         self.__color = 'gray' # private

# obj = Car()
# print(dir(obj))

# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)
# ===============================================


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит Вам!')
#         choice = input('Взять трубку(yes/no): ').lower().strip()
#         self._turn_on if choice == 'yes' else print('Сбросили трубку')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def _turn_on(self):
#         self.__increment_calls()
#         print('Alo')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

# phone = Phone()
# print(phone.username)
# phone.call()
# phone.call()
# phone.call()
# phone.call()
# phone.call()




