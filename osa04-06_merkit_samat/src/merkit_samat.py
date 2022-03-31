# tee ratkaisu tänne
def samat(string, a, b):
    if a >= len(string) or b >= len(string):
        return False
    return string[a] == string[b]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2))
    print()
    print(samat("abc", 0, 3))
    print()
    print(samat("koodari", 0, 10))