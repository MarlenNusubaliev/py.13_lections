# 1
# def strFn():
#     lower1 = 0
#     upper1 = 0
#     a = input('Vvedite text: ')
#     for i in a:
#         if i.islower():
#             lower1 += 1
#         else:
#             upper1 += 1

#     print(f'Букв в нижнем регистре {lower1}')
#     print(f'Букв в верхнем  регистре {upper1}')

# strFn()

# 2

# def func1():
#     n = int(input('Vvedite num: '))
#     dict_ = {x: x ** 3 for x in range(1, n)}
#     print(dict_)

# func1()

# 3

# def num_range(start: int, end: int):
#     b = 0
#     for i in range(start,end + 1):
#         b += i
#     print(b)


# try:
#     num_range(int(input('start: ')),int(input('end: ')))
# except ValueError:
#     print('poka')


# 4

# def is_isogram(s):
#     s = s.lower()
#     return len(set(s)) == len(s)


# print(is_isogram("qwertyuio"))
# print(is_isogram("aba"))


# 5

# b = {}

# def return_amount(text):
#     a = text.lower().split(" ")
#     for word in a:
#         b[word] = a.count(word)



# return_amount("Money, money, money, it’s always sunny, in the richmen’s world")
# print(b)





