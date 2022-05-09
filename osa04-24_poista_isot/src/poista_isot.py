# tee ratkaisu tänne
def poista_isot(list):
    new_list = []
    for string in list:
        if not string.isupper():
            new_list.append(string)

    return new_list

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)