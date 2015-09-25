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

    def get_my_occurance(self):
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

    def get_opponent_occurance(self):
        row = self.create_board()
        col = self.get_col()
        diag = self.get_diag()
        occur_matrix = []
        row_occur = [x.count(self.you) for x in row]
        occur_matrix.append(row_occur)
        col_occur = [y.count(self.you) for y in col]
        occur_matrix.append(col_occur)
        diag_occur = [z.count(self.you) for z in diag]
        occur_matrix.append(diag_occur)
        return occur_matrix

    def find_row_wins(self):
        my_win = self.get_my_occurance()
        row = my_win[0]
        for idx in range(len(row)):
            if row[idx] == 2:
                return True, idx

    def find_col_wins(self):
        my_win = self.get_my_occurance()
        col = my_win[1]
        for idx in range(len(col)):
            if col[idx] == 2:
                return True, idx

    def find_diag_wins(self):
        my_win = self.get_my_occurance()
        diag = my_win[2]
            if col[idx] == 2:
                return True

    def find_row_blocks(self):
        my_block = self.get_opponent_occurance()
        row = my_block[0]
        for idx in range(len(row)):
            if row[idx] == 2:
                return True, idx

    def find_col_blocks(self):
        my_block = self.get_opponent_occurance()
        col = my_block[1]
        if col[idx] == 2:
            return True
            else:

    def find_diag_blocks(self):
        my_block = self.get_opponent_occurance()
        diag = my_block[2]
        for idx in range(len(diag)):
            if diag[idx] == 2:
                return True

    def play_win(self):
        win_possible = self.find_wins()
        if win_possible == True:
            win = self.get_my_occurance()
            row = win[0]
            col = win[1]
            diag = win[2]
            for idx in range(len(row)):
                if row[idx] == 2:
                    win_row = self.board[idx]
                    for i in range(len(win_row)):
                        if "_" not in win_row:
                            if self.me not in win_row:
                                print("{} {}".format(idx, i))

                if col[idx] == 2:
        pass

    def play_block(self):
        pass

    def make_play(self):
        pass
