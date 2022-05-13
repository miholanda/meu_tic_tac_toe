'''
Your task is to write a simple program which pretends to play tic-tac-toe with the user.
 To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

the computer (i.e., your program) should play the game using 'X's;
the user (e.g., you) should play the game using 'O's;
the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
all the squares are numbered row by row starting with 1 (see the example session below for reference)
the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., 
it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
the program checks if the game is over − there are four possible verdicts: the game should continue, 
the game ends with a tie, you win, or the computer wins;
the computer responds with its move and the check is repeated;
don't implement any form of artificial intelligence − a random field choice made by 
the computer is good enough for the game.
The example session with the program may look as follows:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!

Requirements
Implement the following features:

the board should be stored as a three-element list, while each element 
is another three-element list (the inner lists represent rows) so that all 
of the squares may be accessed using the following syntax:

board[row][column]

each of the inner list's elements can contain 'O', 'X', or a digit representing the 
square's number (such a square is considered free)
the board's appearance should be exactly the same as the one presented in the example.
implement the functions defined for you in the editor.

Drawing a random integer number can be done by utilizing a Python function called randrange(). 
The example program below shows how to use it (the program prints ten random numbers from 0 to 8).

Note: the from-import instruction provides access to the randrange function defined 
within an external Python module callled random.

from random import randrange

for i in range(10):
    print(randrange(8))
'''
from random import randrange

def display_board(board):
    for space in board:
        print(space)
    return board

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global computer_move
    while True:
        found = False
        display_board(board)
        print("\n")
        move = int(input("What's your move? Enter number and press enter, please. \n"))
        if move < 0 or move > 9:
            print("Out of range. Retry. \n")
            pass
        else:
            for x in range(3):
                for y in range(3):
                    if move == board[x][y]:
                        temp_show = board[x][y]
                        board[x][y] = 'O'
                        print(f'Position found. Replaced {temp_show} succesfully. \n')
                        display_board(board)
                        computer_move = True
                        found = True
                        print(f'User move completed. Back to menu - computer move status = {computer_move}')
                        print("\n")
                        return board, computer_move
        if found == True:
            break
        else:
            print("Position not found. Occupied? \n")
    return board, computer_move

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_fields
    free_fields = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'X' or board[x][y] == 'O':
                #print(f'Position occupied. \n')
                pass
            else:
                temp_tuple = (x,y)
                #print(f'Free position - row {x} and column {y}')
                free_fields.append(temp_tuple)
                #print("Current list of free fields: ", free_fields)
    print('')
    print(free_fields)
    return True

def victory_for(board):
    global game_status
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    victory_user = False
    victory_computer = False
    for x in range(3):
        for y in range(3):
            #horizontais
            if board[0][0] == board[0][1] == board[0][2]:
                if board[0][0] == 'X':
                    victory_computer = True
                elif board[0][0] == 'O':
                    victory_user = True
                else:
                    pass
            elif board[1][0] == board[1][1] == board[1][2]:
                if board[1][0] == 'X':
                    victory_computer = True
                elif board[1][0] == 'O':
                    victory_user = True
                else:
                    pass
            elif board[2][0] == board[2][1] == board[2][2]:
                if board[2][0] == 'X':
                    victory_computer = True
                elif board[2][0] == 'O':
                    victory_user = True
                else:
                    pass
            #vertical
            if board[0][0] == board[1][0] == board[2][0]:
                if board[0][0] == 'X':
                    victory_computer = True
                elif board[0][0] == 'O':
                    victory_user = True
                else:
                    pass
            elif board[1][0] == board[1][1] == board[1][2]:
                if board[1][0] == 'X':
                    victory_computer = True
                elif board[1][0] == 'O':
                    victory_user = True
                else:
                    pass
            elif board[0][2] == board[1][2] == board[2][2]:
                if board[0][2] == 'X':
                    victory_computer = True
                elif board[0][2] == 'O':
                    victory_user = True
                else:
                    pass
            #diagonal
            if board[0][0] == board[1][1] == board[2][2]:
                if board[0][0] == 'X':
                    victory_computer = True
                elif board[0][0] == 'O':
                    victory_user = True
                else:
                    pass
            elif board[0][2] == board[1][1] == board[2][0]:
                if board[0][2] == 'X':
                    victory_computer = True
                elif board[0][2] == 'O':
                    victory_user = True
                else:
                    pass
    if victory_user:
        print("User has won! Congratulations! \n")
        game_status = True
    elif victory_computer:
        game_status = True
        print("User has lost! Wahhh! Try again! \n")
    else:
        game_status = False
    return game_status

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print('Current board:')
    display_board(board)
    global computer_move
    computer_move = True
    while computer_move:
        for i in range(10):
            trial_number = randrange(10)
        for x in range(3):
            for y in range(3):
                if trial_number == board[x][y]:
                    board[x][y] = "X"
                    computer_move = False
                    print("Computer's move succesful. \n")
                    pause_screen()
                    return board, computer_move
                else:
                    computer_move = True
    return board, computer_move

def pause_screen():
    print("Press enter to continue...")
    input()

def make_board():
    #definir tabuleiro
    global computer_move
    global board
    board = [['' for i in range(3)] for j in range(3)]
    write_positions = 1
    for x in range(3):
        for y in range(3):
            board[x][y] = write_positions
            write_positions += 1
    for space in board:
        print(space)
    print("Inserting first move.")
    board[1][1] = 'X'
    computer_move = False
    pause_screen()
    for space in board:
        print(space)
    print("\n")
    return board, computer_move

def end_game(board):
    confirmation = int(input("Giving up? \n"\
                             "1 - End game. \n"\
                             "0 - No. Go back. It's on!!!\n"))
    if confirmation == 1:
        board = []
        return board, True
    else:
        return False

def check_if_list_was_created():
    if not board:
        print("Oh, man! You didn't start the game yet. The board is empty. \n")
        return False
    else:
        return True

def print_menu():
    global board
    while True:
        op = int(input("1 - Make a move. \n"\
                       "2 - Draw board. \n"\
                       "3 - List free fields. \n"\
                       "4 - End game. \n"\
                       "0 - Return to previous menu. \n"))
        if op == 0:
            print("Bye!!")
            break
        elif op == 1: #make a move
            if check_if_list_was_created() == False:
                pass
            else:
                print("Checkin: computer move status - ", computer_move)
                pause_screen()
                if computer_move == False:
                    enter_move(board)
                    victory_for(board)
                    if game_status:
                        break
                    pass
                elif computer_move == True:
                    print("Computer's turn now. \n")
                    draw_move(board)
                    display_board(board)
                    victory_for(board)
                    if game_status:
                        break
        elif op == 2: #draw board
            if check_if_list_was_created() == False:
                pass
            else:
                display_board(board)
        elif op == 3: #list free fields
            make_list_of_free_fields(board)            
        elif op == 4: #end game
            if end_game(board):
                break
            else:
                pass            
        else:
            print("I dont know what to do. Restarting...")
            print("\n")


board = []
#se estiver na vez do usuário, computer move = false
while True:
    op = int(input("Select an option: \n"\
                    "0 - Exit \n"\
                    "1 - Start game \n"))
    if op == 0:
        print("Bye!!")
        break
    elif op == 1:
        print("Drawing the board and making the first move. \n")
        make_board()
        print_menu()
    else:
        print("I dont know what to do. Restarting...")
