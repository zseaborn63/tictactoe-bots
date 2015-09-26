import random


class RandomBot:

    def __init__(self, me, row1, row2, row3):
        self.me = me
        if self.me == "X":
            self.you = "O"
        else:
            self.you = "X"
        self.row_one = row1
        self.row_two = row2
        self.row_three = row3
        self.board = self.create_board()
        self.columns = self.get_col()
        self.diagonals = self.get_diag()
        self.corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

    def create_board(self):
        return [self.row_one, self.row_two, self.row_three]

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

    def random_choice(self):
        choice_x = random.randint(0, 2)
        choice_y = random.randint(0, 2)
        return choice_x, choice_y

    def random_space_chooser(self):
        dude = self.random_choice()
        x = dude[0]
        y = dude[1]
        while self.board[x][y] in 'XO':
            dude = self.random_choice()
            x = dude[0]
            y = dude[1]
        print("{} {}".format(x, y))
