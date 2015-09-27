# Make a function where if two opposite corners are chosen, it chooses an open corner
# Need a function for first move of O team.  Possibly a random corner, or random edge.


import random
from zach_bot_two import RandomBot


class SpiritBot(RandomBot):

    def is_board_open(self, grid):
        counter = 0
        for row in grid:
            for square in row:
                if square == "_":
                    counter += 1
        if counter == 9:
            return True
        else:
            return False

    def win_or_block_possible(self, grid, me, you):
        for idx, row in enumerate(grid):
            row_value = 0
            open_index = []
            for i, space in enumerate(row):
                if space == me:
                    row_value += 1
                if space == you:
                    row_value -= 1
                if space == "_":
                    open_index.append(i)
            if row_value == 2:
                return (idx, open_index[0])
            if row_value == -2:
                return (idx, open_index[0])

    def row_win_and_block(self):
        row_win = self.win_or_block_possible(self.board, self.me, self.you)
        if row_win:
            return (True, row_win[0], row_win[1])
        else:
            return False

    def column_win_and_block(self):
        col_win = self.win_or_block_possible(self.columns, self.me, self.you)
        if col_win:
            return (True, col_win[1], col_win[0])
        else:
            return False

    def diagonal_win_and_block(self):
        diag_win = self.win_or_block_possible(self.diagonals, self.me, self.you)
        if diag_win:
            if diag_win == (0, 2):
                return (True, 2, 2)
            if diag_win == (0, 0):
                return (True, 0, 0)
            if diag_win == (1, 0):
                return (True, 0, 2)
            if diag_win == (1, 2):
                return (True, 2, 0)
            if diag_win == (1, 1):
                return (True, 1, 1)
            if diag_win == (0, 1):
                return (True, 1, 1)
        else:
            return False

    def make_move(self):
        b = self.is_board_open(self.board)
        y = self.row_win_and_block()
        z = self.column_win_and_block()
        x = self.diagonal_win_and_block()
        if b == True:
            print("0 2")
        elif y:
            print("{} {}".format(y[1], y[2]))
        elif z:
            print("{} {}".format(z[1], z[2]))
        elif x:
            print("{} {}".format(x[1], x[2]))
        else:
            self.random_space_chooser()
