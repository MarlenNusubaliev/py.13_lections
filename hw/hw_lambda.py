'''
1) Умножение соответствующих элементов двух списков: Используйте map и lambda, чтобы умножить 
соответствующие элементы двух списков.
'''

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# res = list(map(lambda x, y: x * y, a, b))
# print(res)

'''
2) Проверка, что в строке есть хотя бы одна гласная буква: Используйте any и lambda, чтобы проверить, 
что в строке есть хотя бы одна гласная буква.

'''
# text = 'Jhn Snw Kng f Nrth'

# res = any(map(lambda x: x in 'a,e,i,o,u,y', text))
# print(res)

'''
3) Фильтрация слов с определенной длиной: Используйте filter и lambda для фильтрации слов в списке 
строк, имеющих заданную длину.
'''

# names = ['Raychel', 'Sandy', 'Bob', 'Kira']
# res = list(filter(lambda x: len(x) > 5, names ))
# print(res)

'''
4) Проверка, что все элементы списка больше нуля: Используйте all и map, чтобы проверить, 
что все элементы в списке больше нуля.
'''

# ls = [1,2,3,4,5]
# res = all(map(lambda x: x > 0, ls))
# print(res)

'''
Сумма квадратов четных чисел: Напишите программу, которая с использованием map и reduce 
находит сумму квадратов четных чисел в списке.
'''
# from functools import reduce

# list_ = [1, 2, 3, 4, 5, 6]

# sum = reduce(lambda x, y: x + y, filter(lambda x: x%2==0, map(lambda x: x ** 2, list_)))
# print(sum)

