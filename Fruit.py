import Constants
import random


class Fruit:
    def __init__(self, board, snake):
        self.board = board
        self.snake = snake
        self.position = (0, 0)
        self.generate()

    def generate(self):
        is_overlapping = True
        while is_overlapping:
            position = (random.randint(0, self.board.height - 1), random.randint(0, self.board.width - 1))
            is_overlapping = False
            for segment in self.snake.segments:
                if segment.position[0] == position[0] and segment.position[1] == position[0]:
                    is_overlapping = True
                    break
            self.position = position

    def draw(self):
        self.board.draw_segment(self.position, Constants.FRUIT_COLOR)
