#This is my bot, for now.....
import random


team = input()
first_row = input()
second_row = input()
third_row = input()

def random_choice():
    choice_x = random.randint(0, 2)
    choice_y = random.randint(0, 2)
    return choice_x, choice_y

grid = [first_row, second_row, third_row]

if second_row[1] not in 'XO':
    print("{} {}".format(1, 1))
else:
    dude = random_choice()
    dude_x = dude[0]
    dude_y = dude[1]
    while grid[dude_x][dude_y] in 'XO':
        dude = random_choice()
        dude_x = dude[0]
        dude_y = dude[1]
    print("{} {}".format(dude_x, dude_y))
