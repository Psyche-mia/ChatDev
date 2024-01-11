'''
This file contains the GameBoard class responsible for managing the game board and its state.
'''
import random
class GameBoard:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.initialize_board()
    def initialize_board(self):
        for _ in range(2):
            self.add_new_tile()
    def move(self, direction):
        if direction == 'up':
            self.move_up()
        elif direction == 'down':
            self.move_down()
        elif direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()
    def move_up(self):
        # Code to move the tiles up
        pass
    def move_down(self):
        # Code to move the tiles down
        pass
    def move_left(self):
        # Code to move the tiles left
        pass
    def move_right(self):
        # Code to move the tiles right
        pass
    def is_game_over(self):
        for row in self.board:
            if 0 in row:
                return False
            for i in range(3):
                if row[i] == row[i + 1] or row[i] == 0:
                    return False
        for i in range(4):
            for j in range(3):
                if self.board[j][i] == self.board[j + 1][i] or self.board[j][i] == 0:
                    return False
        return True
    def get_empty_cells(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        return empty_cells
    def add_new_tile(self):
        empty_cells = self.get_empty_cells()
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4