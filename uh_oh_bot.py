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

    def make_move(self):
        x = self.is_board_open(self.board)
        if x == True:
            print("0 2")
        else:
            self.random_space_chooser()
