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
            print(c, end = "")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()

def kopioi_ja_lisaa(sudoku: list, row: int, column: int, number: int):
    new = []
    for r in sudoku:
        new.append(r[:])
 
    new[row][column] = number
    return new


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

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)