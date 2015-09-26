# Make a function where if two opposite corners are chosen, it chooses an open corner


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

    def win_or_block_possible(self, grid, me, you)
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
            print("{} {}".format(row_win[0], row_win[1]))
        else:
            return False

    def column_win_and_block(self):
        col_win = win_or_block_possible(self.columns, self.me, self.you)
        if col_win:
            print("{} {}".format(col_win[0], col_win[1]))
        else:
            return False

    def diagonal_win_and_block(self):
        pass

    def make_move(self):
        x = self.is_board_open(self.board)
        if x == True:
            print("0 2")
        else:
            self.random_space_chooser()
