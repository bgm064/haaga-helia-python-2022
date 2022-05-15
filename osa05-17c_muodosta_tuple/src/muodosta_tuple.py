# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
    tuple = []

    tuple.append(x)
    tuple.append(y)
    tuple.append(z)

    smallest = min(tuple)
    largest = max(tuple)
    total = sum(tuple)

    tuple = (smallest, largest, total)
    
    return(tuple[0], tuple[1], tuple[2])


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))