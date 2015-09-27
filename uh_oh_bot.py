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

    def is_second_move(self, grid):
        counter = 0
        for row in grid:
            for square in row:
                if square == "_":
                    counter += 1
        if counter == 8:
            return True
        else:
            return False

    def bottled_chaos(self):
        edges = self.edges
        board = self.board
        for x in edges:
            if (x[0], x[1]) in board == "_":
                return (True, x[0], x[1])
            else:
                return False


    def are_opposite_corners_taken(self):
        corners = self.corners
        if corners[0] and corners[3] == self.you:
            return (True, 2, 0)
        elif corners[1] and corners[2] == self.you:
            return (True, 0, 0)
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
            elif row_value == -2:
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
        first_move = self.is_board_open(self.board)
        second_move = self.is_second_move(self.board)
        corner_move = self.are_opposite_corners_taken()
        b = self.bottled_chaos()
        y = self.row_win_and_block()
        z = self.column_win_and_block()
        x = self.diagonal_win_and_block()
        if first_move == True:
            print("2 0")
        elif second_move == True:
            if self.board[0][2] != self.you:
                print("0 2")
            else:
                print("2 2")
        elif y:
            print("{} {}".format(y[1], y[2]))
        elif z:
            print("{} {}".format(z[1], z[2]))
        elif x:
            print("{} {}".format(x[1], x[2]))
        elif corner_move:
            if (corner_move[1], corner_move[2]) == "_":
                print("{} {}".format(corner_move[1], corner_move[2]))
        elif b:
            print("{} {}".format(b[1], b[2]))
        else:
            self.random_space_chooser()
