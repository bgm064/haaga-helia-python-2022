# Kirjoita ratkaisu tähän
string = input("Anna merkkijono: ")
part = input("Anna osajono: ")

first = string.find(part)
string = string[first + len(part):]
second = string.find(part)

if second != -1:
    print("Osajonon toinen esiintymä on kohdassa " + str(first + second + len(part)) + ".")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")