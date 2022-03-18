# Kirjoita ratkaisu tähän
until = int(input("Mihin asti: "))
multiplier = int(input("Mikä kerroin: "))
counter = 1
print(counter)

while counter < until and counter * multiplier <= until:
    counter *= multiplier
    print(counter)