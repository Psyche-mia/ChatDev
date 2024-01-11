'''
This file contains the GameUI class responsible for handling the graphical user interface for the game.
'''
# Import pygame module
import pygame
class GameUI:
    def __init__(self):
        # Initialize the Pygame window and set up the display
        self.direction = None
        pygame.init()  # Initialize pygame
        self.screen = pygame.display.set_mode((400, 500))
        pygame.display.set_caption('2048 Game')
    def draw_board(self, board):
        # Code to draw the game board and tiles on the screen
        tile_colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }
        self.screen.fill((187, 173, 160))
        for i in range(4):
            for j in range(4):
                tile_value = board[i][j]
                color = tile_colors.get(tile_value, (205, 193, 180))
                pygame.draw.rect(self.screen, color, (j * 100, i * 100, 100, 100))
                if tile_value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(tile_value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(j * 100 + 50, i * 100 + 50))
                    self.screen.blit(text, text_rect)
        pygame.display.flip()
    def update_board(self, board):
        # Code to update the display of the game board after each move
        self.draw_board(board)
    def handle_input(self):
        # Code to handle user input for moving tiles
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.direction = 'down'
                elif event.key == pygame.K_LEFT:
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.direction = 'right'