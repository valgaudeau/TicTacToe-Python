# Create a Tic Tac Toe game in Python

import random

board = []
for x in range(0, 9):
    board.append(' ')


def insert_letter(letter, position):
    if letter == 'X':
        board[position - 1] = 'X'  # Remember that the array representing the board starts at 0, while the positions which can chosen by the players start at 1. Hence, [position-1].
    elif letter == 'O':
        board[position] = 'O'  # For the computer moves, we remove the -1 because the computer randomly chooses a move based on the open indexes in an array. Therefore, no need for adjusting.


def is_space_free(position):
    if board[position - 1] == ' ':  # Again, remember that the array representing the board starts at 0, while the positions which can be chosen by the players start at 1.
        return True
    elif board[position - 1] != ' ':
        return False


def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def final_result(board):
    streak = 3  # how many in a row we need to win
    D = 3  # Dimensions, which in this case are 3x3
    i = 0
    while i < (D * D):  # In this case, both dimensions are the same length.
        if (board[i] != " ") and (board[i] == board[i + 1]) and (board[i] == board[i + 2]):  # Find wins for rows
            return board[i]
        if (i % D) == (D - streak):  # This is useful if we work in higher dimensions, at the moment we move up 3 every time. Writting it with these variables makes it an easy transition.
            i = i + streak  # So we move up 3 every time. What we get here is we check if 3 in a row for index 0, 3 and 6.
        else:
            i = i + 1  # Again, only really useful for higher dimensions.
    for i in range(3):
        if (board[i] != " ") and (board[i] == board[i + 3]) and (board[i] == board[i + 6]):  # Find wins for columns
            return board[i]
    i = 0
    if (board[i] != " ") and (board[i] == board[i + 4]) and (board[i] == board[i + 8]):  # Find win for first diagonal
        return board[i]
    i = 2
    if (board[i] != " ") and (board[i] == board[i + 2]) and (board[i] == board[i + 4]):  # Find win for second diagonal
        return board[i]


def player_move():
    run = True
    while run:
        player_input = input("Please enter the position at which you want to place an X on the board (choose an integer from 1 to 9):\n")
        try:
            player_input = int(player_input)
            if 0 < player_input < 10:
                if is_space_free(player_input):
                    run = False
                    insert_letter('X', player_input)
                else:
                    print("Sorry, this move isn't possible. Please try again")
            else:
                print("Please type a number within the accepted range (1 to 9)")
        except:
            print("You can only enter a number here")

    return (final_result(board) == 'X')


def comp_move():
    # Could create an algorithm to make the computer play good moves, but in that case the human player will never win.
    # Therefore, I think it makes more sense to make the computer play random moves unless he can wi, or he has to block a win from the human player.

    move = 0
    winmove = -1
    blockmove = -1

    for i in range(3):
        temp = []
        temp.append(board[i])
        temp.append(board[i + 3])
        temp.append(board[i + 6])

        a = (temp.count(" ") == 1)
        b = (temp.count("O") == 2)
        c = (temp.count("X") == 2)

        if ((a and b) or (a and c)):  # if we have a situation where we have an empty position, and the computer has 2 'O' in that column or the player has 2 'X' in that column, computer picks it.
            x = temp.index(" ")
            move = i + x * 3  # translates position from 2 dimensional array to 1 dimensional array which represents our board
            if (b):
                winmove = move  # the situation where we complete the column and win.
                # print("winmove " + str(move + 1) + " detected vertically")  # debugging purposes here, want to see the message if we get to this condition rather than have to guess if it worked.
            if (c):
                blockmove = move  # the situation where we block the player from winning.
                # print("blockmove " + str(move + 1) + " detected vertically")

    for i in range(0, 7, 3):
        temp = []
        temp.append(board[i])
        temp.append(board[i + 1])
        temp.append(board[i + 2])

        a = (temp.count(" ") == 1)
        b = (temp.count("O") == 2)
        c = (temp.count("X") == 2)

        if ((a and b) or (a and c)):
            x = temp.index(" ")
            move = i + x  # translates position from 2 dimensional array to 1 dimensional array which represents our board
            if (b):
                winmove = move
                # print("winmove " + str(move + 1) + " detected horizontally")
            if (c):
                blockmove = move
                # print("blockmove " + str(move + 1) + " detected horizontally")

    temp = []
    temp.append(board[0])
    temp.append(board[4])
    temp.append(board[8])
    a = (temp.count(" ") == 1)
    b = (temp.count("O") == 2)
    c = (temp.count("X") == 2)

    if ((a and b) or (a and c)):
        x = temp.index(" ")
        move = x * 4
        if (b):
            winmove = move
            # print("winmove " + str(move + 1) + " detected diagonally")
        if (c):
            blockmove = move
            # print("blockmove " + str(move + 1) + " detected diagonally")

    temp = []
    temp.append(board[2])
    temp.append(board[4])
    temp.append(board[6])
    a = (temp.count(" ") == 1)
    b = (temp.count("O") == 2)
    c = (temp.count("X") == 2)

    if ((a and b) or (a and c)):
        x = temp.index(" ")
        move = 2 + x * 2
        if (b):
            winmove = move
            # print("winmove " + str(move + 1) + " detected diagonally")
        if (c):
            blockmove = move
            # print("blockmove " + str(move + 1) + " detected diagonally")

    if (winmove >= 0):
        insert_letter('O', winmove)
    elif (blockmove >= 0):
        insert_letter('O', blockmove)
    else:
        possible_moves = [x for x, letter in enumerate(board) if
                          letter == ' ']  # List comprehension & enumerate combined. This returns a list with all of the empty indexes in board.
        if len(possible_moves) > 0:
            random_move = random.choice(
                possible_moves)  # choice is a method which returns a random element from a given sequence
            insert_letter('O', random_move)
        else:
            # The reason we need this conditional to capture the option of there being 0 possible moves and 'passing' is that if we're in a draw situation where the human plays the last move,
            # our main function still has to run comp_move before going accessing the code if board_is_full is True.
            # Without this if / else statement here, we get an error as it's impossible for the choice() method to return a random element from an empty sequence.
            pass
    return (final_result(board) == 'O')


def is_board_full(board):
    return board.count(" ") == 0


def clear_board(board):
    for i in range(0, 9):
        board[i] = ' '


def main():
    print("Welcome to this Tic Tac Toe game. You are playing the crosses, and the computer is playing the circles.")
    print("To play your move, enter a number between 1 and 9. The first square is the top left corner can be accessed by typing one, and the square directly adjacent to it on the right is 2.")

    main_run = True
    while main_run:

        while True:
            print_board(board)
            if is_board_full(board):
                print("The game is a draw")
                break
            if player_move():
                print_board(board)
                print("Well done, you won this round")
                break
            if comp_move():
                print_board(board)
                print("Sorry, you lost this round")
                break

        answer = input("Would you like to play another game?(Y/N)\n")
        if answer.lower() == 'y' or answer.lower() == 'yes':
            clear_board(board)
        elif answer.lower() == 'n' or answer.lower() == 'no':
            main_run = False


main()
