class Grid:
    def __init__(self, length, width , player):
        self.length = length
        self.width = width
        self.board = self.intitialize_board()
        self.player = player

    def intitialize_board(self):
        board = []
        for i in range(self.length):
            row = []
            for j in range(self.width):
                row.append("_")
            board.append(row)
        return board

    