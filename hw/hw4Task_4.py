# 1
# list_a = [1, 2, 39, 5, -6, 7, 8.1, 9, 10, -43, -134, 3.14, 2.55, '«Lenovo»', '«Acer»', '«Asus»']
# list_b  = [123, -1.85, 43, -4.4, 8.16, - 5, 3.26, 21, 22, -43.97, '«Dell»', '«HP»', '«Lenovo»', '«Acer»']

# ls_c = [list_a + list_b]
# print(ls_c)

# for in ls_c:
# -------------------------------------------------------------------------------ERROR

# 2
# name = input('Введите Имя: ')
# email = input('Введите Email: ')
# password = input('Введите пароль: ')

# v1 = f'{name}, Вы успешно зарегистрировались, информация отправлена на {email}'
# v2 = '%s Вы успешно зарегистрировались, информация отправлена на %s' %(name, email)
# v3 = '{} Вы успешно зарегистрировались, информация отправлена на {}' .format(name, email)
# v4 = name + ' Вы успешно зарегистрировались, информация отправлена на ' + email

# if name[-1].isdigit():
#     print(v1)
# else:
#     print("Ошибка: Имя должно заканчиваться хотя бы одной цифрой")
# if password.isdigit():
#     print('Отличный пароль')
# else:
#     print("Ошибка: Пароль должен содержать только числа")
# if email.endswith(".kg"):
#     print('Email проверка успешна')
# else:
#     print("Ошибка: Email должен оканчиваться на '.kg'")


# 3
# word = input("Введите слово: ")

# unique_letters = set()

# for letter in word:
#     if letter.isalpha():  
#         unique_letters.add(letter)

# count_unique_letters = len(unique_letters)

# print("Кол-во уникальных букв:", count_unique_letters)