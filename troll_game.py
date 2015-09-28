from zach_bot_two import RandomBot


team = input()
first_row = input()
second_row = input()
third_row = input()

d = RandomBot(team, first_row, second_row, third_row)
d.random_space_chooser()
