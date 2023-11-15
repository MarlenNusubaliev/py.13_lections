# 1
# players = {
#     ("Will", "Smith"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }

# a = list(players)
# for k, v in players.items():
#     print(k + v)

# 2
# num = ['sdvsvd', 15, 2, 651, 4, 5, 6, 'dvdfb', 8, 65]
# a1 = (num[0], num[1])
# a2 = (num[2], num[3])
# a3 = (num[4], num[5])
# a4 = (num[6], num[7])
# a5 = (num[8], num[9])
# print([a1, a2, a3, a4, a5])

# 2.1
# a = ['0', 'altai_a_kak_eshe?', 2, 333, 'ываываываыв', 5, 6, 7, 8, 9]
# b = []
# for i in range(0, len(a), 2):
#     d = (a[i], a[i+1])
#     b.append(d)
# print(b)



# 3
# a = "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# ls = list(a)
# print('А: ', ls.count('А'))
# print('О: ', ls.count('О'))

# 4

# while True:
#     num1 = int(input('Vvedite 1-oe chislo: '))
#     num2 = int(input('Vvedite 2-oe chislo: '))
#     znak = input('+, -, *, /, q: ')
#     if znak == '+':
#         print(num1 + num2)
#     elif znak == '-':
#         print(num1 - num2)
#     elif znak == '*':
#         print(num1 * num2)
#     elif znak == '/':
#         print(num1 / num2)
#     elif znak == 'q':
#         break
#     elif znak == '':
#         print('Нет ничего приятнее, чем знание о твоих знаниях!')
        
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания.

# 5
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83

# }

# num = int(input('Сколько песен выбрать? '))
# sum = 0

# for i in range(num):
#     time = input(f'Название {i + 1} песни: ')
#     if violator_songs.get(time):
#         sum += violator_songs.get(time)
#     else:
#         print('Нет такой песни')

# print(f'Общее время звучания песен: {sum}')



# 6
# print(''' 
#       Пример для входных данных:
#       Кыргызстан Бишкек Кант Каракол
#       Германия Берлин Лейпциг Мюнхен
#       ''')
# strany = {}
# kolvo = int(input('kolvo: '))
# for i in range(kolvo):
#     a = input('strana: ').split(' ')
#     strany[a[0]] = [a[1], a[2], a[3]]
# b = input('gorod: ')
# counter = 0
# for k, v in strany.items():
#     if b in strany[k]:
#         print(f'Город {b} расположен в стране {k}.')
#     else:
#         counter += 1
#     if counter == 2:
#         print(f'По городу {b} данных нет.')
#         break
