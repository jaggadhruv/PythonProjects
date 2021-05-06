def player_select_marker():

    '''
    output = (player1Marker, player2Marker)
    '''

    marker = ""
    player1_marker = ""
    player2_marker = ""

    while marker != "x" and marker != "o":
        marker = input("Player 1: Choose option 'x' or 'o' ")

        if marker == "x":
            player1_marker = "x"
            player2_marker = "o"
        else:
            player1_marker = "o"
            player2_marker = "x"

    return player1_marker, player2_marker


def place_marker(board, marker, position):

    board[position] = marker

