# tee ratkaisu tänne
import random

def lyhin(lista):
    name_list = []

    for i in lista:
        if len(name_list) == 0 or len(i) < len(name_list[0]):
            name_list = [i]
            
        elif len(i) == len(name_list[0]):
            name_list.append(i)

    return random.choice(name_list)

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = lyhin(lista)
    print(tulos) # ['emilia', 'juhani']
    lista = ["jani", "topi", "elmeri", "kasper"]
    tulos = lyhin(lista)
    print(tulos) # ['eka']
