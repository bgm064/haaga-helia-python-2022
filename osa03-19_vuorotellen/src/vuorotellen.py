# Kirjoita ratkaisu tähän
first = 1
second = int(input("Anna luku: "))

while first < second:
    print(first)
    print(second)

    first += 1
    second -= 1

if first == second:
    print(first)