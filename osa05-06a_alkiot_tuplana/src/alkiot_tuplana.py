# tee ratkaisu tänne
def tuplaa_alkiot(numbers):
    doubles = []
    for number in numbers:
        doubles.append(number * 2)
    
    return doubles


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)