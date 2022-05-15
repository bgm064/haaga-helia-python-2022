# tee ratkaisu tänne
def tulosta(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for char in row:
            s += 1
            if char == 0:
                char = "_"
            c = f"{char} "
            if s % 3 == 0 and s < 8:
                c += " "
            print(c, end="")
 
        print()
        r += 1
        if r % 3 == 0 and r < 8:
            print()
 
def lisays(sudoku: list, row: int, column: int, number: int):
    sudoku[row][column] = number


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)