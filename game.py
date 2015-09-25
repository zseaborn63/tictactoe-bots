from new_bot import LogicBot


team = input()
first_row = input()
second_row = input()
third_row = input()

d = LogicBot(team, first_row, second_row, third_row)
d.random_space_chooser()
