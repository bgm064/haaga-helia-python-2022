# Kirjoita ratkaisu tähän
string = input("Anna merkkijono: ")
chars = len(string) - 1

while chars >= 0:
    print(string[chars:])
    chars -= 1