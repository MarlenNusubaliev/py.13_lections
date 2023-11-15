# num = int(input('Vvedite chislo: '))
# # 1
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')

# # 2
# res = 'even' if num % 2 == 0 else 'odd'
# print(res)

# # 3
# print('even' if num % 2 == 0 else 'odd')

# Ternary oprators(тернарные операторы) - это констркция которая по своему действию аналагично if/else, но при это записывается в одну строку

# <выражение если True> if <условие> else <выржеие если False>



# sentens = input('vvedite text: ')

# if sentens[-1] == '?':
#     res = 'voprositelnoe'
# else: 
#     res = 'Normalnoe'

# print(res)

# res = '?' if sentens[-1] == '?' else 'normal'
# print(res)



# ls = [55, 15, 64, 99, 45, 12]
# print(ls)


# choice = input('min/max?: ').lower().strip()

# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'incorect choice'
# print(res)
# =================================================================================================================
# Calkulate

flag = True
symbols = '0123456789' + '-' + '.'

while flag:
    print()
    num1 = input('chislo1: ')
    is_correct = True
    for x in num1:
        if x not in symbols:
            print('nepravilnoe chislo: ')
            is_correct = False
            break
    if not is_correct:
        continue


    num2 = input('chislo2: ')
    is_correct = True
    for x in num2:
        if x not in symbols:
            print('nepravilnoe chislo: ')
            is_correct = False
            break
    if not is_correct:
        continue

    num1 = (float(num1) if '.' in num1 else int(num1))
    num2 = (float(num2) if '.' in num2 else int(num2))
    # print(num1, type(num1))
    # print(num2, type(num2))

    operator = input('vvedite operaciu(+,-,*,/): ').strip()

    if operator == '+':
        print(f'res:  {num1 + num2}')
    elif operator == '-':
        print(f'res:  {num1 - num2}')
    elif operator == '*':
        print(f'res:  {num1 * num2}')
    elif operator == '/':
        print(f'res:  {num1 / num2}' if num2 != 0 else 'na 0 ne dilitsa')
    else:
        print('Nevernyi operator')

    choice = input('Hotitte prodoljit?(yes/no): ')
    if choice.lower().strip() != 'yes':
        flag = False
        print('buy')


