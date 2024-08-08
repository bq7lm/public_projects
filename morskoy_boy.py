from colorama import *
import random
bot_x = 0
bot_y = 0
class Board:  # Класс вывода поля
    def __init__(self):
        self.size = 6  # Размер поля
        self.cells = [['О' for _ in range(self.size)] for _ in range(self.size)]  # Замена ячейки

    def __str__(self):
        board_str = "  | 1 | 2 | 3 | 4 | 5 | 6 |\n"
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
        self.positions = positions  # Здесь передаем список позиций

    def place(self):
        for x, y in self.positions:
            if self.cells[x][y] == 'О':
                self.cells[x][y] = '■'  # Помещаем корабль
            else:
                print("Клетка уже занята!")

    def hit(self, x, y):
        if self.cells[x][y] == '■':
            self.cells[x][y] = 'X'  # Попадание
            print("Попадание!")
        elif self.cells[x][y] == 'О':
            self.cells[x][y] = 'T'  # Промах
            print("Промах!")
        else:
            print("Эта клетка уже была выбрана!")

def game():
    # Размещаем корабль на позициях (0, 0), (0, 1) и (0, 2)
    ship_positions = [(0, 0), (0, 1), (0, 2), (1,4), (1,5,),(3,0),(3,2), (3,4), (4,4),(5,0),(5,2)]
    ship = Ship(board.cells, ship_positions)
    ship.place()
    print(board)
    bot_moves = set()  # Множество для хранения сделанных ботом ходов

    def get_coordinate(prompt):
        while True:
            try:
                coordinate = int(input(prompt))  # Пробуем преобразовать ввод в целое число
                if 1 <= coordinate <= 6:  # Проверяем, что число в диапазоне от 1 до 6
                    return coordinate - 1  # Возвращаем значение для индексации
                else:
                    print('Ошибка! Нужно ввести число от 1 до 6.')
            except ValueError:
                print('Нужно ввести цифру от 1 до 6!')

    while True:
        player_y = get_coordinate('Введите номер строки (1-6): ')
        print('Вы выбрали строку:', player_y + 1)

        player_x = get_coordinate('Введите номер столбца (1-6): ')
        print('Вы выбрали столбец:', player_x + 1)
        ship.hit(player_y, player_x)
        
        
        while True:
            bot_y = random.randint(0, 5)
            bot_x = random.randint(0, 5)

            if (bot_y, bot_x) not in bot_moves:  # Проверяем, делал ли бот уже ход в эту клетку
                bot_moves.add((bot_y, bot_x))  # Добавляем клетку в многообразие ходов бота
                break

        print(f'Бот выбрал строку {bot_y + 1} и столбец {bot_x + 1}.')
        ship.hit(bot_y, bot_x)
        print(board)
board = Board()
game()