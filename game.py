from colorama import *
init()

board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Поле
def print_board(): # Функция вывода поля
    for i in range(3):
        print(Fore.BLUE+'----'*3 + Style.RESET_ALL)
        print(Fore.BLUE+'|'+ Style.RESET_ALL, board[ i * 3],Fore.BLUE+'|'+ Style.RESET_ALL, board[1+ i*3],Fore.BLUE+'|'+ Style.RESET_ALL, board[2+i*3],Fore.BLUE+ '|'+ Style.RESET_ALL) #Вывод поля  гранц
    print(Fore.BLUE+'----' * 3 + Style.RESET_ALL)


def check_wins(): # Проверка на победу
    win = False
    wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # Победный компбинации
    for i in wins:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]: # Проверка совпадений с переменной wins
            win = True
    return win


def player_move(move, m): # Замена X или O в клетке
    if move > 9 or move < 1 or board[move - 1] in ('X', 'O'):
        return False
    board[move - 1] = m
    return True


def game():
    print('Игра крестк нолики')
    step = 0 # Кол-во шагов сделанные игроками (до 9)
    player = (Fore.GREEN+'X'+Style.RESET_ALL) # Текущий грок (X по умолчанию)
    print_board()
    while check_wins() == False and step < 9:
        move = int(input(f'Делает ход {player} игрок, введте клетку: '))
        if player_move(move, player):
            print(f'Игрок сделал ход.')
            
            if player == (Fore.GREEN+'X'+Style.RESET_ALL):  # Смена гроков
                player = (Fore.RED+'O'+Style.RESET_ALL)
            else:
                player = (Fore.GREEN+'X'+Style.RESET_ALL)
            print_board()
            step += 1
        else:
            print('Неверный ход')
   
   
    if step >= 9:
        print('Ничья!')
    else:
        player = "O" if player == 'X' else 'X'
        print(f'Выиграл игрок {player}!')

game()