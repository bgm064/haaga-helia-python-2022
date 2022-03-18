# Kirjoita ratkaisu tähän
str = input("Anna merkkijono: ")
counter = 0
place = -1

while counter < len(str):
    print(str[place])
    counter += 1
    place -= 1
