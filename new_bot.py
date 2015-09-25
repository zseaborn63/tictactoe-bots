import random
from zach_bot_two import RandomBot



class LogicBot(RandomBot):

    def get_col(self):
        b = self.create_board()
        col_matrix = []
        for idx in range(len(b)):
            col = [row[idx] for row in b]
            col_matrix.append(col)
        return col_matrix

    def get_diag(self):
        d = self.create_board()
        return [[d[0][0], d[1][1], d[2][2]], [d[0][2], d[1][1], d[2][0]]]

    def get_occurance(self):
        row = self.create_board()
        col = self.get_col()
        diag = self.get_diag()
        occur_matrix = []
        row_occur = [x.count(self.me) for x in row]
        occur_matrix.append(row_occur)
        col_occur = [y.count(self.me) for y in col]
        occur_matrix.append(col_occur)
        diag_occur = [z.count(self.me) for z in diag]
        occur_matrix.append(diag_occur)
        return occur_matrix
