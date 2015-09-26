from uh_oh_bot import SpiritBot


team = input()
first_row = input()
second_row = input()
third_row = input()

d = SpiritBot(team, first_row, second_row, third_row)
d.make_move()
