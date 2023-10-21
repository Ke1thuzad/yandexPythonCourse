class Cell:
    def __init__(self, status):
        self.cell_status = status

    def status(self):
        return self.cell_status


def decode_cell(code: str):
    return 8 - int(code[1]), ord(code[0]) - 65


class Checkers:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                if (i + j) % 2 and i < 3:
                    self.board[i].append(Cell('B'))
                elif (i + j) % 2 and i > 4:
                    self.board[i].append(Cell('W'))
                else:
                    self.board[i].append(Cell('X'))

    def move(self, from_cell, to_cell):
        decoded_from = decode_cell(from_cell)
        decoded_to = decode_cell(to_cell)
        from_cell = self.board[decoded_from[0]][decoded_from[1]]
        self.board[decoded_to[0]][decoded_to[1]], self.board[decoded_from[0]][decoded_from[1]] = from_cell, Cell('X')

    def get_cell(self, p):
        decoded = decode_cell(p)
        return self.board[decoded[0]][decoded[1]]