from IPython.display import clear_output

def display_board(board):
    clear_output()
    print("Current GAME Status")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

# ____________________________________________________________________

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

    return (player1_marker, player2_marker)


# ____________________________________________________________________

def user_Input():
    # Initialize Variables
    userChoice1 = ""
    userChoice2 = ""
    acceptableRange = range(1, 10)
    choiceCheck = False
    rangeCheck = False

    while True:

        userChoice1 = input("Enter a Number between (1-9) ")


        choiceCheck = userChoice1.isdigit()

        if choiceCheck == True:
            userChoice1 = int(userChoice1)
        else:
            print("Warning: Type, Not Valid")

        if userChoice1 in acceptableRange:
            rangeCheck = True
        else:
            rangeCheck = False
            print("Warning: Range, Not Valid")

        if choiceCheck == True and rangeCheck == True:
            print(f"The number entered is: {userChoice1}")
            userChoice2 = input("Enter Choice 'x' or 'o' ")
        else:
            print("Enter a numeric number between range (1-9) again")
            choiceCheck = False
            rangeCheck = False
            userChoice2 = "ND"

    return userChoice1, userChoice2

# ____________________________________________________________________

def replacement_choice(row1, row2, row3, userChoice1, userChoice2):
    ticTacLookup = {1:row1[0],2:row1[1],3:row1[2],
                    4:row2[0],5:row2[1],6:row2[2],
                    7:row3[0],8:row3[1],9:row3[2]}

    ticTacLookup[userChoice1] = userChoice2

    return row1, row2, row3

def gameON_choice():
    choice = ""

    while True:
        choice = input("Keep playing ('y' or 'n')")

        if choice == 'y':
            return True
        else:
            return False


# ____________________________________________________________________
# ____________________________________________________________________
# ____________________________________________________________________

testBoard = ["","x","o","x","o","x","o","x","o","x"]
display_board(testBoard)

(player1Marker, player2Marker) = player_select_marker()
print(f"Player 1 is {player1Marker}", f" and Player 2 is {player2Marker}")

gameStatus = True
#
while gameStatus == True:
#
#     display_information(row_1, row_2, row_3)
#
#     choice1, choice2 = user_Input()
#
#     row_1, row_2, row_3 = replacement_choice(row_1,row_2,row_3, choice1, choice2)
#
#     display_information(row_1, row_2, row_3)
#
    gameStatus = gameON_choice()