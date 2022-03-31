# tee ratkaisu tänne
def positiivisten_summa(numbers: list):
    sum = 0

    for i in numbers:
        if i > 0:
            sum += i

    return sum


if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)