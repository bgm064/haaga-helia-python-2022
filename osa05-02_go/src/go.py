# tee ratkaisu tänne
def kumpi_voitti(board: list):
    player1 = 0
    player2 = 0

    for row in board:
        for square in row:
            if square == 1:
                player1 +=1
            elif square == 2:
                player2 += 1

    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    else:
        return 0
    
    
if __name__ == "__main__":
    lauta = [ [1,2,1], [1,0,2], [0,2,2] ]
    print(kumpi_voitti(lauta))