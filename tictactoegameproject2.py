# DISPLAY BOARD

def display_board(board):

    print('\n'*100)
    print('   |   |')
    print(' '+board[7]+' | ' + board[8] + ' | '+board[9])
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | ' + board[5] + ' | '+board[6])
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | ' + board[2] + ' | '+board[3])


#PLAYER INPUT

def player_input():

    '''
    OUTPUT=(Player 1 marker, Player 2 marker)

    '''

    marker=''

    while not (marker=='X' or marker=='O'):
        marker=input('Player1: Choose X or O : ').upper()

    if marker=='X':
        return('X','O')
    else:
        return('O','X')


# PLACE MARKER

def place_marker(board, marker, position):
    board[position] = marker


# WIN CHECK

def win_check(board,mark):

    #SEE IF ALL ROWS OR COLOUMNS OR DIAGONALS HAS THE SAME MARKERS?
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[3]==mark and board[5]==mark and board[7]==mark))


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1 '
    else:
        return 'Player 2 '

def space_check (board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position between 1 and 9 : '))
    return position

def replay():
    choice = input('Play again? Enter Yes or NO ?')
    return choice=='Yes'

#WHILE LOOP TO KEEP RUNNING THE GAME
print("Welcome to Tic Tac Toe")

while True:
    #Play the game

    ##Set Up - Board,  Whose First, Choose Markers X, O
    the_board=[' ']*10
    Player1_marker,Player2_marker=player_input()

    turn=choose_first()
    print(turn + 'will go first')

    play_game=input('Ready to play? Y or N : ')

    if  play_game=='Y':
        game_on = True
    else:
        game_on=False

    ### Game Play

    while game_on:

        if turn == 'Player 1':

            #Show the board
            display_board(the_board)

            #Choose a position
            position = player_choice(the_board)

            #Place the marker on the position
            place_marker(the_board,Player1_marker,position)

            #Check if they won
            if win_check(the_board,Player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE Game!")
                    game_on=False
                else:
                    turn='Player 2'

        else:

             #Show the board
            display_board(the_board)

            #Choose a position
            position=player_choice(the_board)

            #Place the marker on the position
            place_marker(the_board,Player2_marker,position)

            #Check if they won
            if win_check(the_board,Player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    game_on=False
                else:
                    turn='Player 1'

    if not replay():
            break


                    







        


