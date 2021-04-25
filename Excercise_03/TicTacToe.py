class TicTacToe():
    def __init__(self, playground:list):
        if(playground):
            #show initial playground
            printPlayground(playground)
            getInput(playground)
        else:
            print("no playground defined")

#1. get user input
def getInput(playground:list):
    sign:str = input("Dein Zeichen:\n") #Sign of user
    row:int = int(input("Welche Reihe bespielen:\n"))
    col:int = int(input("Welche Zeile bespielen:\n"))
    handleInput(playground, sign, row, col)

#2. handle userinput
def handleInput(playground:list, sign:str, row:int, col:int):
    # ckeck input is validate move
    if (verifyMove(playground, row, col)):
        play(playground, sign, row, col)
    else:
        print("Ungueltiger Spielzug")
        getInput(playground)

#3. function checks move is at playground and in empty field
def verifyMove(playground:list,row:int, col:int):
    #move is in range of playground
    if(row>(len(playground)-1) or col>(len(playground)-1)):
        return 0
    #move is on empty field
    elif(playground[row][col]=="_"):
        return 1
    else:
        return 0

#4. play users move
def play(playground:list, sign:str, row:int, col:int):
    #set sign on selected field
    playground[row][col] = sign
    #show current game state
    printPlayground(playground)
    #check game has to continue or is won by player
    if(verifyScore(playground, sign)):
        print("\n************************")
        print(sign, "hat gewonnen")
        print("************************")
    else:
        getInput(playground)

#5. print each row in playground
def printPlayground(playground:list):
    for i in range(len(playground)):
        print(playground[i])

#6. function checks game state at every move
def verifyScore(playground:list, sign:str):
    #horizontal check
    for i in range(len(playground)):
        if((playground[i][0] == sign) and (playground[i][1] == sign) and (playground[i][2] == sign)):
            return 1
    #vertical check
    for i in range(len(playground)):
        if ((playground[0][i] == sign) and (playground[1][i] == sign) and (playground[2][i] == sign)):
            return 1
    #diagonal check
    if ((playground[0][0] == sign) and (playground[1][1] == sign) and (playground[2][2] == sign)):
        return 1
    elif ((playground[2][0] == sign) and (playground[1][1] == sign) and (playground[0][2] == sign)):
        return 1
    else:
        return 0

#---------------------------------------------------------------------------------------------------

#INITIALIZE PLAYGROUND AND TICTACTOE OBJECT

#multidimensional array as playground
playground:list = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

#start game with new TicTacToe object
TicTacToe(playground)
