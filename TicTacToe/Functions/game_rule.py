import random


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    if board[position] == " ":
        return True


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):

    position = 0

    while position not in list(range(1, 10)) or not space_check(board, position):
        position = int(input("Choose a position from [1-9]"))
        return position


def replay():

    choice = input("To play again enter 'yes'")
    return choice == "yes"
