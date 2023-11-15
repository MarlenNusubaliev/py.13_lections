num = 200
black_ls = ['Нурсултан', 'Вероника', 'Айкена']

name = input('Введите имя: ').title()

if name in black_ls:
    print(f'{name}, ты не являешься студентом, тебе данной програмой - игрой пользоваться нельзя!".')
else:
    print('Угадай число!')
    while True:
        a = int(input('Введите число: '))

        if a == num:
            print('Ты угадал!')
            break
        elif (a >= num - 50 and a <= num - 10) or (a >= num + 10 and a <= num + 50):
            print('Ты был не совсем далек')
        elif num - 10 < a < num + 10:
            print('Ты был очень близок')
        else:
            print('Ты очень далеко')
