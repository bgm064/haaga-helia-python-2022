# tee ratkaisu tänne
def poista_pienin(numbers):
    numbers.remove(min(numbers))


if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)