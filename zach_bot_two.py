import random

team = input()
first_row = input()
second_row = input()
third_row = input()

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
        self.board = self.create_board(self.row_one, self.row_two, self.row_three)

    def create_board(self, row1, row2, row3):
        return [row1, row2, row3]

    def random_choice(self):
        choice_x = random.randint(0, 2)
        choice_y = random.randint(0, 2)
        return choice_x, choice_y

    def space_chooser(self):
        dude = self.random_choice()
        x = dude[0]
        y = dude[1]
        board = self.create_board(self.row_one, self.row_two, self.row_three)
        while board[x][y] in 'XO':
            dude = self.random_choice()
        print("{} {}".format(*dude))

d = ZachBot(team, first_row, second_row, third_row)
d.space_chooser()
