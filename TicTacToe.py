#!/usr/bin/python

#const
x = 'X'
o = 'O'
empty = " "
tie = 'Tie'
numSquares = 9

def displayInstruct():
    #Displays instruction of the game
    print("""
        Welcome to Tic-Tac-Toe game! Your brain will fight against computer's processor!
        Are You ready? 
        So, our board looks like that :
        
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
        
        You just have to choose, who starts and then just write a number of field, which You want to mark! \n
    """)

def question():
        odp = None
        while odp != '0' and odp != '1':
            odp = input('Write 0 if You want to start! Else write 1')
        return odp

def whoStarts():
    #Here we are
    first = question()
    if first == '0':
        print('You have the first move! You are also the X')
        human = x
        pc = o
    else:
        print('Computer has the first move! You are also the O')
        human = o
        pc = x
    return pc, human

def newBoard():
    #Creates new, empty board (according to previously data)
    board = []
    for square in range(numSquares):
        board.append(empty)
    return board

def displayBoard(board):
    #Displays board on the screen
    print("\n \t", board[0]," | ", board[1], " | ", board[2])
    print("    -------------")
    print("\t", board[3], " | ", board[4], " | ", board[5])
    print("    -------------")
    print("\t", board[6], " | ", board[7], " | ", board[8])

def legalMoves(board):
    move = []
    for square in range(numSquares):
        if board[square] == empty:
            move.append(square)
    return move

def winner(board):
    #Determine the winner of the game
    winCombo = ((0,1,2),
                (3,4,5),
                (6,7,8),
                (0,3,6),
                (1,4,7),
                (2,5,8),
                (0,4,8),
                (2,4,6))
    for row in winCombo:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
    if empty not in board:
        return tie
    return None

def humanMove(board, human):
    #Read human's move
    legal = legalMoves(board)
    move = None
    while move not in legal:
        try:
            move = int(input('Make Your move!'))
            if move not in legal:
                print('\n Wpisałeś złe pole, wybierz inne!')
        except ValueError: print('Choose the right square!')
    return move

def computerMove(board, pc, human):
    #Computer is making it's move!
    #At the beginning, we are creating working-on-board, because we will change the board list
    board = board[:]

    #Now we are making tuple of best moves for pc
    bestMoves = (4,0,2,6,8,1,3,5,7)
    print("I choose square number ", end='')

    #If pc can win, make this move
    for move in legalMoves(board):
        board[move] = pc
        if winner(board) == pc:
            print(move)
            return move
        #This move has been checked, here we are removing it, for clearing the workBoard
        board[move] = empty

    #If human can win in next move, block that
    for move in legalMoves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #This move has been checked, here we are removing it, for clearing the workBoard
        board[move] = empty

    #If nobody can win in next move, chose the best free square
    for move in bestMoves:
        if move in legalMoves(board):
            print(move)
            return move

def nextTurn(turn):
    #Now, we are changing the moving person
    if turn == x:
        return o
    else:
        return x

def congrats(theWinner, pc, human):
    #Just congratulations!
    if theWinner != tie:
        print(theWinner, "wins!")
    else:
        print('Draw!')

    if theWinner == pc:
        print('Me, the almighty computer, is winner again! MWAHAHAHA')
    elif theWinner == human:
        print('Human masterrace!')
    elif theWinner == tie:
        print("So, it's a draw. Till the next time!")



def main():
    displayInstruct()
    pc, human = whoStarts()
    turn = x
    board = newBoard()
    displayBoard(board)

    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, pc, human)
            board[move] = pc
        displayBoard(board)
        turn = nextTurn(turn)

    theWinner = winner(board)
    congrats(theWinner, pc, human)



main()
input('For end the game, press Enter')








