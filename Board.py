import Constants
import pygame


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.width = Constants.SCREEN_WIDTH // Constants.SEGMENT_SIZE
        self.height = Constants.SCREEN_HEIGHT // Constants.SEGMENT_SIZE

    def draw_segment(self, position, color):
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(position[0] * Constants.SEGMENT_SIZE,
                                     position[1] * Constants.SEGMENT_SIZE,
                                     Constants.SEGMENT_SIZE, Constants.SEGMENT_SIZE))
