import random
from zach_bot_two import RandomBot


team = input()
first_row = input()
second_row = input()
third_row = input()

def LogicBot(RandomBot):

    def __init__(self, team, row1, row2, row3):
        pass

    def get_col(self):
        b = self.create_board()
        col_matrix = []
        for idx in range(len(b)):
            col = [row[idx] for row in b]
            col_matrix.append(col)
        return col_matrix

    def get_diag(self):
        d = self.create_board()
        retrun [[d[0][0], d[1][1], d[2][2]], [d[0][2], d[1][1], d[2][0]]]

    

l = LogicBot()
l.random_space_chooser(team, first_row, second_row, third_row)
