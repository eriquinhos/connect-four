import pygame
import numpy as np
import board as bd

BLACK = (0, 0, 0)
TURQUOISE = (43, 189, 179)
PINK = (173, 14, 88)
PURPLE = (126, 14, 173)
SQUARE_SIZE = 60
WIDTH = bd.COL_NUMBER * SQUARE_SIZE
HEIGHT = (bd.ROW_NUMBER + 1) * SQUARE_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RADIUS = int((SQUARE_SIZE / 2) - 5)

def draw_board(board=np.zeros((bd.ROW_NUMBER, bd.COL_NUMBER))):
    for col in range(bd.COL_NUMBER):
        for row in range(bd.ROW_NUMBER):
            pygame.draw.rect(SCREEN, TURQUOISE,
                             (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(SCREEN, BLACK,
                               (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for col in range(bd.COL_NUMBER):
        for row in range(bd.ROW_NUMBER):
            if board[row][col] == 1:
                pygame.draw.circle(SCREEN, PINK,
                               (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                HEIGHT - int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(SCREEN, PURPLE,
                               (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                HEIGHT - int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()
