import random
from colorama import *
class Board:
    def __init__(self):
        self.size = 6  # Размер поля
        self.cells = [['О' for _ in range(self.size)] for _ in range(self.size)]  # Замена ячейки

    def __str__(self):
        board_str = Fore.BLUE+ "  | 1 | 2 | 3 | 4 | 5 | 6 |\n" + Style.RESET_ALL  # Вывод поля
        board_str +=Fore.BLUE + "  " + '-' * 21 + '----' + "\n" + Style.RESET_ALL
        for i in range(self.size):
            board_str += Fore.BLUE + f"{i + 1} | " + Style.RESET_ALL
            for j in range(self.size):
                board_str += self.cells[i][j] + Fore.BLUE+ " | " + Style.RESET_ALL
            board_str += Fore.BLUE + "\n  " + '-' * 21 + '----' + "\n" + Style.RESET_ALL
        return board_str
class Ship: #Корабли игрока
    def __init__(self, cells, positions):
        self.cells = cells
        self.positions = positions  # Список позиций корабля
        self.hit_count = 0  # Счетчик попаданий по кораблю
    def place(self):
        for x, y in self.positions:
            if self.cells[x][y] == 'О':
                self.cells[x][y] = Fore.GREEN+'■'+Style.RESET_ALL  # Помещаем корабли на поле
            else:
                print("Клетка уже занята!")
    def hit_for_bot(self, x, y):
        if self.cells[x][y] == Fore.GREEN+'■'+Style.RESET_ALL:
            self.cells[x][y] = Fore.RED+'X'+Style.RESET_ALL # Попадание
            self.hit_count += 1  # Увеличиваем счетчик попаданий
            print("Попадание!")
            if self.hit_count == len(self.positions):  # Проверяем, потоплен ли корабль
                print("Корабли потоплены!")
                return True  # Возвращаем True, если корабль потоплен
            return False
        elif self.cells[x][y] == 'О':
            self.cells[x][y] = Fore.YELLOW+'T'+Style.RESET_ALL  # Промах
            print("Промах!")
        else:
            print("Эта клетка уже была выбрана!")
        return False

class BoardBot:
    def __init__(self):
        self.size_bot = 6  # Размер поля
        self.cells_bot = [['О' for _ in range(self.size_bot)] for _ in range(self.size_bot)]  # Замена ячейки

    def __str__(self):
        board_str = Fore.BLUE+ "  | 1 | 2 | 3 | 4 | 5 | 6 |\n" + Style.RESET_ALL  # Вывод поля
        board_str +=Fore.BLUE + "  " + '-' * 21 + '----' + "\n" + Style.RESET_ALL
        for i in range(self.size_bot):
            board_str += Fore.BLUE + f"{i + 1} | " + Style.RESET_ALL
            for j in range(self.size_bot):
                board_str += self.cells_bot[i][j] + Fore.BLUE+ " | " + Style.RESET_ALL
            board_str += Fore.BLUE + "\n  " + '-' * 21 + '----' + "\n" + Style.RESET_ALL
        return board_str


board_bot = BoardBot()
board = Board()

class BotShip:
    def __init__(self, cells_bot, positions_bot):
        self.cells_bot = cells_bot
        self.positions_bot = positions_bot  # Список позиций корабля
        self.hit_count_bot = 0  # Счетчик попаданий по кораблю
    def place_for_player(self):
        for x, y in self.positions_bot:
            if self.cells_bot[x][y] == 'О':
                self.cells_bot[x][y] = 'o'  # Помещаем корабли на поле
            else:
                print("Клетка уже занята!")
    def hit_for_player(self, x, y):
        if self.cells_bot[x][y] == 'o':
            self.cells_bot[x][y] = Fore.RED+'X'+Style.RESET_ALL # Попадание
            self.hit_count_bot += 1  # Увеличиваем счетчик попаданий
            print("Попадание!")
            if self.hit_count_bot == len(self.positions_bot):  # Проверяем, потоплен ли корабль
                print("Корабли потоплены!")
                return True  # Возвращаем True, если корабль потоплен
            return False
        elif self.cells_bot[x][y] == 'О':
            self.cells_bot[x][y] = Fore.YELLOW+'T'+Style.RESET_ALL  # Промах
            print("Промах!")
        else:
            print("Эта клетка уже была выбрана!!!!")
        return False

def get_coordinate_player(prompt):
    while True:
        try:
            coordinate = int(input(prompt))
            if 1 <= coordinate <= 6:
                return coordinate - 1
            else:
                print('Ошибка! Нужно ввести число от 1 до 6.')
        except ValueError:
            print('Нужно ввести цифру от 1 до 6!')

def get_coordinate(prompt):
    while True:
        try:
            coordinate = int(input(prompt))
            if 1 <= coordinate <= 6:
                return coordinate - 1
            else:
                print('Ошибка! Нужно ввести число от 1 до 6.')
        except ValueError:
            print('Нужно ввести цифру от 1 до 6!')

def game():
    # Размещаем корабли
    ship_positions = [(0, 0), (0, 1), (0, 2), (1, 4), (1, 5), (3, 0), (3, 2), (3, 4), (4, 4), (5, 0), (5, 2)] # Позииции кораблей на поле
    ship = Ship(board.cells, ship_positions)
    ship.place()

    ship_positions_bot = [(1, 1), (1, 2), (1, 3,), (2, 4), (2, 5), (3, 1),(3, 3), (3, 5), (4, 5), (5, 1), (5, 3)]
    ship_bot = BotShip(board_bot.cells_bot, ship_positions_bot)
    ship_bot.place_for_player()

    print(board)

    bot_moves = set()  # Множество для хранения сделанных ботом ходов

    while True:
        print(board_bot)
        print('Поле Бота.')
        player_y = get_coordinate_player('Введите номер строки (1-6): ')
        print('Вы выбрали строку:', player_y + 1)

        player_x = get_coordinate_player('Введите номер столбца (1-6): ')
        print('Вы выбрали столбец:', player_x + 1)
        if ship_bot.hit_for_player(player_y, player_x):  # Проверяем, потоплен ли корабль после удара игрока
            print("Вы выиграли!")
            break  # Выход из игры

        while True:
            bot_y = random.randint(0, 5)  # Ход бота
            bot_x = random.randint(0, 5)

            if (bot_y, bot_x) not in bot_moves:  # Проверяем, делал ли бот уже ход в эту клетку
                bot_moves.add((bot_y, bot_x))  # Добавляем клетку в многообразие ходов бота
                break

        print(f'Бот выбрал строку {bot_y + 1} и столбец {bot_x + 1}.')
        if ship.hit_for_bot(bot_y, bot_x):  # Проверяем, потоплен ли корабль после удара бота
            print("Бот выиграл!")
            break  # Выход из игры
        print(board)
        print('Поле Игрока.')
game()