# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):

    if merkkijono == "":
        merkkijono = "*"

    print(merkkijono[0] * leveys)

def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0
    
    while i < koko:
        viiva(koko, "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
    print()
    risunelio(3)
