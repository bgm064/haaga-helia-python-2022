# Kirjoita ratkaisu tähän
numbers = []

while True:
    num = int(input("Anna luku: "))
    numbers.append(num)

    if num == 0:
        print("Moi!")
        break

    print("Lista:", numbers)
    print("Järjestettynä:", sorted(numbers))