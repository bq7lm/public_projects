import random
from colorama import Fore, Style  # Убедитесь, что colorama установлена

class Board:
    def __init__(self):
        self.size = 6  # Размер поля
        self.cells = [['О' for _ in range(self.size)] for _ in range(self.size)]  # Замена ячейки

    def __str__(self):
        board_str = "  | 1 | 2 | 3 | 4 | 5 | 6 |\n"  # Вывод поля
        board_str += "  " + '-' * 21 + '----' + "\n"
        for i in range(self.size):
            board_str += f"{i + 1} | "
            for j in range(self.size):
                board_str += f"{self.cells[i][j]} | "
            board_str += "\n  " + '-' * 21 + '----' + "\n"
        return board_str


class Ship:
    def __init__(self, cells, positions):
        self.cells = cells
        self.positions = positions  # Список позиций корабля
        self.hit_count = 0  # Счетчик попаданий по кораблю

    def place(self):
        for x, y in self.positions:
            if self.cells[x][y] == 'О':
                self.cells[x][y] = Fore.GREEN + '■' + Style.RESET_ALL  # Помещаем корабли на поле
            else:
                print("Клетка уже занята!")

    def hit(self, x, y):
        if self.cells[x][y] == Fore.GREEN + '■' + Style.RESET_ALL:
            # Попадание по собственному кораблю
            print("Вы промахнулись!")
            return False  # Вернем False, чтобы не учитывать это как попадание
        elif self.cells[x][y] == Fore.RED + 'X' + Style.RESET_ALL:
            # Если уже был выстрел в это место
            print("Эта клетка уже была выбрана!")
            return False
        elif self.cells[x][y] == 'О':
            self.cells[x][y] = 'T'  # Промах
            print("Промах!")
            return False
        elif self.cells[x][y] == Fore.GREEN + 'P' + Style.RESET_ALL:
            # Попадание по кораблю бота
            self.cells[x][y] = Fore.RED + 'X' + Style.RESET_ALL  # Попадание
            self.hit_count += 1  # Увеличиваем счетчик попаданий
            if self.hit_count == len(self.positions):  # Проверяем, потоплен ли корабль
                print("Корабль бота потоплен!")
                return True  # Вернем True, если корабль бота был поражен
            return True

    def is_sunk(self):
        return self.hit_count == len(self.positions)  # Проверка, потоплен ли корабль


class BotShip(Ship):
    def __init__(self, cells, positions):
        super().__init__(cells, positions)


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
    player_ship_positions = [(0, 0), (0, 1), (0, 2)]
    bot_ship_positions = [(1, 4), (1, 5)]

    player_ship = Ship(board.cells, player_ship_positions)
    player_ship.place()

    bot_ship = BotShip(board.cells, bot_ship_positions)
    bot_ship.place()

    # Помечаем корабль бота символом P
    for x, y in bot_ship_positions:
        board.cells[x][y] = Fore.GREEN + 'P' + Style.RESET_ALL

    print(board)

    bot_moves = set()  # Множество для хранения сделанных ботом ходов

    while True:
        player_y = get_coordinate('Введите номер строки (1-6): ')
        print('Вы выбрали строку:', player_y + 1)

        player_x = get_coordinate('Введите номер столбца (1-6): ')
        print('Вы выбрали столбец:', player_x + 1)

        player_hit = player_ship.hit(player_y, player_x)  # Проверяем, попал ли игрок

        # Ход бота, который выполняется всегда
        while True:
            bot_y = random.randint(0, 5)  # Ход бота
            bot_x = random.randint(0, 5)

            if (bot_y, bot_x) not in bot_moves:  # Проверяем, делал ли бот уже ход в эту клетку
                bot_moves.add((bot_y, bot_x))  # Добавляем клетку в многообразие ходов бота
                break

        print(f'Бот выбрал строку {bot_y + 1} и столбец {bot_x + 1}.')
        bot_hit = bot_ship.hit(bot_y, bot_x)  # Проверяем, попал ли бот

        # Проверка на окончание игры
        if bot_ship.is_sunk():
            print("Бот потоплен! Вы выиграли!")
            break  # Выход из игры

        if player_ship.is_sunk():
            print("Ваш корабль потоплен! Вы проиграли.")
            break  # Выход из игры

        print(board)


board = Board()
game()
