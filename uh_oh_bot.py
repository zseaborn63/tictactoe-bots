import random
from zach_bot_two import RandomBot


class SpiritBot(RandomBot):

    def is_board_open(self, grid):
        counter = 0
        for row in board:
            for square in row:
                if square == "_"
                    counter += 1
        if counter == 9:
            return True
        else:
            return False

    def make_move(self):
        pass
