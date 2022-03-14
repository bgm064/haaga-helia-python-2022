from math import sqrt
# Kirjoita ratkaisu tähän

while True:
    num = int(input("Syötä luku: "))
    if num == 0:
        print("Lopetetaan...")
        break
    elif num < 0:
        print("Epäkelpo luku")
    else:
        print(sqrt(num))