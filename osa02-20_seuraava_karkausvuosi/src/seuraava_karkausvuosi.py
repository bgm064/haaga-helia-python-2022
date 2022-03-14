# Kirjoita ratkaisu tähän
start = int(input("Vuosi: "))
year = start + 1

while True:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        break
    year += 1

print(f"Vuotta {start} seuraava karkausvuosi on {year}")