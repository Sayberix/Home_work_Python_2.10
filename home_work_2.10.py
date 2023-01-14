# 3. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

#!/usr/bin/python
 # -*- coding: utf-8 -*-

import copy
from random import choice

# вывод массива
def print_box(func_box: list) -> str:
    for i in func_box: 
        print(' '.join(list(map(str, i))))
    print('\n')

# начальное заполнение массива
def init_box(func_box: list) -> list:
    for i in range(len(func_box)):
        for j in range(len(func_box[i])): 
            func_box[i][j] = '.'
            ...
    return func_box

def dict_elements(func_box: list, number: int, symbol: str) -> list:
    match number:
        case 1:
            print_box(fill_elements(func_box,0,0,symbol))
        case 2:
            print_box(fill_elements(func_box,0,1,symbol))
        case 3:
            print_box(fill_elements(func_box,0,2,symbol))
        case 4:
            print_box(fill_elements(func_box,1,0,symbol))
        case 5:
            print_box(fill_elements(func_box,1,1,symbol))
        case 6:
            print_box(fill_elements(func_box,1,2,symbol))
        case 7:
            print_box(fill_elements(func_box,2,0,symbol))
        case 8:
            print_box(fill_elements(func_box,2,1,symbol))
        case 9:
            print_box(fill_elements(func_box,2,2,symbol))
        case _:
            print(f'неверный ввод! Повторите ввод!: ',dict_elements(func_box,int(input())))
    return func_box

def fill_elements(func_box: list, i_parametr: int, j_parametr: int, symbol: str) -> list:
    global turn_counter
    for i in range(len(func_box)):
        for j in range(len(func_box[i])):
            if i == i_parametr and j == j_parametr:
                if func_box[i][j] == ".":
                    func_box[i][j] = symbol
                    turn_counter += 1
                else:
                    n = int(input('Эта ячейка уже занята! Повторите ввод!: '))
                    dict_elements(func_box, n, symbol)
    return func_box

def check_fill_for_endgame(func_box: list, symbol: str) -> bool:
    global turn_counter
    if turn_counter >= 5:   # проверяем счетчик хода, должно быть не менее 5 ходов выполнено для проверки на окончание игры
        for i in range(len(func_box)):
            for j in range(len(func_box[i])):
                if (symbol == func_box[0][0] and symbol == func_box[0][1] and symbol == func_box[0][2]) \
                    or (symbol == func_box[0][0] and symbol == func_box[1][0] and symbol == func_box[2][0]) \
                        or (symbol == func_box[0][1] and symbol == func_box[1][1] and symbol == func_box[2][1]) \
                            or (symbol == func_box[0][2] and symbol == func_box[1][2] and symbol == func_box[2][2]) \
                                or (symbol == func_box[0][0] and symbol == func_box[1][1] and symbol == func_box[2][2]) \
                                    or (symbol == func_box[0][2] and symbol == func_box[1][1] and symbol == func_box[2][0]):
                                        ...
                                        return True
    return False
            

def check_end_game(func_box: list) -> bool:
    global turn_counter, player_1, player_2
    if turn_counter <= 9:   # Проверка на условие "ничья"
        if check_fill_for_endgame(func_box, 'X'):
            print(f"Игрок {player_1}. Победил!")
            return False
        elif check_fill_for_endgame(func_box, 'O'):
            print(f"Игрок {player_2}. Победил!")
            return False
    else:
        print("Ничья!")
        return False
    return True

def matrix_for_enter(func_box: list):
    print('Отображение матрицы "крестики-нолики". Ввод необходимо совершать по номерам ячеек: ')
    print_box(func_box)

print(' ')
mas = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
       ]

mas_work = []
mas_work = copy.deepcopy(mas)
print_box(init_box(mas_work))

print('Игра в "крестики нолики".')
print_box(mas)

player_1 = str(input('Введите имя первого игрока: '))
player_2 = str(input('Введите имя второго игрока: '))
print('Выбираем произвольно игрока, кторый будет первым ходить:')
turn_counter = 0    # счетчик ходов в игре
flag = choice([True, False]) # флаг очередности
if flag:
    print(f"Первый ходит игрок {player_1}")
    matrix_for_enter(mas)
    game_move = int(input('Введите номер ячейки (от 1 до 9): '))
    dict_elements(mas_work, game_move, 'X')
    flag = False
else:
    print(f"Первый ходит игрок {player_2}")
    matrix_for_enter(mas)
    game_move = int(input('Введите номер ячейки (от 1 до 9): '))
    dict_elements(mas_work, game_move, 'O')
    flag = True
    
while check_end_game(mas_work):
    if flag:
        matrix_for_enter(mas)
        game_move = int(input(f'Ходит игрок {player_1}. Введите номер ячейки (от 1 до 9): '))
        dict_elements(mas_work, game_move, 'X')
        flag = False
    else:
        matrix_for_enter(mas)
        game_move = int(input(f'Ходит игрок {player_2}. Введите номер ячейки (от 1 до 9): '))
        dict_elements(mas_work, game_move, 'O')
        flag = True