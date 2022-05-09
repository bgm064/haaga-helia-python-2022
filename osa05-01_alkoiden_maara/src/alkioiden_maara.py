# tee ratkaisu tänne
def laske_alkiot(list, search):
    found = 0
    for row in list:
        for element in row:
            if element == search:
                found += 1
    
    return found


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))