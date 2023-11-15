# 1
# def summa_n(N):
#     total = 0
    
#     for i in range(1, N + 1):
#         total += i
    
#     return total

# while True:
#     user_input = input('Введите число: ')
    
#     if user_input.lower() == 'выход':
#         break
    
#     try:
#         N = int(user_input)
#         result = summa_n(N)
#         print(f'Я знаю, что сумма чисел от 1 до {N} равна {result}')
#     except ValueError:
#         print('введите целое число или "выход".')

# 2
# def positive():
#     print('Положительное')

# def negative():
#     print('Отрицательное')

# def test():
#     num = int(input('Введите целое число: '))
#     if num > 0:
#         positive()
#     elif num < 0:
#         negative()

# test()


# 3

# import math


# def circle_area():
#     radius = float(input('Введите радиус круга: '))

#     area = math.pi * radius ** 2
#     print(f'Площадь круга равна: {area}')



# def triangle_area():
#     a = float(input('Введите 1 сторону: '))
#     b = float(input('Введите 2 сторону: '))
#     c = float(input('Введите 3 сторону: '))

#     s = (a + b + c) / 2
#     print(f'Площадь треугольника: {s}')

# def reactingle_area():
#     hight = int(input('Высота: '))
#     width = int(input('Ширина: '))

#     area = hight * width
#     print(f'Площадь Прямоугольника: {area}')


# def user_input():
#     user = input('Выберите, Площадь круга, треугольника, Прямоугольника: ')
#     if user == 'круг':
#         return circle_area()
#     elif user == 'треугольник':
#         return triangle_area()
#     elif user == 'прямоугольник':
#         return reactingle_area()
    
# user_input()




# 4



# def rev():
#     while True:
#         a = input('Vvedite num: ')
#         if a == 0:
#             break
#         else:
#             a = a[::-1]
#         return a
    
# print(rev())








# 5

# def count_coins(one_kop, five_kop, ten_kop, fifty_kop):
#     total = one_kop + 5 * five_kop + 10 * ten_kop + 50 * fifty_kop
#     return total

# one_kop = int(input("Монет по 1 копейке: "))
# five_kop = int(input("Монет по 5 копеек: "))
# ten_kop = int(input("Монет по 10 копеек: "))
# fifty_kop = int(input("Монет по 50 копеек: "))

# total_amount = count_coins(one_kop, five_kop, ten_kop, fifty_kop)

# print(f"Всего у нас {total_amount / 100} рубля")


    
# 6
# def culc():
#     flag = True
#     symbols = '0123456789' + '-' + '.'

#     while flag:
#         print()
#         num1 = input('chislo1: ')
#         is_correct = True
#         for x in num1:
#             if x not in symbols:
#                 print('nepravilnoe chislo: ')
#                 is_correct = False
#                 break
#         if not is_correct:
#             continue


#         num2 = input('chislo2: ')
#         is_correct = True
#         for x in num2:
#             if x not in symbols:
#                 print('nepravilnoe chislo: ')
#                 is_correct = False
#                 break
#         if not is_correct:
#             continue

#         num1 = (float(num1) if '.' in num1 else int(num1))
#         num2 = (float(num2) if '.' in num2 else int(num2))
#         # print(num1, type(num1))
#         # print(num2, type(num2))

#         operator = input('vvedite operaciu(+,-,*,/): ').strip()

#         if operator == '+':
#             print(f'res:  {num1 + num2}')
#         elif operator == '-':
#             print(f'res:  {num1 - num2}')
#         elif operator == '*':
#             print(f'res:  {num1 * num2}')
#         elif operator == '/':
#             print(f'res:  {num1 / num2}' if num2 != 0 else 'na 0 ne dilitsa')
#         else:
#             print('Nevernyi operator')

#         choice = input('Hotitte prodoljit?(yes/no): ')
#         if choice.lower().strip() != 'yes':
#             flag = False
#             print('buy')

# culc()