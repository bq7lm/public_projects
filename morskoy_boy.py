class Board:
    def __init__(self):
        self.size = 6
        self.cells = [['О' for _ in range(self.size)] for _ in range(self.size)]

    def __str__(self):
        board_str = "   | 1 | 2 | 3 | 4 | 5 | 6 |\n"
        board_str += "  " + '-' * 21 + "\n"
        for i in range(self.size):
            board_str += f"{i + 1} | "
            for j in range(self.size):
                board_str += f"{self.cells[i][j]} | "
            board_str += "\n  " + '-' * 21 + "\n"
        return board_str
board = Board()
print("Текущее состояние доски:")
print(board)
