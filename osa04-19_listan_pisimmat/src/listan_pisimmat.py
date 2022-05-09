# tee ratkaisu tänne
def pisimmat(lista):
    name_list = []

    for i in lista:
        if len(name_list) == 0 or len(i) > len(name_list[0]):
            name_list = [i]
            
        elif len(i) == len(name_list[0]):
            name_list.append(i)

    return name_list

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['emilia', 'juhani']