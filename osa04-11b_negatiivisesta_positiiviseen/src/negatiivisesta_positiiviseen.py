# Kirjoita ratkaisu tähän
num = int(input("Anna luku: "))

for i in range(-num, num+1):
    if i == 0:
        continue
    print(i)

    # Koska Pythonissa bool-tyyppi vastaa arvoja
    # 0 ja 1 (False ja True), voitaisiin ehto kirjoittaa myös näin:
    # if i:
       # print(i)