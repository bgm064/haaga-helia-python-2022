# tee ratkaisu tänne
def parilliset(numbers: list):
    even = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)

    return even


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)