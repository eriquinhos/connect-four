import board as bd
import graphics
import pygame
import sys
import math

board = bd.create_board()
game_over = False
turn = 0

pygame.init()

game_font = pygame.font.SysFont('montserrat', 56)

graphics.draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            pygame.draw.rect(graphics.SCREEN, graphics.BLACK, (0, 0, graphics.WIDTH, graphics.SQUARE_SIZE))
            if turn == 0:
                pygame.draw.circle(graphics.SCREEN, graphics.PINK,
                                   (posx, int(graphics.SQUARE_SIZE/2)), graphics.RADIUS)
            else:
                pygame.draw.circle(graphics.SCREEN, graphics.PURPLE,
                                   (posx, int(graphics.SQUARE_SIZE / 2)), graphics.RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]

            posy = int(math.floor(posx / graphics.SQUARE_SIZE))

            if bd.is_valid_location(board, posy):
                row = bd.get_net_open_row(board, posy)
                bd.drop_pieces(board, row, posy, turn + 1)

                if bd.winning_move(board, turn + 1):
                    label = game_font.render(f"Player {turn + 1} wins!!", 1, (255, 0, 0))
                    graphics.SCREEN.blit(label, (40, 10))
                    game_over = True

            graphics.draw_board(board)
            # bd.print_board(board)
            turn = (turn + 1) % 2

            if game_over:
                pygame.time.wait(2000)

pygame.quit()
bd.print_board(board)
