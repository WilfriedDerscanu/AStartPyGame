import Constants


class Segment:
    def __init__(self, board, position, color):
        self.position = position
        self.color = color
        self.board = board

    def draw(self):
        self.board.draw_segment(self.position, self.color)

    def move(self, direction):
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])

    def follow(self, segment):
        self.position = segment.position


class Snake:
    def __init__(self, board):
        self.board = board
        self.segments = [Segment(board, (board.height // 2, board.width // 2), Constants.HEAD_COLOR),
                         Segment(board, (board.height // 2, board.width // 2 + 1), Constants.BODY_COLOR),
                         Segment(board, (board.height // 2, board.width // 2 + 2), Constants.BODY_COLOR)]

    def update(self, direction, fruit):
        if self.segments[0].position[0] + direction[0] == fruit.position[0] \
                and self.segments[0].position[1] + direction[1] == fruit.position[1]:
            self.segments.append(Segment(self.board, (self.board.height // 2, self.board.width // 2 + 1),
                                         Constants.BODY_COLOR))
            fruit.generate()

        for i in reversed(range(1, len(self.segments))):
            self.segments[i].follow(self.segments[i - 1])
        self.segments[0].move(direction)

    def draw(self):
        for segment in self.segments:
            segment.draw()
