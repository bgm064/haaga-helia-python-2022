# tee ratkaisu tänne
def rivi_oikein(sudoku: list, row: int):
    numbers = []
    for number in sudoku[row]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True 

def sarake_oikein(sudoku: list, column: int):
    numbers = []
    for row in sudoku:
        number = row[column]
        if number > 0 and number in numbers:
            return False
        numbers.append(number) 
    return True

def nelio_oikein(sudoku: list, row: int, column: int):
    numbers = []
    for r in range(row, row + 3):
        for c in range(column, column + 3):
            number = sudoku[r][c]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
    return True

def sudoku_oikein(sudoku: list):
    results = []
    
    row = 0
    while row < 9:
        results.append(rivi_oikein(sudoku, row))
        row += 1

    column = 0
    while column < 9:
        results.append(sarake_oikein(sudoku, column))
        column += 1

    squares = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    i = 0
    while i < 9:
        results.append(nelio_oikein(sudoku, squares[i][0], squares[i][1]))
        i += 1
    print(results)

    for result in results:
        if result is False:
            return False
            
    return True


if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    
    print(sudoku_oikein(sudoku2))