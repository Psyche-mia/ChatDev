'''
This is the main file to start the 2048 game.
'''
from game_board import GameBoard
from game_ui import GameUI
from game_manager import GameManager
if __name__ == "__main__":
    game_board = GameBoard()
    game_ui = GameUI()
    game_manager = GameManager(game_board, game_ui)
    game_manager.game_loop()