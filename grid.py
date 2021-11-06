class Grid:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.board = self.intitialize_board()

    def intitialize_board(self):
        board = []
        for i in range(self.length):
            row = []
            for j in range(self.width):
                row.append("_")
            board.append(row)
        return board

    