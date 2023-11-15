# операторы сравнения
# условные операторы и логичекие операторы


# операторы сравнения
# <, >, ==, !=(не равно), <=, >=

# res = 5 > 3 
# print(res)
# print(5 == 10, 10 == 10, 5 != 5, 5 != 6)
# print(5 >= 5)

# str1 = 'Codify'
# str2 = 'Bootcamp'
# print(str1 > str2)
# print(str1 < str2)
# print('ABC' == 'abc')
# print('a' > 'A')

# print(ord('a'))  #<--- Аск значение
# print(ord('A'))

# str1 = 'Codify'
# str2 = 'Bootcamp'
# print(len(str1) > len(str2))
# print(len(str1) != len(str2))
# -----------------------------------------------------------------------------------------------------------

# условные операторы
# if, elif, else

# weather = 'rain'
# if  weather == 'rain':
#     print('I gonna take an umbrella')
# else: 
#     print('I gonna take sunglasses')

# print("end")

# name = input('Enter your name: ')

# if name == 'John':
#     print('My name is John Snow')
#     print('John is king of North')


# age = int(input('Enter your age: '))

# if age > 18:
#     print(f'I\'m {age} years old')


# str = input('Enter smt: ')

# if str.lower() == 'hello':
#     print('Hello it is me. \nI was wondering if avter all this years yor\'d like to meet!')

# elif str.lower() == 'john':
#     print('Welcome back John Snow')

# elif str.lower() == 'abra-kadabra':
#     print('Sim salamon kadabra')
# else:
#     print('Not found any match')


# print('Registration form: ')
# email = input('Enter your email: ')
# password = input('Enter your password: ')
# if len(password) < 8:
#     raise ValueError('Password is too short!')
# elif password.isdigit():
#     raise ValueError('Password is invalid! \nAt least need one symbol!')
# elif password.isalpha():
#     raise ValueError('Password is invalid! \nAt least need one number!')

# password2 = input('Enter your password confirmation: ')
# if password != password2:
#     raise Exception('Password did\'t match!')

# print(f'Successfully registered! Hello Mr/Mrs {email}!')


# money = 1_000_000
# status = 'premium'

# if money >=  1_000_000 and status == 'premium': 
#     print('President of our club!')
# elif money >= 1_000_000 or status == 'premium':
#     print('Ministr of our club!')
# else: 
#     print('Honorable member of ourclub!')



# text = 'Hello world! S vami Aibek'
# symbol = input('Enter the symbol: ')
# print(text)

# if symbol in text.lower():
#     print(f'Thr symbol: {symbol} exists in {text.lower().index(symbol)} index!')
# else:
#     print(f'The symbol: {symbol} not exists!')





# -------Задачи------


# 1
# num = int(input('Vvedite num: '))
# if num >= 5:
#     print('True')
# else:
#     print('False')

# 2
# text = input('Vvedite text: ')
# if len(text) >= 5:
#     print('True')
# else:
#     print('False')

# 3
# num = int(input('Vvedite chislo: '))
# if num >= 90:
#     print("Отлично ваша оценка 5")
# elif num >= 80:
#     print('Здорово ваша оценка 4')
# elif num >= 70:
#     print('Хорошо ваша оценка 3')
# elif num >= 60:
#     print('Вам стоит подучить материал')
# else: 
#     print('вы не сдали экзамен')

# 4
# num = int(input('Vvedite chislo: '))
# if num < 0:
#     print('negative')
# elif num > 0:
#     print('positive')
# elif num == 0:
#     print('Zero')

# 5
# num1 = int(input('Vash nomer 1: '))
# num2 = int(input('Vash nomer 2: '))

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# 6
# num1 = int(input('Vash nomer 1: '))
# num2 = int(input('Vash nomer 2: '))
# num3 = int(input('Vash nomer 3: '))

# if num1 < num2:
#     print('nomer 1:', num1)
# elif num2 < num3:
#     print('nomer 2:', num2)
# else:
#     print('nomer 3:', num3)

# 7
# a = 5
# b = 4
# c = 3

# if a == b == c:
#     print('3')
# elif a == b or b == c or c == a:
#     print('2')
# else:
#     print('0')

# 8
# num1, num2 = int(input('num 1: ')), int(input('num 1: '))
# res1 = num1 / num2 
# res2 = num1 % num2
# res3 = num1 // num2


# if  res1 == 0:
#     print('Частное: ', res1)
# else:

#     print('Частное: ', res3)
#     print('Остаток: ', res2)

# 9
# num = int(input('Vvedite nomer goda: '))
# if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#     print('Yes')
# else:
#     print('No')

# 10
# num = int(input('chislo: '))
# s = input('Перевести в байты или в килобайты: ')
# if s == '1':
#     print(f'{num, num * 1024}')
# elif s == '2':
#     print(f'{num, num / 1024}')