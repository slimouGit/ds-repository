class TicTacToe():
    playground = [["_", "_", "_"],
                  ["_", "_", "_"],
                  ["_", "_", "_"]]

    def __init__(self, playground):
        self.playground = playground

def verifyScore(sign:str):
    #horizontal check
    if((TicTacToe.playground[0][0] == sign) and (TicTacToe.playground[0][1] == sign) and (TicTacToe.playground[0][2] == sign)):
        return 1
    elif((TicTacToe.playground[1][0] == sign) and (TicTacToe.playground[1][1] == sign) and (TicTacToe.playground[1][2] == sign)):
        return 1
    elif ((TicTacToe.playground[2][0] == sign) and (TicTacToe.playground[2][1] == sign) and (TicTacToe.playground[2][2] == sign)):
        return 1
    #vertical check
    elif ((TicTacToe.playground[0][0] == sign) and (TicTacToe.playground[1][0] == sign) and (TicTacToe.playground[2][0] == sign)):
        return 1
    elif ((TicTacToe.playground[0][1] == sign) and (TicTacToe.playground[1][1] == sign) and (TicTacToe.playground[2][1] == sign)):
        return 1
    elif ((TicTacToe.playground[0][2] == sign) and (TicTacToe.playground[1][2] == sign) and (TicTacToe.playground[2][2] == sign)):
        return 1
    #diagonal check
    elif ((TicTacToe.playground[0][0] == sign) and (TicTacToe.playground[1][1] == sign) and (TicTacToe.playground[2][2] == sign)):
        return 1
    elif ((TicTacToe.playground[2][0] == sign) and (TicTacToe.playground[1][1] == sign) and (TicTacToe.playground[0][2] == sign)):
        return 1
    else:
        return 0

def verifyMove(row, col):
    if(row>2 or col>2):
        return 0
    elif(TicTacToe.playground[row][col]=="_"):
        return 1
    else:
        return 0

def play(sign:str, row:int, col:int):
    TicTacToe.playground[row][col] = sign
    printPlayground(TicTacToe.playground)
    if(verifyScore(sign)):
        print(sign, "hat gewonnen")
    else:
        getInput()

def getInput():
    sign = input("Dein Zeichen:\n")
    row = int(input("Welche Reihe bespielen:\n"))
    col = int(input("Welche Zeile bespielen:\n"))
    if(verifyMove(row, col)):
        play(sign, row, col)
    else:
        print("Ungueltiger Spielzug")
        getInput()

def printPlayground(playground):
    print("",playground[0],"\n",playground[1],"\n",playground[2])

getInput()
