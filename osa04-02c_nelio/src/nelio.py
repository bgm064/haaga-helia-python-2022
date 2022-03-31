# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):

    if merkkijono == "":
        merkkijono = "*"

    print(merkkijono[0] * leveys)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0

    while i < koko:
        viiva(koko, merkki)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
    print()
    nelio(3, "o")
