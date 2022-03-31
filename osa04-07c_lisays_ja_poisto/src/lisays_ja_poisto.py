# Kirjoita ratkaisu tähän
from re import L


list = []
print("Lista on nyt", list)
i = 1

while True:
    command = input("(l)isää, (p)oista vai e(x)it: ")

    if command == "l":
        list.append(i)
        i += 1
    elif command == "p":
        list.pop(-1)
        i -= 1
    elif command == "x":
        print("Moi!")
        break

    print("Lista on nyt", list)