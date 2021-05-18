import Constants
from Position import Position


class Segment:
    def __init__(self, board, position, color):
        self.position = position
        self.color = color
        self.board = board

    def draw(self):
        self.board.draw_segment(self.position, self.color)

    def move(self, direction):
        self.position = Position(self.position.x + direction.x, self.position.y + direction.y)

    def follow(self, segment):
        self.position = segment.position


class Snake:
    def __init__(self, board):
        self.board = board
        self.segments = [Segment(board, Position(board.width // 2, board.height // 2), Constants.HEAD_COLOR),
                         Segment(board, Position(board.width // 2, board.height // 2 + 1), Constants.BODY_COLOR),
                         Segment(board, Position(board.width // 2, board.height // 2 + 2), Constants.BODY_COLOR)]

    def update(self, direction, fruit):
        if self.segments[0].position.x + direction.x == fruit.position.x \
                and self.segments[0].position.y + direction.y == fruit.position.y:
            self.segments.append(Segment(self.board, Position(self.board.width // 2, self.board.height // 2 + 1),
                                         Constants.BODY_COLOR))
            fruit.generate()

        for i in reversed(range(1, len(self.segments))):
            self.segments[i].follow(self.segments[i - 1])
        self.segments[0].move(direction)

    def draw(self):
        for segment in self.segments:
            segment.draw()
