# tee ratkaisu tänne
def pisimman_pituus(lista):
    name_list = []

    for i in lista:
        if len(name_list) == 0 or len(i) > len(name_list[0]):
            name_list = [i]
            longest = len(i)

    return longest


if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)