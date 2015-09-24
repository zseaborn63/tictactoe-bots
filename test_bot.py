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

random_spot = random_choice()
random_x = random_spot[0]
random_y = random_spot[1]
while grid[random_x][random_y] in 'XO':
    random_spot = random_choice()
    random_x = random_spot[0]
    random_y = random_spot[1]
print("{} {}".format(random_x, random_y))
