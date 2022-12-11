# Constants
import sys, random

# constants used for displaying the board:
EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_0 = '0'
BOARD_WIDTH = 7
BOARD_HEIGHT = 6

COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')

def main():
    # Set up the game:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:
        displayBoard(gameBoard)
        playerMove = askPlayerForMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print('Player' + playerTurn + ' has won!')
            sys.exit()

        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print('There is a tie!')

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_0
        elif playerTurn == PLAYER_0:
            playerTurn = PLAYER_X

def getNewBoard():
    board = {}
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            board[(x, y)] = EMPTY_SPACE
    return board

def displayBoard(board):
    print('1234567'.center(10, ' '))
    print('+.......+')
    for y in range(BOARD_HEIGHT):
        print('|', end='')
        for x in range(BOARD_WIDTH):
            print(board[(x, y)], end='')
        print('|')
    print('+.......+')

# displayBoard(newBoard)
def askPlayerForMove(playerTile, board):
    # Prompt user input
    # Quit if user enters 'Quit'
    # Ask again if the user enters an invalid input
    # Determine if  column is occupied
    while True:
        print('Player {}, enter the column or QUIT'.format(playerTile))
        response = input('>' )

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue # Ask player again for their move

        columnIndex = int(response) - 1 # -1 for 0-based the index.

        # If the column is full, ask for a move again:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue # Ask player again for their move.

        # Starting from the bottom, find the first empty space
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    # x loop
    for x in range(BOARD_WIDTH):
        # y loop
        for y in range(BOARD_HEIGHT):
                if board[(x, y)] == EMPTY_SPACE:
                    return False
    return True


def isWinner(playerTile, board):
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going right down diagonal:
            tile1 = board[(columnIndex , rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex)]
            tile3 = board[(columnIndex + 1, rowIndex + 1)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
    