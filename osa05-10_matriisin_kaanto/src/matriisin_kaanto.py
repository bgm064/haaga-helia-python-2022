# tee ratkaisu tänne
def transponoi(matrix: list):
    copy = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = copy[i][j]


if __name__ == "__main__":
    transponoi([[1, 2, 3],[4, 5, 6],[7, 8, 9]])