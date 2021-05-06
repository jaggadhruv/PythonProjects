from Functions import display_information
from Functions import player_input
from Functions import winning_game
from Functions import game_rule

print("Welcome to TIC TAC TOE")


while True:
    # Play the Game

    # Set the Game
    board = [" "]*10
    player1_marker, player2_marker = player_input.player_select_marker()

    turn = game_rule.choose_first()
    print(turn + " will play first")

    play_game = input("If you are ready to play then type - yes")

    if play_game == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            # Show board
            display_information.display_board(board)
            # Choose a position
            position = game_rule.player_choice(board)
            # Place the marker on the chosen position
            player_input.place_marker(board, player1_marker, position)
            # Check if player won
            if winning_game.win_check(board, player1_marker):
                display_information.display_board(board)
                print("Player 1 has WON the Game")
                game_on = False
            else:
                if game_rule.full_board_check(board):
                    display_information.display_board(board)
                    print("The Game ended in a TIE")
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            # Show board
            display_information.display_board(board)
            # Choose a position
            position = game_rule.player_choice(board)
            # Place the marker on the chosen position
            player_input.place_marker(board, player2_marker, position)
            # Check if player won
            if winning_game.win_check(board, player2_marker):
                display_information.display_board(board)
                print("Player 2 has WON the Game")
                game_on = False
            else:
                if game_rule.full_board_check(board):
                    display_information.display_board(board)
                    print("The Game ended in a TIE")
                    game_on = False
                else:
                    turn = "Player 1"

    if not game_rule.replay():
        break
