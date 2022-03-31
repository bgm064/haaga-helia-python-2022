# tee ratkaisu tänne
def viiva(leveys, merkkijono):

    if merkkijono == "":
        merkkijono = "*"

    print(merkkijono[0] * leveys)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")
