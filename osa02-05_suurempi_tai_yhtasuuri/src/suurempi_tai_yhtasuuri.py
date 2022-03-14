# Kirjoita ratkaisu tähän
first = int(input("Anna ensimmäinen luku:"))
second = int(input("Anna toinen luku:"))

if first > second:
    print(f"Suurempi luku: {first}")
elif first < second:
    print(f"Suurempi luku: {second}")
else:
    print("Luvut ovat yhtä suuret!")