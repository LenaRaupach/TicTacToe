def player1Sign():
    player1 = input("Hello! Do you want to be X or O?\t").lower()
    return player1


def player2Sign(player1):
    if player1 == "x":
        player2 = "o"
    else:
        player2 = "x"
    return player2

def ready():
    ready = False
    while ready == False:
        answer = input("Are you ready? Write yes or no!\t")
        if answer == "yes":
            ready = True

def displayBoard(board):
    print("\n   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |\n")
    return board

def previewField():
    print("\nThis is the field. In order to place your sign, write the associative number.\n")
    displayBoard(["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    ready()


def askMove(player, again="no"):
    if again == "no":
        print("It's {}'s turn. ".format(player))
        move = int(input("Where do you place your sign?\t\t"))
    else:
        move = int(input("this field is alredy taken, {}! choose another one! \t".format(player)))
    return move

def setMove(move, board, player):
    board[move] = player
    return board

def playersTurn(player):
    if player == "Player1":
        newplayer = "Player2"
    else:
        newplayer = "Player1"
    return newplayer

def checkDone(board):
    strike = False
    if board[1]=="x" or board[1]=="o":
        if board[1]==board[2]==board[3] or board[1]==board[4]==board[7] or board[1]==board[5]==board[9]:
            strike = True
    if board[5]=="x" or board[5]=="o":
        if board[4]==board[5]==board[6] or board[2]==board[5]==board[8]:
            strike = True
    if board[9]=="x" or board[9]=="o":
        if board[7]==board[8]==board[9] or board[3]==board[6]==board[9]:
            strike = True
    if board[3]=="x" or board[3]=="o":
        if board[3]==board[5]==board[7]:
            strike = True
    return strike

def checkFull(board):
    c = 0
    for i in range(1, len(board)):
        if board[i] != " ":
            c += 1
    if c == 9:
        return True
    else:
        return False

if __name__ == "__main__":
    done = False
    full = False
    player = "Player1"
    player1 = player1Sign()
    player2 = player2Sign(player1)
    previewField()
    board = displayBoard(["#", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    while done == False and full == False:
        move = askMove(player)
        if move in range(1,10):
            while board[move] != " ":
                move = askMove(player, "yes")
            else:
                if player == "Player1":
                    board = setMove(move, board, player1)
                else:
                    board = setMove(move, board, player2)
            board = displayBoard(board)
            done = checkDone(board)
            full = checkFull(board)
            player = playersTurn(player)
        else:
            print("\nChoose a field between 1 and 9!\n")
    else:
        if done == True:
            print("Done! {} won!".format(player))
        elif full == True:
            print("Field is full.")