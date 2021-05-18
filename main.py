import sys

import pygame
import numpy
import Constants
from Board import Board
from Snake import Snake
from Fruit import Fruit
from Position import Position


def generate_mat(gen_board, gen_snake, gen_fruit):
    mat = numpy.zeros((gen_board.height, gen_board.width))
    for segment in gen_snake.segments:
        mat[segment.position.y, segment.position.x] = -1  # wall
    mat[gen_snake.segments[0].position.y, gen_snake.segments[0].position.y] = 1  # start
    mat[gen_fruit.position.y, gen_fruit.position.x] = 2  # end
    return mat


pygame.init()

screen = pygame.display.set_mode((Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH))
pygame.display.set_caption("A* PySnake")
numpy.set_printoptions(threshold=sys.maxsize)

board = Board(screen)
snake = Snake(board)
fruit = Fruit(board, snake)
clock = pygame.time.Clock()

running = True
direction = Position(0, -1)
while running:
    clock.tick(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = Position(-1, 0)
            elif event.key == pygame.K_DOWN:
                direction = Position(1, 0)
            elif event.key == pygame.K_LEFT:
                direction = Position(0, -1)
            elif event.key == pygame.K_RIGHT:
                direction = Position(0, 1)

    screen.fill((0, 0, 0))

    snake.update(direction, fruit)
    snake.draw()
    fruit.draw()

    pygame.display.update()
