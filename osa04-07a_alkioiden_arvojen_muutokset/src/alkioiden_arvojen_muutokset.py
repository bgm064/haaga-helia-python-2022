# Kirjoita ratkaisu tähän
list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Anna indeksi: "))

    if index == -1:
        break
    elif index < 0 or index >= len(list):
        print("Indeksi on listan ulkopuolella")
    else:
        value = int(input("Anna arvo: "))
        list[index] = value
        print(list)