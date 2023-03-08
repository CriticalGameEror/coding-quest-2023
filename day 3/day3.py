with open("input.txt") as f:
    input = f.readlines()

# checks if a set has 3 in a row
def checkWin(set):
    if 1 in set and 2 in set and 3 in set:
        return True
    elif 4 in set and 5 in set and 6 in set:
        return True
    elif 7 in set and 8 in set and 9 in set:
        return True
    elif 1 in set and 4 in set and 7 in set:
        return True
    elif 2 in set and 5 in set and 8 in set:
        return True
    elif 3 in set and 6 in set and 9 in set:
        return True
    elif 1 in set and 5 in set and 9 in set:
        return True
    elif 3 in set and 5 in set and 7 in set:
        return True
    else:
        return False

oWins = 0
xWins = 0
draws = 0

# checks each game
for line in input:
    isDraw = True
    currentSquaresO = set()
    currentSquaresX = set()
    xTurn = True
    for square in line.strip().split():
        if xTurn:
            xTurn = False
            currentSquaresX.add(int(square))
            # if X has won
            if checkWin(currentSquaresX):
                xWins += 1
                isDraw = False
                break
        else:
            xTurn = True
            currentSquaresO.add(int(square))         
            # if O has won
            if checkWin(currentSquaresO):
                oWins += 1
                isDraw = False
                break
    # if it is a draw
    if isDraw:
        draws += 1

print(xWins * oWins * draws)