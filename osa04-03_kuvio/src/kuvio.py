# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(leveys, merkkijono):

    if merkkijono == "":
        merkkijono = "*"

    print(merkkijono[0] * leveys)

def kuvio(rivi, x, koko, y):
    i = 0

    while i < rivi:
        i += 1
        viiva(i, x)
    
    i = 0

    while i < koko:
        viiva(rivi, y)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")