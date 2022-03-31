# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):

    if merkkijono == "":
        merkkijono = "*"

    print(merkkijono[0] * leveys)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0

    while i < koko:
        i += 1
        viiva(i, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
    print()
    kolmio(3)
