'''
This file contains the GameManager class responsible for managing the game flow and interaction between the GameBoard and GameUI.
'''
import pygame
class GameManager:
    def __init__(self, game_board, game_ui):
        self.game_board = game_board
        self.game_ui = game_ui
    def start_game(self):
        self.game_ui.draw_board(self.game_board.board)
        while not self.game_board.is_game_over():
            self.game_ui.update_board(self.game_board.board)
            self.game_ui.handle_input()
            self.game_board.move(self.game_ui.direction)
            self.game_board.add_new_tile()
    def game_loop(self):
        # Code to manage the game loop, including handling user input and updating the display
        pygame.init()
        self.start_game()  # Add this line to start the game
        while True:  # Change the loop to run indefinitely
            self.game_ui.update_board(self.game_board.board)
            self.game_ui.handle_input()
            self.game_board.move(self.game_ui.direction)
            self.game_board.add_new_tile()
            if self.game_board.is_game_over():  # Check for game over condition after each move
                break
        pygame.quit()