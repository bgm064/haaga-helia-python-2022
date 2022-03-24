# Kirjoita ratkaisu tähän
string = input("Anna merkkijono: ")
index = -1
chars = ""

while index < len(string) - 1:
    index += 1
    chars += string[index]
    print(chars)