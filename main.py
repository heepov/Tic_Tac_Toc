import numpy as np
import pygame
import sys

pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 8
SPACE_BORDER = 30
SPACE_CROSS = 45
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 12
CROSS_WIDTH = 18

LINES_COLOR = '#0AA292'
BG_COLOR = '#14bdac'
CROSS_COLOR = '#545454'
CIRCLE_COLOR = '#F2EBD2'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINES_COLOR, (0 + SPACE_BORDER, 200), (600 - SPACE_BORDER, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINES_COLOR, (0 + SPACE_BORDER, 400), (600 - SPACE_BORDER, 400), LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen, LINES_COLOR, (200, 0 + SPACE_BORDER), (200, 600 - SPACE_BORDER), LINE_WIDTH)
    pygame.draw.line(screen, LINES_COLOR, (400, 0 + SPACE_BORDER), (400, 600 - SPACE_BORDER), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE_CROSS, row * 200 + 200 - SPACE_CROSS),
                                 (col * 200 + 200 - SPACE_CROSS, row * 200 + SPACE_CROSS), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE_CROSS, row * 200 + SPACE_CROSS),
                                 (col * 200 + 200 - SPACE_CROSS, row * 200 + 200 - SPACE_CROSS), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def if_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


draw_lines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()

    pygame.display.update()
