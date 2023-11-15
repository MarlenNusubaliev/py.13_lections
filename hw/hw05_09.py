# morze = {'A': '.-',     'B': '-...',   'C': '-.-.',
#         'D': '-..',    'E': '.',      'F': '..-.',
#         'G': '--.',    'H': '....',   'I': '..',
#         'J': '.---',   'K': '-.-',    'L': '.-..',
#         'M': '--',     'N': '-.',     'O': '---',
#         'P': '.--.',   'Q': '--.-',   'R': '.-.',
#         'S': '...',    'T': '-',      'U': '..-',
#         'V': '...-',   'W': '.--',    'X': '-..-',
#         'Y': '-.--',   'Z': '--..',

#         '0': '-----',  '1': '.----',  '2': '..---',
#         '3': '...--',  '4': '....-',  '5': '.....',
#         '6': '-....',  '7': '--...',  '8': '---..',
#         '9': '----.' 
#         }


# user = input('Vvedite text: ').upper().split()
# for w in user:
#     w2 = []
#     for i in w:
#         w2.append(morze[i])

#     print(' '.join(w2))



'''  В данном упражнении мы напишем программу, выполняющую симуляцию игры в лото с одной картой. 
Начните с генерирования списка из всех возможных номеров для выпадения (от B1 до O75). 
После этого перемешайте номера в хаотичном порядке, воспользовавшись функцией shuffle из модуля random. 
Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока карточка не окажется выигравшей. 
Проведите 1000 симуляций и выведите на экран минимальное, максимальное и среднее количество 
извлечений номеров, требующееся для выигрыша
'''

from random import shuffle

min_draws_to_win = 10000
max_draws_to_win = 0
total_draws = 0

for _ in range(1000):
    bilet = [['b7', 'b54', 'b64', 'b12', 'b13'],
            ['i5', 'i6', 'i8', 'i9', 'i10'],
            ['n11', 'n12', 'n13', 'n14', 'n15'],
            ['g16', 'g6','g29', 'g41', 'g54'],
            ['o16', 'o17', 'o36', 'o41', 'o54']]
    numbers = [f'{x}{i}' for x in 'bingo' for i in range(76)]
    shuffle(numbers)

    diagonals = [[], []]
    i = 0
    i2 = -1
    for row in bilet:
        diagonals[0].append(row[i])
        diagonals[1].append(row[i2])
        i += 1
        i2 -= 1
    print(diagonals)

    draws = 0
    win = False
    while not win:
        draws += 1    
        lot = numbers.pop()
        # проверка попадания ряд и столб
        for row in bilet:
            if lot in row:
                row[row.index(lot)] = "X"
        # проверка попадания диагонали
        for diagonal in diagonals:
            if lot in diagonal:
                diagonal[diagonal.index(lot)] = "X"

        # проверка ряда
        for row in bilet:
            if len(set(row)) == 1:
                print(bilet)
                print('BINGO')
                win = True

        # проверка столбца
        for num in range(5):
            col = [row[num] for row in bilet]
            if len(set(row)) == 1:
                print(bilet)
                print('BINGO')
                win = True
        
        # проверка диагонали
        for diagonal in diagonals:
            if len(set(diagonal)) == 1:
                print(bilet)
                print('BINGO')
                win = True

        print(bilet)
        print()
    
    min_draws_to_win = min(min_draws_to_win, draws)
    max_draws_to_win = max(max_draws_to_win, draws)
    total_draws += draws

print(f'Min draws to win: {min_draws_to_win}')
print(f'Max draws to win: {max_draws_to_win}')
print(f'Avarage draws to win in 1000 games: {total_draws / 1000}')
  