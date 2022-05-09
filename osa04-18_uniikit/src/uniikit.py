# tee ratkaisu tänne
from enum import unique


def uniikit(numbers: list):
    unique_list = []
    unique_numbers = set(numbers)

    for i in unique_numbers:
        unique_list.append(i)

    return sorted(unique_list)


if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]
    lista = [1, 10, 100, 1000]
    print(uniikit(lista))