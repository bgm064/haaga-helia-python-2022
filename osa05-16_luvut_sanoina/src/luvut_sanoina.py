# tee ratkaisu tänne
def lukukirja():
    singles = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
    numbers = {}

    for i in range(10):
        numbers[i] = singles[i]

    numbers[10] = "kymmenen"
 
    for i in range(1, 10):
        numbers[i + 10] = singles[i] + "toista"
 
    for i in range(2, 10):
        numbers[i * 10] = singles[i] + "kymmentä"
        for j in range(1, 10):
            numbers[i * 10 + j] = singles[i] + "kymmentä" + singles[j]
 
    return numbers


if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])